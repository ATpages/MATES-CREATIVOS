from flask import Flask, render_template, request, redirect
from controller_db import *

app = Flask(__name__)

#Inicio
@app.route("/")
def index():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("index.html",title=titulo)

#Sobre Nosotros
@app.route("/sobre_nosotros")
def sobre_nosotros():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("sobre_nosotros.html",title=titulo)

#Nuestras Clases
@app.route("/nuestras_clases")
def nuestras_clases():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("nuestras_clases.html",title=titulo)

#Inscribite
@app.route("/inscripcion")
def inscripcion():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("inscripcion.html",title=titulo)

#Unite al Staff
@app.route("/sumate_al_staff")
def sumate_al_staff():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("sumate_al_staff.html",title=titulo)

#Contacto
@app.route("/contacto")
def contacto():
    titulo = "Escuela de Ballet (L&A)"
    return render_template("contacto.html",title=titulo)

#Ver Clases (adm)
@app.route("/ver_datos")
def ver_datos():
    cursos = resultados_cursos()
    #conexion = conexionMySQL()
    titulo = "Escuela de Ballet (L&A)"
    return render_template("ver_datos.html",title=titulo, cursos=cursos)

#Cargar Datos (adm)
@app.route("/inscripcion")
def cargar_datos():
    cursos = resultados_cursos()
    #conexion = conexionMySQL()
    titulo = "Escuela de Ballet (L&A)"
    return render_template("inscripcion.html",title=titulo, cursos=cursos)

#Envío de Datos (adm)
@app.route("/inscripcion/guardar_nuevos_datos", methods =["POST"])
def nueva_carga_de_datos():
    #print(request.form)
    nombre_alumno = request.form["nombre"]
    apellido_alumno = request.form["apellido"]
    telefono = request.form["telefono"]
    email = request.form["email"]
    clase = request.form["clase"]
    cargar_nuevos_datos(nombre_alumno, apellido_alumno, telefono, email, clase)
    return redirect("/inscripcion")

#Update
@app.route("/ver_datos/editar_datos/<int:id_alumno>")
def editar_datos(id_alumno):
    title = "Editar Datos"
    dato_por_id = obtener_dato_por_id(id_alumno)
    return render_template("edicion_de_datos.html", title=title, datos=dato_por_id)
    
    