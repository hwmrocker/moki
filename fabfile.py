from fabric.api import *

env.hosts = ['gladis@gladis.org']
env.roledefs = {'gweb':['gladis@gladis.org']}

@task
def uptime():
    run('uptime')


@task
def deploy():
    with cd('/home/gladis/webapps/mokiapp/moki'):
        run('git fetch')
        run('git rebase origin/master')

    with cd('/home/gladis/webapps/mokiapp/apache2/bin'):
        run('./restart')
