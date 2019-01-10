Vagrant.configure('2') do |config|
  config.vm.box = 'azure-lsp'

  #Para permitir la conexion ssh
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|


    azure.tenant_id = "4fa7xxxx-xxxx-xxxx-xxxx-xxxxe8e1d1cd"
    azure.client_id = "21e9xxxx-xxxx-xxxx-xxxx-xxxx10c59656"
    azure.client_secret ="dcacxxxx-xxxx-xxxx-xxxx-xxxx23322cef"
    azure.subscription_id = "45aexxxx-xxxx-xxxx-xxxx-xxxx8f9cf14f"


    azure.vm_name = "libsepebot"
    azure.vm_size = "Standard_B1s"
    azure.location = "northeurope"
    azure.admin_username = "libsepe_admin"
    azure.vm_password = 'ClavE'

  end




  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end

end
