from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    #choose a templating language
    config.include('pyramid_mako')

    #Static assets
    config.add_static_view('static', 'static', cache_max_age=3600)

    #Routes
    config.add_route('root', '/')
    config.add_route('pass_index', '/passes')
    config.add_route('user_pass_index', '/user/{uid}/passes')


    #API endpoints
    config.add_route('api_pass_index', '/api/v1/passes.json')
    config.add_route('api_pass_by_id', '/api/v1/pass/{id}.json')

    config.add_route('api_user_by_id', '/api/v1/user/{uid}.json')
    config.add_route('api_user_pass_index', '/api/v1/user/{uid}/passes.json')

    config.scan()
    return config.make_wsgi_app()
