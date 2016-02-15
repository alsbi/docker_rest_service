# -*- coding: utf-8 -*-
__author__ = 'alsbi'

import json
from functools import wraps

# decorator
def get_error(func):
    @wraps(func)
    def work(self, *args, **kwargs):
        err, ret = func(self, *args, **kwargs)
        # TODO error except
        # if err == 500 or err == 404:
        if err != 200:
            raise ValueError
        return json.loads(ret)

    return work


class Api(object):
    """
    :param transport:
    :return json
    """

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
    def show_container(self, id):
        return self.transport.get('/containers/{id}/json'.format(id = id))

    @get_error
    def show_container_opt(self, id, action=None):
        return self.transport.get('/containers/{id}/{action}'.format(id = id, action = action))

    @get_error
    def delete_container(self, id):
        return self.transport.delete('/containers/{id}'.format(id = id))

    @get_error
    def start_container(self, id):
        return self.transport.post('/containers/{id}/start'.format(id = id))

    @get_error
    def restart_container(self, id, ttl=5):
        return self.transport.post('/containers/{id}/restart?t={ttl}'.format(id = id, ttl = ttl))

    @get_error
    def stop_container(self, id):
        pass

    @get_error
    def kill_container(self, id):
        return self.transport.post('/containers/{id}/kill'.format(id = id))
