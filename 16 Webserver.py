from flask import Flask, jsonify, request
 
app = Flask(__name__)
"""
alumnos = [
            {'id':1, 'nombre':'Juan', 'cursos':5},
            {'id':2, 'nombre':'Josefa', 'cursos':2},
        ]
"""
alumnos = []
 
@app.route("/")
def home():
    return "HOME"
 
    
@app.route('/alumno', methods=['GET','POST','PUT','DELETE'])
def alumno():
    if request.method == "GET":
        return jsonify({"alumnos":alumnos})
    
    elif request.method == "POST":
        # calculo el id
        if not alumnos:
            codigo = 1
        else:
            codigo = alumnos[-1]['id'] + 1
        
        # añado el alumno
        alumno = {
                'id': codigo,
                'nombre': request.json['nombre'],
                'cursos':request.json['cursos']
            }
        alumnos.append(alumno)
        return jsonify("Alumno añadido")
        
    elif request.method == "PUT":
        id_alumno = request.json['id']
        for alumno in alumnos:
            if id_alumno == alumno.get('id'):
                if request.json['nombre'] is not None:
                    alumno['nombre'] = request.json['nombre']
                if request.json['cursos'] is not None:
                    alumno['cursos'] = request.json['cursos']
                return jsonify("Datos modificados")
        return jsonify(f"id {id_alumno} no hallado")
                
    elif request.method == "DELETE":
        id_alumno = request.json['id']
        for alumno in alumnos:
            if id_alumno == alumno.get('id'):
                alumnos.remove(alumno)
                return jsonify("Alumno borrado")
        return jsonify(f"id {id_alumno} no hallado")
                
@app.route("/alumno/<int:i>")
def get_alumno(i):
    try:
        return jsonify({"alumno":alumnos[i-1]})
    except IndexError:
        return jsonify(f"id {i} no hallado")
    
 
 
@app.route("/administrativos")
def admin():
    return "En construcción"
    
@app.route("/instructores")
def instructores():
    return "En construcción.... PROXIMAMENTE..."
 
if __name__ == "__main__":
    app.run(debug=True)
    
# Linux
# export FLASK_APP=webserver.py
# flask run
 
# WINDOWS
# set FLASK_APP=webserver.py
# python -m flask run