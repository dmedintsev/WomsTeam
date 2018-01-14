# coding=utf-8
import os
from fabric.api import run, env, cd, roles, sudo, reboot, settings

# Списком можно перечислить несколько серверов"

env.roledefs['git'] = [
    '95.85.20.67',
]

env.roledefs['central'] = ['95.85.20.67:22']

login = "djwoms"
password = "Djwoms25"

def production_central():
    """Окружение для продакшена
    """
    env.user = login
    env.password = password
    env.project_root = '/home/djwoms/djangochannel'
    env.timeout = 30
    env.shell = '/bin/bash -c'  # Используем шелл отличный от умолчательного (на сервере)
    env.python = '/home/djwoms/my/bin/python'

@roles('central')
def restart():
    """ Применение кода питон
        Перезагрузка supervisor
    """
    production_central()
    sudo('supervisorctl restart djangochannel',
         shell=True, pty=True, combine_stderr=True, user=None)