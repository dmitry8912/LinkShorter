import functools

from flask import (
    Blueprint, g, current_app, redirect, request, jsonify
)
from flask_redis import FlaskRedis
from hashids import Hashids
from linkShorter.redisimpl import next_id

bp = Blueprint('auth', __name__, url_prefix='/api')


@bp.route('/addLink', methods=['POST'])
def add_link():
    next_link_id = Hashids().encode(g.redis_client.client_id(), next_id())
    g.redis_client.set(next_link_id, request.json['link'])
    return jsonify({
        "short_id": next_link_id
    })


redirect_bp = Blueprint('redirect', __name__, url_prefix='/')


@redirect_bp.route('/<link>', methods=['GET'])
def get_link(link):
    return redirect(g.redis_client.get(link), 302)


@bp.before_app_request
def connect_redis():
    if 'redis_client' not in g:
        g.redis_client = FlaskRedis(current_app)
    pass
