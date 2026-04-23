import os
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Esto habilita que el frontend (puerto 3000) pueda consultar al backend (puerto 4000)

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
        cur.execute("SELECT nombre, apellido, legajo, feature, servicio, estado FROM members;")
        rows = cur.fetchall()
        
        # Mapeo de los resultados a un formato de lista de diccionarios
        # Esto asegura que el frontend reciba objetos con nombres de campos claros
        members = []
        for row in rows:
            members.append({
                "nombre": row[0],
                "apellido": row[1],
                "legajo": row[2],
                "feature": row[3],
                "servicio": row[4],
                "estado": row[5]
            })
        
        # 3. Cierre de la conexión
        cur.close()
        conn.close()
        
        # 4. Respuesta (Devolvemos la lista directamente para que coincida con el fetch del front)
        return jsonify(members), 200
    except Exception as e:
        print(f"Error en la base de datos: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/info', methods=['GET'])
def get_info():
    metadata = {
        "service": "backend-con-flask",
        "version": "1.0.0",
        "python_version": "3.12"
    }
    return jsonify(metadata), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)