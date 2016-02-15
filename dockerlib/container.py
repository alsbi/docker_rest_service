# -*- coding: utf-8 -*-
__author__ = 'alsbi'
from abc import ABCMeta, abstractmethod


class BaseContainer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def show_stats(self):
        pass

    @abstractmethod
    def show_log(self):
        pass

    @abstractmethod
    def show_top(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def delete(self):
        pass
