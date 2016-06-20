from fabric.api import local, settings, abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local("./manage.py test web_app", capture=True)
    if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")


def commit():
    local("git add -i && git commit")


def push():
    local("git push")


def prepare_deploy():
    test()
    commit()
    push()

