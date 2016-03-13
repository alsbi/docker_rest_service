# -*- coding: utf-8 -*-
__author__ = 'alsbi'

import json

from flask import jsonify, Flask, request, render_template

from dockerlib import Transport, Api, template, ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict
from .engine import Docker, DockerContainer

APP = Flask(__name__, static_url_path = '/static')

# /v0.1/info
CurrentEngine = Docker(version = '0.1',
                       api = Api,
                       transport = Transport,
                       container = DockerContainer)


@APP.route('/')
def index():
    return render_template('index.html', info_js = "{version}_pager.js".format(version = CurrentEngine.version))


@APP.route(CurrentEngine.constract_route('/info'), methods = ['GET'])
def info():
    try:
        return jsonify(CurrentEngine.info())
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error


@APP.route(CurrentEngine.constract_route('/containers/json'), methods = ['GET'])
def containers():
    try:
        return json.dumps([container for container in CurrentEngine.show_container_all()], indent = 4)
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error


@APP.route(CurrentEngine.constract_route('/images/json'), methods = ['GET'])
def images():
    try:
        return json.dumps([img for img in CurrentEngine.show_images()])
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error


@APP.route(CurrentEngine.constract_route('/containers/create'), methods = ['POST'])
def containers_create():
    try:
        if request.method == 'POST':
            return jsonify(CurrentEngine.create_container(data = template(**json.loads(request.data))))
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error


@APP.route(CurrentEngine.constract_route('/containers/<uid>'), methods = ['GET'])
def containers_id(uid):
    try:
        return jsonify(CurrentEngine.show_container(uid))
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error


@APP.route(CurrentEngine.constract_route('/containers/<uid>/<action>'), methods = ['POST'])
def containers_action(uid, action):
    try:
        return jsonify(getattr(CurrentEngine, '{action}_container'.format(action = action))(uid = uid))
    except (ExecutionError, ApiError, BadParameter, NotRunning, NotFound, Conflict) as e:
        return str(e), e.error
    except AttributeError as e:
        return jsonify({'error': 500, 'message': 'Action "{action}" not found'.format(action = action)}), 500


def start():
    APP.run(debug = True,
            host = '0.0.0.0',
            threaded = True)
