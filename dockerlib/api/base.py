# -*- coding: utf-8 -*-
__author__ = 'alsbi'
import json

from .utils import Api
from .container import Container


class Base(object):
    @staticmethod
    def info():
        return json.loads(Api.info())

    @staticmethod
    def show_container_all():
        for container in json.loads(Api.show_container_all()):
            yield Container(data = json.dumps(container))

    @staticmethod
    def show_container_active():
        for container in json.loads(Api.show_container_active()):
            yield Container(data = json.dumps(container))

    @staticmethod
    def show_images():
        for images in json.loads(Api.show_images()):
            yield images

    @staticmethod
    def show_images_history(images):
        return json.loads(Api.show_images_history(images))
