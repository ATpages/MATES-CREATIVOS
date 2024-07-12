from flask import Flask, render_template
from controller_db import conexionMySQL, resultados_cursos

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
"""
#Buscar Clases (adm)
@app.route("/buscar_clases")
def buscar_clases():
    cursos = resultados_cursos()
    #conexion = conexionMySQL()
    titulo = "Escuela de Ballet (L&A)"
    return render_template("buscar_clases.html",title=titulo, cursos=cursos)

#Ver Clases (adm)
@app.route("/ver_clases")
def ver_clases():
    cursos = resultados_cursos()
    #conexion = conexionMySQL()
    titulo = "Escuela de Ballet (L&A)"
    return render_template("ver_clases.html",title=titulo, cursos=cursos)"""