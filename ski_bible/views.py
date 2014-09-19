from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Pass,
    Skier,
    )

#/api/v1/passes.json
@view_config(route_name='api_pass_index', renderer='json')
def api_pass_index(request):
    try:
        passes = DBSession.query(Pass).all()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if passes:
        passes_list = []
        for p in passes:
            i = {
            'id': p.id,
            'uid': p.uid,
            'speed': p.speed,
            'line': p.line,
            'count': p.count,
            'division': p.division,
            'date': str(p.date),
            'notes': p.notes,
            }
            passes_list.append(i)
        return {'passes': passes_list}
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'no passes found'}


#/api/v1/pass/{id}.json
@view_config(route_name='api_pass_by_id', renderer='json')
def api_pass_by_id(request):
    try:
        one = DBSession.query(Pass).filter_by(id=request.matchdict.get('id')).first()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if one:
        return one.as_dict()
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'id not found'}

#/api/v1/user/{uid}.json
@view_config(route_name='api_user_by_id', renderer='json')
def api_user_by_id(request):
    uid = request.matchdict.get('uid')
    try:
        skier = DBSession.query(Skier).filter_by(id=uid).first()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if skier:
        return skier.as_dict()
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'no skiers found by that id'}

#/api/v1/user/{uid}/passes.json
@view_config(route_name='api_user_pass_index', renderer='json')
def api_user_pass_index(request):
    uid = request.matchdict.get('uid')
    try:
        passes = DBSession.query(Pass).filter_by(uid=uid).all()
        skier = DBSession.query(Skier).filter_by(id=uid).first()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if passes and skier:
        passes_list = []
        skier_dict = skier.as_dict()
        for p in passes: passes_list.append(p.as_dict())
        skier_dict['passes'] = passes_list
        return skier_dict
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'no passes found for that skier id'}

#/
@view_config(route_name='root', renderer='templates/root.mako')
def root(request):
    return {'project': "Dan's Ski Bible"}

#/passes
@view_config(route_name='pass_index', renderer='templates/pass_index.mako')
def pass_index(request):
    try:
        passes = DBSession.query(Pass).all()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if passes:
        passes_list = []
        for p in passes:
            i = {
            'id': p.id,
            'uid': p.uid,
            'speed': p.speed,
            'line': p.line,
            'count': p.count,
            'division': p.division,
            'date': str(p.date),
            }
            passes_list.append(i)
        return {'passes': passes_list}
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'no passes found'}

#/user/{uid}/passes
@view_config(route_name='user_pass_index', renderer='templates/pass_index.mako')
def user_pass_index(request):
    uid = request.matchdict.get('uid')
    try:
        passes = DBSession.query(Pass).filter_by(uid=uid).all()
    except DBAPIError:
        request.response.status = 500
        return {'error': 500, 'msg': 'internal server error'}
    if passes:
        passes_list = []
        for p in passes:
            i = {
            'id': p.id,
            'uid': p.uid,
            'speed': p.speed,
            'line': p.line,
            'count': p.count,
            'division': p.division,
            'date': str(p.date),
            }
            passes_list.append(i)
        return {'passes': passes_list}
    else:
        request.response.status = 404
        return {'error': 404, 'msg': 'no passes found'}