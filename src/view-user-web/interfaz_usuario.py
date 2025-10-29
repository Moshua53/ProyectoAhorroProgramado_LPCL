from flask import Blueprint, render_template, request

blueprint = Blueprint( "interfaz_usuario", __name__, "templates")

import sys
sys.path.append("src")
from model.usuarios import Usuario
import Controller.usuarios_controller as usuarios_controller

@blueprint.route("/")
def Home():
    return render_template("index.html")

@blueprint.route( "/nuevo" )
def nuevo():
    return render_template("nuevo_usuario.html")

@blueprint.route( "/crear" )
def creat():
    usuario = Usuario( cedula=request.args["cedula"], 
                       nombre=request.args["nombre"],
                       apellido=request.args["apellido"], 
                       correo=request.args["correo"],)
    usuarios_controller.insertar( usuario )

    return render_template("usuario.html", user = usuario, mensaje = "Usuario insertado exitosamente! ")

@blueprint.route("/buscar")
def buscar():
    cedula = request.args["cedula"]
    usuario = usuarios_controller.buscar_por_cedula( cedula )
    return render_template( "usuario.html", user = usuario )