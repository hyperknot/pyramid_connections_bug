from pyramid.view import view_config
from ..models import MyModel


@view_config(route_name='test1', renderer='string')
def test1(request):
    one = request.dbsession.query(MyModel).get(1)
    return 'test1 ' + one.name


@view_config(route_name='test2', renderer='string')
def test2(request):
    one_name = get_one(request.dbsession)
    return 'test2 ' + one_name


@view_config(route_name='test3', renderer='string')
def test3(request):
    return 'test3'


@view_config(route_name='home', renderer='string')
def my_view(request):
    return '/'





def get_one(dbsession):
    print('get_one')

    one = dbsession.query(MyModel).get(1)
    return one.name
