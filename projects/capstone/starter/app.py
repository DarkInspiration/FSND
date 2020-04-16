import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import Actor, Movie, setup_db, db_drop_and_create_all
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):

  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"*": {"origins": "*"}})

  '''
  After_request decorator to set Access-Control-Allow
  '''

  @app.after_request
  def after_request(response):
      response.headers.add(
          'Access-Control-Allow-Headers',
          'Content-Type, Authorization,true')
      response.headers.add(
          'Access-Control-Allow-Methods',
          'GET, PATCH, POST, DELETE, OPTIONS')
      return response


  ''' ACTORS ROUTES '''
  ''' GET all /actors'''

  @app.route('/actors', methods=['GET'])
  @requires_auth("get:actors")
  def get_actors(jwt):
      try:
        query = Actor.query.all()

        if not query:
            abort(404)

        return jsonify({
          'status': 200,
          'success': True,
          'actors': [i.format() for i in query],
          'total_actors': len(query)
        })
      except:
          abort(500)

  ''' POST /actors'''

  @app.route('/actors', methods=['POST'])
  @requires_auth("post:actor")
  def post_actors(jwt):
      try:
        body = request.get_json()
        if not body:
            abort(400)

        actor = Actor(name=body['name'], age=body['age'], gender=body['gender'])
        actor.insert()
        query = Actor.query.all()

        return jsonify({
          'status': 201,
          'success': True,
          'actor': actor.format(),
          'total_actors': len(query)
        })
      except:
          abort(400)

  ''' DELETE /actors'''

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth("delete:actor")
  def delete_actors(actor_id, jwt):
      try:
        actor = Actor.query.filter(
            Actor.id == actor_id).one_or_none()
            
        if actor_id is None:
            abort(404)
        else:
            actor.delete()
            query = Actor.query.all()

            return jsonify({
                'status': 200,
                'success': True,
                'deleted': actor_id,
                'total_questions': len(query)
            })
      except:
          abort(422)

  ''' PATCH /actors'''
  
  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth("patch:actors")
  def patch_actors(actor_id, jwt):
      try:
        actor = Actor.query.filter(
            Actor.id == actor_id).one_or_none()
        if actor_id is None:
            abort(404)
        else:
            body = request.get_json()
            if not body:
                abort(400)

            actor.name = body['name']
            actor.age = body['age']
            actor.gender = body['gender']
            actor.update()

            query = Actor.query.all()

            return jsonify({
                'status': 200,
                'success': True,
                'updated': actor.format(),
                'total_questions': len(query)
            })
      except:
          abort(422)

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)