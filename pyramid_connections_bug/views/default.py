from pyramid.view import view_config

from ..models import MyModel
from ..sql import get_siteconfig, debug_dbsession


@view_config(route_name='test', renderer='string')
def test(request):
    siteconfig1 = request.siteconfig
    siteconfig2 = request.dbsession.query(MyModel).get(1)
    debug_dbsession(request.dbsession)
    return 'test ' + siteconfig1['name']


@view_config(route_name='test1', renderer='string')
def test1(request):
    siteconfig = request.dbsession.query(MyModel).get(1)
    debug_dbsession(request.dbsession)
    return 'test1 ' + siteconfig.name


@view_config(route_name='test2', renderer='string')
def test2(request):
    siteconfig = get_siteconfig(request.dbsession)
    debug_dbsession(request.dbsession)
    return 'test2 ' + siteconfig['name']


@view_config(route_name='test3', renderer='string')
def test3(request):
    siteconfig = request.siteconfig
    debug_dbsession(request.dbsession)
    return 'test3 ' + siteconfig['name']


@view_config(route_name='home', renderer='string')
def my_view(request):
    return 'views are: /test /test1 /test2 /test3'

