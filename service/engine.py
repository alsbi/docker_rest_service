# -*- coding: utf-8 -*-
__author__ = 'alsbi'
import json

from dockerlib import BaseContainer, BaseService
from .logger import Loger


class Docker(BaseService):
    def __init__(self, version, transport, api, container):
        super(Docker, self).__init__(version = version, transport = transport, api = api, container = container)
        self.logger = Loger()

    def info(self):
        return self.api.info()

    def show_container_all(self):
        for container in self.api.show_container_all():
            yield self.container(self.api, data = json.dumps(container)).show()

    def show_container_active(self):
        for container in self.api.show_container_active():
            yield self.container(self.api, data = json.dumps(container)).show()

    def start_container(self, uid):
        return self.container(self.api, uid = uid).start()

    def create_container(self, data):
        return self.container(data).create()

    def stop_container(self, uid):
        return self.container(self.api, uid = uid).stop()

    def show_container(self, uid):
        return self.container(self.api, uid = uid).show()

    def get_log_container(self, uid):
        return self.container(self.api, uid = uid).show_log()

    def show_images(self):
        for images in self.api.show_images():
            yield images

    def show_images_history(self, images):
        return self.api.show_images_history(images)


class DockerContainer(BaseContainer):
    def __init__(self, api, uid=None, data=None):
        self.api = api
        self.uid = uid
        self.__parse(data)
        self.logger = Loger()

    def __parse(self, data=None):
        if data:
            self.json = data.strip()
            self.uid = json.loads(self.json)['Id']
        else:
            data = self.api.show_container(self.uid)
            for opt, value in data.iteritems():
                setattr(self, opt, value)
            self.json = json.dumps(data, indent = 4)

    def create(self):
        if self.uid is None:
            ret = self.api.create_container(self.json)
            self.uid = ret['Id']
        self.__parse()
        return self.uid

    def show(self):
        return self.api.show_container(self.uid)

    def show_stats(self):
        return self.api.show_container_opt(self.uid, action = 'stats')

    def show_log(self):

        return self.api.show_container_opt(self.uid, action = 'logs?stderr=1&stdout=1&tail=20')

    def show_top(self):
        return self.api.show_container_opt(self.uid, action = 'top')

    def start(self):
        return self.api.start_container(self.uid)

    def stop(self):
        return self.api.stop_container(self.uid)

    def delete(self):
        return self.api.delete_container(self.uid)

    def __repr__(self):
        return self.json

    def __atr(self):
        ret = {}
        for opt in dir(self):
            if not opt.startswith('_') and opt != 'json':
                obj = getattr(self, opt)
                if not callable(obj):
                    ret[opt] = obj
        return ret
