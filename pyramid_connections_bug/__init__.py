import os

from pyramid.config import Configurator
from transaction import TransactionManager

from .views.default import get_siteconfig


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


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')

    tm = TransactionManager(explicit=True)
    with tm:
        dbsession = config.registry['dbsession_factory']()
        siteconfig = get_siteconfig(dbsession)

    debug_dbsession(dbsession)



    # example reason for using siteconfig here
    # if not siteconfig['logout_on_close']:
    #     settings['redis.sessions.cookie_max_age'] = 123

    # bug is here
    # using dbsession creates an additional DB connection,
    # which will be 'idle in connection forever'

    # changing it to x.dbsession solves it
    config.add_request_method(lambda r: get_siteconfig(r.dbsession), 'siteconfig', reify=True)

    config.scan()
    return config.make_wsgi_app()
