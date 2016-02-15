# -*- coding: utf-8 -*-
__author__ = 'alsbi'
import json


class ApiError(Exception):
    def __str__(self):
        return json.dumps({'error': self.error, 'message': self.message}, indent = 4)


class ExecutionError(ApiError):
    def __init__(self, error=None, message=None):
        super(ExecutionError, self).__init__(message)
        self.message = message
        self.error = error


class BadParameter(ApiError):
    def __init__(self, error=None, message=None):
        super(BadParameter, self).__init__(message)
        self.message = message
        self.error = error


class Conflict(ApiError):
    def __init__(self, error=None, message=None):
        super(Conflict, self).__init__(message)
        self.message = message
        self.error = error


class NotFound(ApiError):
    def __init__(self, error=None, message=None):
        super(NotFound, self).__init__(message)
        self.message = message
        self.error = error


class NotRunning(ApiError):
    def __init__(self, error=None, message=None):
        super(NotRunning, self).__init__(message)
        self.message = message
        self.error = error


def check_error(error):
    if error == 500:
        return ExecutionError
    elif error == 404:
        return NotFound
    elif error == 400:
        return BadParameter
    elif error == 409:
        return Conflict
    elif error == 304:
        return NotRunning
