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

  ''' ACTORS ROUTES '''
  ''' GET all /actors'''
  @app.route('/actors', methods=['GET'])
  def get_actors():
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
  def post_actors():
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
  def delete_actors(actor_id):
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

  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)