def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    config.add_route('test1', '/test1')
    config.add_route('test2', '/test2')
    config.add_route('test3', '/test3')

