import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Actor, Movie, setup_db, db_drop_and_create_all


def create_app(test_config=None):

  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"*": {"origins": "*"}})

  @app.route('/actors', methods=['GET'])
  def index():
        query = Actor.query.all()

        return jsonify({
          'status': 200,
          'success': True,
          'actors': [i.format() for i in query]
        })

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)