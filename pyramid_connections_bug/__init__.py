from pyramid.config import Configurator
from .views.default import get_siteconfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.models')
    config.include('.routes')

    dbsession = config.registry['dbsession_factory']()

    siteconfig = get_siteconfig(dbsession)
    dbsession.rollback()

    # example reason for using siteconfig here
    # if not siteconfig['logout_on_close']:
    #     settings['redis.sessions.cookie_max_age'] = 123

    # bug is here
    # using dbsession creates an additional DB connection,
    # which will be 'idle in connection forever'

    # changing it to x.dbsession solves it
    config.add_request_method(lambda x: get_siteconfig(dbsession), 'siteconfig', reify=True)

    config.scan()
    return config.make_wsgi_app()
