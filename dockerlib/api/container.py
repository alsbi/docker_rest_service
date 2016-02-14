# -*- coding: utf-8 -*-
__author__ = 'alsbi'
import json

from utils import Api


class Container(object):
    def __init__(self, uid=None, data=None):
        self.uid = uid
        self.__parse(data)

    def __parse(self, data=None):
        if data:
            self.json = data.strip()
        else:
            for opt, value in json.loads(Api.show_container(self.uid)).iteritems():
                setattr(self, opt, value)
            self.json = json.dumps(self.__atr(), indent = 4)

    def create(self):
        if self.uid is None:
            ret = json.loads(Api.create_container(self.json))
            self.uid = ret['Id']
        self.__parse()
        return self.uid

    def show(self):
        return Api.show_container(self.uid)

    def show_stats(self):
        return Api.show_container_opt(self.uid, action = 'stats')

    def show_log(self):
        return Api.show_container_opt(self.uid, action = 'log')

    def show_top(self):
        return Api.show_container_opt(self.uid, action = 'top')

    def start(self):
        return Api.start_container(self.uid)

    def stop(self):
        return Api.stop_container(self.uid)

    def delete(self):
        pass

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
