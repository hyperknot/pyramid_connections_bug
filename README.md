pyramid_connections_bug
=======================

```
cd pyramid_connections_bug
python3 -m venv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install -e ".[testing]"
dropdb pyramid_connections_bug -U pyramid_connections_bug --if-exists
dropuser pyramid_connections_bug --if-exists
createuser pyramid_connections_bug --createdb
createdb -O pyramid_connections_bug -U pyramid_connections_bug pyramid_connections_bug
env/bin/initialize_pyramid_connections_bug_db development.ini
env/bin/pserve development.ini --reload
```

monitor via **pg_top**

```
pg_top -d pyramid_connections_bug
```



One idle connection

http://localhost:6543/test1

http://localhost:6543/test2



Another "idle in transaction" connection

http://localhost:6543/test3



Two connections this time

http://localhost:6543/test2