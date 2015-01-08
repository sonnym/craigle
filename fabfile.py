from fabric.api import local, env, sudo, cd

def deploy(environment):
    configure_env(environment)

    with cd( '/srv/craigle'):
        sudo('git pull')

        sudo('venv/bin/pip3 install -r requirements.txt')

        sudo('venv/bin/python3 manage.py migrate --noinput')
        sudo('venv/bin/python3 manage.py collectstatic --noinput')

        sudo('sudo systemctl reload-or-restart httpd supervisord')

        sudo('venv/bin/python3 manage.py rqenqueue "importers.run"')

def configure_env(environment):
    resolve_key_filename(environment)

    env.host_string = resolve_host(environment)
    env.user = resolve_user(environment)

def resolve_host(environment):
    if environment == 'production':
        return 'craigle.us'
    elif environment == 'testing':
        host_name_line = local ('vagrant ssh-config | grep HostName', capture=True)
        port_line = local ('vagrant ssh-config | grep Port', capture=True)

        return "%s:%s" % (host_name_line.split()[1], port_line.split()[1])

def resolve_user(environment):
    if environment == 'production':
        return 'sonny'
    elif environment == 'testing':
        return 'vagrant'

def resolve_key_filename(environment):
    if environment == 'testing':
        id_file_line = local('vagrant ssh-config | grep IdentityFile', capture=True)
        env.key_filename = id_file_line.split()[1]
