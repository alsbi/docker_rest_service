# -*- coding: utf-8 -*-
__author__ = 'alsbi'

from flask import Flask, jsonify

from dockerlib import Base

tmpl_dir = ''
app = Flask(__name__)


@app.route('/')
@app.route('/info')
def info():
    return jsonify(Base.info())


@app.route('/containers/json')
def containers():
    return jsonify(Base.show_container_all())


@app.route('/containers/<id>')
def containers_id(id):
    return jsonify(Base.show_container(id))


@app.route('/containers/<id>/<action>')
def containers_action(id, action):
    return getattr(Base, '{action}_container'.format(action = action))(id)


def start():
    app.run(debug = True,
            host = '0.0.0.0',
            threaded = True)
