from fabric.api import run


def runApp():

     # Iniciamos el servicio web
     run('python3 /home/vagrant/LibSePeBOT-IV/app.py')

def updateApp():

    run("rm -rf /home/vagrant/LibSePeBOT-IV")

    run("git clone https://github.com/GinesNC/LibSePeBOT-IV.git /home/vagrant/LibSePeBOT-IV")
