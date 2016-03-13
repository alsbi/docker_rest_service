# -*- coding: utf-8 -*-
__author__ = 'alsbi'

from functools import wraps

from .errors import *


# decorator
def get_error(func):
    @wraps(func)
    def work(self, *args, **kwargs):
        err, ret = func(self, *args, **kwargs)
        if err > 300:
            raise check_error(error = err)(error = err, message = ret)
        if ret:
            try:
                return json.loads(ret)
            except ValueError:
                return {'error': err, 'message': ret}
        else:
            return {'error': err, 'message': ret}

    return work


class Api(object):
    def __init__(self, transport):
        self.transport = transport

    @get_error
    def info(self):
        return self.transport.get('/info')

    @get_error
    def delete_images(self, images):
        return self.transport.delete('/images/{images}'.format(images = images))

    @get_error
    def show_images_history(self, images):
        return self.transport.get('/images/{images}/history'.format(images = images))

    @get_error
    def show_images(self):
        return self.transport.get('/images/json')

    @get_error
    def show_container_active(self):
        return self.transport.get('/containers/json')

    @get_error
    def show_container_all(self):
        return self.transport.get('/containers/json?all=1')

    @get_error
    def create_container(self, data):
        return self.transport.post('/containers/create', data = json.loads(data))

    @get_error
    def show_container(self, uid):
        return self.transport.get('/containers/{uid}/json'.format(uid = uid))

    @get_error
    def show_container_opt(self, uid, action=None):
        return self.transport.get('/containers/{uid}/{action}'.format(uid = uid, action = action))

    @get_error
    def delete_container(self, uid):
        return self.transport.delete('/containers/{uid}'.format(uid = uid))

    @get_error
    def start_container(self, uid):
        return self.transport.post('/containers/{uid}/start'.format(uid = uid))

    @get_error
    def restart_container(self, uid, ttl=5):
        return self.transport.post('/containers/{uid}/restart?t={ttl}'.format(uid = uid, ttl = ttl))

    @get_error
    def stop_container(self, uid):
        return self.transport.post('/containers/{uid}/stop'.format(uid = uid))

    @get_error
    def kill_container(self, uid):
        return self.transport.post('/containers/{uid}/kill'.format(uid = uid))
