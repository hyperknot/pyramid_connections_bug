import os

from .models import MyModel


def debug_dbsession(dbsession):
    pid = os.getpid()

    dbsession = dbsession
    connection = dbsession.connection()
    engine = connection.engine
    pool = engine.pool

    print('----- DBSession debug -----')
    print('PID:        {}'.format(pid))
    print('Engine:     {}'.format(id(engine)))
    print('Connection: {}'.format(id(connection)))
    print('DBSession:  {}'.format(id(dbsession)))
    print('Pool:       {}'.format(id(pool)))
    print(pool.status())
    print('---------------------------')



def get_siteconfig(dbsession):
    print('get_siteconfig')

    siteconfig = dbsession.query(MyModel).get(1)
    return dict(name=siteconfig.name)
