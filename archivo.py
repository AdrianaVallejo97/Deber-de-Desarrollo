#importar librerias
from flask import Flask, Request, jsonify
from flask_cors import CORS, cross_origin
#configurar el proyecto 
#declarar una variable 
apli= Flask (__name__)
cors= CORS(apli)
apli.config["CORS_HEADERS"]= "Content-Type"

#metodo de  la llamada 
@apli.route("/api/")
def indice_contenidos():
    return "buenas noches 6:31"

# Ruta 1: Devolver un HOME
@apli.route("/api/home")
def obtener_home():
    contenido = "HOME"
    return (contenido)

# Ruta 2: APRUEBO
@apli.route("/api/apruebo")
def obtener_apruebo():
    contenido = "APRUEBO"
    return contenido

# Ruta 3: Devolver COMPROBADO
@apli.route("/api/comprobado")
def obtener_comprobado():
    contenido="COMPROBADO"
    return (contenido)

if __name__ == "__main__":
    apli.run(debug=True,port=8000)
