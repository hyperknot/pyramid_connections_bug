pyramid_connections_bug
=======================

Getting Started
---------------

- Change directory into your newly created project.

    cd pyramid_connections_bug

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Configure the database.


    dropdb pyramid_connections_bug -U pyramid_connections_bug --if-exists
    dropuser pyramid_connections_bug --if-exists
    createuser pyramid_connections_bug --createdb
    createdb -O pyramid_connections_bug -U pyramid_connections_bug pyramid_connections_bug
    
    env/bin/initialize_pyramid_connections_bug_db development.ini

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini


    monitor via **pg_top**

    `pg_top -d pyramid_connections_bug`

- ​