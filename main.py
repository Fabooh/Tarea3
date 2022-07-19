from flask import Flask, jsonify, request
from flask_cors import CORS
from config import config
from models import db, Personas


def create_app(enviroment):
	app = Flask(__name__)
	app.config['JSON_AS_ASCII'] = False
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app


# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)
CORS(app)

#/ / /#

#CRUD API SIMPLE
#===============================================================================#
@app.route('/api/personas', methods=['GET'])
def get_persona():
    personas = [user.json() for user in Personas.query.all()]
    response = jsonify(personas)
    return response
#===============================================================================#


#===============================================================================#
@app.route('/api/personas', methods=['POST'])
def put_persona():
    json = request.get_json()
    persona = Personas.create(json['username'])
    response = jsonify(persona.json())
    return response
#===============================================================================#



#===============================================================================#
@app.route('/api/personas/<id>', methods=['PUT'])
def editar_persona(id):
    json = request.get_json()
    persona = Personas.query.filter_by(id=id).first()
    persona.nombre = json['nombre']
    persona.update()
    return jsonify(persona.json())
#===============================================================================#



#===============================================================================#
@app.route('/api/personas/<id>', methods=['DELETE'])
def delete_persona(id):
    persona = Personas.query.filter_by(id=id).first()
    persona.delete()
    return jsonify({'mensaje':'Usuario borrado'})
#===============================================================================#


if __name__ == '__main__':
	app.run(debug=True)



