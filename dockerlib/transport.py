# -*- coding: utf-8 -*-
__author__ = 'alsbi'

import requests_unixsocket

path = 'socket'
session = requests_unixsocket.Session()
server_address = '/var/run/docker.sock'


class Transport(object):
    @staticmethod
    def get(command):
        path = 'http+unix://{sock}{command}'.format(sock = server_address.replace('/', '%2F'), command = command)
        r = session.get(path)
        return r.status_code, r.text

    @staticmethod
    def post(command, data=None):
        headers = {'Content-type': 'application/json'}
        path = 'http+unix://{sock}{command}'.format(sock = server_address.replace('/', '%2F'), command = command)
        r = session.post(path, json = data, headers = headers)
        return r.status_code, r.text

    @staticmethod
    def delete(command):
        path = 'http+unix://{sock}{command}'.format(sock = server_address.replace('/', '%2F'), command = command)
        r = session.delete(path)
        return r.status_code, r.text
