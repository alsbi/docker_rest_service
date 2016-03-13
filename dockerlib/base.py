# -*- coding: utf-8 -*-
__author__ = 'alsbi'

from abc import ABCMeta, abstractmethod


class BaseService:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, version='0.1', transport=None, api=None, container=None):
        self.version = version
        self.container = container
        self.api = api(transport())

    def constract_route(self, route):
        return '/v{version}{route}'.format(version = self.version, route = route)

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def create_container(self, data):
        pass

    @abstractmethod
    def show_container_all(self):
        pass

    @abstractmethod
    def start_container(self, uid):
        pass

    @abstractmethod
    def stop_container(self, uid):
        pass

    @abstractmethod
    def show_container(self, uid):
        pass

    @abstractmethod
    def show_container_active(self):
        pass

    @abstractmethod
    def show_images(self):
        pass

    @abstractmethod
    def show_images_history(self, images):
        pass
