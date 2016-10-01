from fabric.api import *
import sys
project = 'flask_example_page'
port = '8807'

env.activate = 'source venv/bin/activate && source .env'
env.location = 'cd ~/' + project

def pre_install():
    sudo('apt-get install -y git')
    sudo('pip install virtualenv')

def install():
    run('rm -rf ' + project)
    run('git clone https://github.com/DanielTimLee/' + project)
    with prefix(env.location):
        run('virtualenv --python=python3 venv')
        with prefix(env.activate):
            run('pip install -r requirements.txt')

def run_server():
    with prefix(env.location):
        run('python app.py '+port)

def deploy():
    pre_install()
    install()
    run_server()

def source_update():
    with prefix(env.location):
        run('git pull origin')

def env_update():
    with prefix(env.location):
        with prefix(env.activate):
            run("pip install -r requirements.txt")

def update():
    source_update()
    env_update()
    run_server()
