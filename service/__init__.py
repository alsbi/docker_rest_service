# -*- coding: utf-8 -*-
__author__ = 'alsbi'
import json

from flask import jsonify, Flask

from dockerlib import Transport, Api
from .engine import Base, Container

app = Flask(__name__)

CurrentBase = Base(version = '0.1', transport = Transport, api = Api, container = Container)

print(CurrentBase.constract_route('/containers/json'))

@app.route('/')
@app.route(CurrentBase.constract_route('/info'))
def info():
    return jsonify(CurrentBase.info())


@app.route(CurrentBase.constract_route('/containers/json'))
def containers():
    return json.dumps([i for i in CurrentBase.show_container_all()])


@app.route(CurrentBase.constract_route('/images/json'))
def images():
    return json.dumps([i for i in CurrentBase.show_images()])


@app.route(CurrentBase.constract_route('/containers/<id>'))
def containers_id(id):
    return jsonify(CurrentBase.show_container(id))


@app.route(CurrentBase.constract_route('/containers/<id>/<action>'))
def containers_action(id, action):
    return getattr(CurrentBase, '{action}_container'.format(action = action))(id)


def start():
    app.run(debug = True,
            host = '0.0.0.0',
            threaded = True)
