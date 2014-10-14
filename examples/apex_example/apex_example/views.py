from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/index.pt')
def index(request):
    return {}

@view_config(route_name='test', renderer='templates/test.pt')
def test(request):
    return {}

@view_config(route_name='protected', renderer='templates/protected.pt',
             permission='authenticated')
def protected(request):
    return {}

@view_config(route_name='groupusers', renderer='templates/groupusers.pt',
             permission='users')
def groupusers(request):
    return {}
