# Django bootstrapped server

Simple and minimal setup with vagrant, postgres & supervisor

## Easy to run
Just `vagrant up` and once it done head to `localhost:8000`

## What technologies was used to make it happen
- __Vagrant__ for creating and managing lightweight VirtualBox instances
- __Ansible__ as provisioning tool
- __Postgres__ as production ready database
- __Supervisor__ for process controlling and monitoring
- __Gunicorn__ as wsgi HTTP server
- __Django__ as python web-framework

## Toppings
- Opionated configs for OhMyZsh and Vim
- Flake8 and iPython for better developing experience
- Procfile and runtime.txt for Heroku deployment
- Nice Makefile with handy shortcuts

## Project structure

    .editorconf
    .gitignore
    Makefile
    Procfile
    Vagrantfile
    apps
    ├── __init__.py
    ├── urls.py
    └── views
        ├── __init__.py
        ├── index.py
    config
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    manage.py
    provision.yml
    requirements.txt
    runtime.txt
    setup.cfg
    setup.py
    tests
    ├── __init__.py
    └── conftest.py

