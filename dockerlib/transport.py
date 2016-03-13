# -*- coding: utf-8 -*-
__author__ = 'alsbi'

import requests_unixsocket


class Transport(object):
    def __init__(self, server_address='/var/run/docker.sock'):
        self.server_address = server_address
        self.session = requests_unixsocket.Session()

    def get(self, command):
        path = 'http+unix://{sock}{command}'.format(sock = self.server_address.replace('/', '%2F'), command = command)
        r = self.session.get(path)
        return r.status_code, str(r.text.encode('utf8'))

    def post(self, command, data=None):
        headers = {'Content-type': 'application/json'}
        path = 'http+unix://{sock}{command}'.format(sock = self.server_address.replace('/', '%2F'), command = command)
        r = self.session.post(path, json = data, headers = headers)
        return r.status_code, str(r.text.encode('utf8'))

    def delete(self, command):
        path = 'http+unix://{sock}{command}'.format(sock = self.server_address.replace('/', '%2F'), command = command)
        r = self.session.delete(path)
        return r.status_code, str(r.text.encode('utf8'))
