import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Traigo info de la BD desde variables de entorno
DB_URL = os.environ.get('DATABASE_URL')

# Funcion para conectarse con la BD
def conexion_bd():
    return psycopg2.connect(DB_URL)

@app.route('/api/health', methods=['GET'])
def healthcheck():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/team', methods=['GET'])
def traer_equipo():
    try:
        # 1. Conexión con la BD
        conn = conexion_bd()
        cur = conn.cursor()
        
        # 2. Ejecución de la consulta
        cur.execute("SELECT * FROM members;")
        rows = cur.fetchall()
        
        # 3. Cierre de la conexión
        cur.close()
        conn.close()
        
        # 4. Respuesta
        return jsonify({"members": rows}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
