from fabric.api import *

env.user = 'daniel-rasp'
env.hosts = ['27.35.13.110:227']
env.activate = 'source venv/bin/activate && source .env'

def pre_install():
    sudo('apt-get install -y git')
    sudo('pip install autoenv virtualenv')
    run('echo "source `which activate.sh`" >> ~/.bashrc')

def create_venv():
    pass

def env_update():
    local("pip install -r requirements.txt")



def hello():
    print("Hello world!")
