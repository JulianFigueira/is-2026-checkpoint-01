import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Traigo info de la BD desde variables de entorno
DB_URL = os.environ.get('DATABASE_URL')

# Funcion para conectarse con la BD
def conexion_bd():
    return psycopg2.connect(DB_URL)