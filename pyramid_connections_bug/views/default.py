from pyramid.view import view_config
from ..models import MyModel


@view_config(route_name='test1', renderer='string')
def test1(request):
    siteconfig = request.dbsession.query(MyModel).get(1)
    return 'test1 ' + siteconfig.name


@view_config(route_name='test2', renderer='string')
def test2(request):
    siteconfig = get_siteconfig(request.dbsession)
    return 'test2 ' + siteconfig['name']


@view_config(route_name='test3', renderer='string')
def test3(request):
    siteconfig = request.siteconfig
    return 'test3 ' + siteconfig['name']


@view_config(route_name='home', renderer='string')
def my_view(request):
    return '/'




def get_siteconfig(dbsession):
    print('get_siteconfig')

    siteconfig = dbsession.query(MyModel).get(1)
    return dict(name=siteconfig.name)
