import os

from flask import Flask, abort, redirect, render_template, url_for, jsonify

def create_app(test_config=None):
  app = Flask(__name__)

  @app.route('/api/homeline')
  def index():
    return jsonify( ["test", "json"] )
