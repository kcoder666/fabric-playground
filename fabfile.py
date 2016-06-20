from fabric.api import local

def prepare_deploy():
    local("./manage.py test web_app")
    local("git add -i && git commit")
    local("git push")

