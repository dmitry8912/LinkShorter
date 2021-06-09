from flask import current_app, g
from flask_redis import FlaskRedis


def next_id():
    return g.redis_client.incr('short_id')
