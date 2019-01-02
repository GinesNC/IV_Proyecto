# Provisionamiento, despliegue y ejecución automática

Las configuraciones necesarias para conseguir esto son:

## Configuración local

En primer lugar para un despliegue desde cero hay que configurar varias cosas. Una de ellas es el entorno local, en el cual hay que instalar Vagrant y Azure CLI. Hacer login en Azure, establecer la suscripción con la que se va a trabajar y crear el directorio activo de azure (ADD).

Con `az login` se hace el login en Azure y muestra las suscripciones disponibles.
Tras esto y aunque ya está establecida por defecto, pongo la que está activa:

      az account set -s <id>

donde en *id* se corresponde con el campo *id* de la suscripción que devuelve `az login`.

Ahora se crea el ADD con acceso a la cuenta de Azure y a la suscripción correspondiente.

    az ad sp create-for-rbac

Tras esta ejecución devuelve un *id* de la aplicación, un password y un *tenantID*. Estos valores son los que se deben poner en las variables correspondientes del Vagrantfile. También se pueden crear como variables de entorno, como `export NOMBRE_VARIABLE="valor variable"`, para que no aparezca esa información delicada en el fichero.

## Configuración del provisionamiento

En el siguiente paso es crear el fichero para realizar el provisionamiento. En el cual se indicará todo lo que la máquina tiene que tener instalado. Para ello uso Ansible y este *playbook.yml*:

    - hosts: all
      remote_user: vagrant

      tasks:

      - name: Instalar GitHub,
        sudo: true
        apt:
          name: git
          state: present

      - name: Install Python 3
        sudo: true
        apt:
          name: python3
          state: present
          update_cache: yes

      - name: Instalar pip
        sudo: true
        apt:
          name: python3-pip
          state: present
          update_cache: yes


      - name: clonar repositorio libsepe
        sudo: false
        git :
          repo: https://github.com/GinesNC/LibSePeBOT-IV.git
          dest: /home/vagrant/LibSePeBOT-IV
          force: yes

      - name: install requirements
        sudo: yes
        command: pip3 install -r /home/vagrant/LibSePeBOT-IV/requirements.txt


Donde indico que se haga para todos los host y que el usuario *vagrant* será el encargado de ejecutar las taras. Esas tareas están especificadas en la sección *task*, donde instalo git, python3, pip3, clono el repositorio e instalo todas las dependencias de mi aplicación que se encuentran en *requirements.txt*.

Con `state: present` se verifica el estado del paquete y si está instalado no lo vuelve a instalar, continuando con la ejecución.

En el caso de clonar el repositorio de GitHub, Ansible cuenta con el [modulo *git*](https://docs.ansible.com/ansible/latest/modules/git_module.html)  que facilita esta tarea.

# Configuración Vagrant

Hay que configurar el _Vagrantfile_ el cual para hacerlo me he ayudado de este [tutorial](https://blog.scottlowe.org/2017/12/11/using-vagrant-with-azure/) y del repositorio en [GitHub de azure](https://github.com/Azure/vagrant-azure).


    Vagrant.configure('2') do |config|
      config.vm.box = 'azure'

      config.ssh.private_key_path = '~/.ssh/id_rsa'
      config.vm.provider :azure do |azure, override|

        azure.tenant_id = ENV['AZURE_TENANT_ID']
        azure.client_id = ENV['AZURE_CLIENT_ID']
        azure.client_secret = ENV['AZURE_CLIENT_SECRET']
        azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

        azure.vm_name = "libsepebot-iv"
        azure.vm_size = "Standard_B1s"
        azure.location = "northeurope"


      end


      config.vm.provision "ansible" do |ansible|
        ansible.playbook = "/provision/playbook.yml"
      end

    end

Parte de este archivo se da en el repositorio de Azure. Las variables son del entorno y las que he creado con la información que he obtenido antes. Para que no le diese un nombre al azar he establecido el nombre con la variable `azure.vm_name`, he elegido el tamaño a uno básico, ya que no requiere de muchos recursos este proyecto. Y por último he establecido el servidor de _northeurope_ ya que he comparado precios y este era un poco más barato con respecto al de _westeurope_.
Y por último para que se haga el provisionamiento con Ansible y el *playbook.yml* creado antes.

Una vez hecho e instalado el pugling de Azure con `vagrant plugin install vagrant-azure`, se puede levantar la máquina con `vagrant up --provider=azure`. Esto creará la máquina y realizará el provisionamiento especificado.
Si posteriormente se realizan cambios en el *playbook.yml* se pueden aplicar con `vagrant provision`.

## Ejecución automática

Para la ejecución he usado Fabric y para el *fabfile.py* me he ayudado de la [documentación oficial](http://docs.fabfile.org/en/2.4/getting-started.html#run-commands-via-connections-and-run). Mi fichero a quedado así:

    from fabric.api import run


    def runApp():

         # Iniciamos el servicio web
         run('python3 /home/vagrant/LibSePeBOT-IV/app.py')

    def updateApp():

        run("rm -rf /home/vagrant/LibSePeBOT-IV/")

        run("git clone https://github.com/GinesNC/LibSePeBOT-IV.git /home/vagrant/LibSePeBOT-IV")


Donde puedo poner en funcionamiento la aplicación con `runApp()` o se puede actualizar con `updateApp()`.

Esto se puede hacer con la herramienta de Fabric, que es `fab` y se ejecutaría de esta forma:

      fab -H vagrant@40.112.90.212 updateApp   

Si el *fabfile.py* está en el mismo directorio. Pero si se encuentra en otro lugar hay que especificarlo con la opción `-f RUTA/fabfile.py`
