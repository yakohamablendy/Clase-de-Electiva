from flask import Flask, render_template_string
import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime

app = Flask(__name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'mysql',
    'database': 'hola_mundo_db',
    'user': 'usuario',
    'password': 'password123',
    'port': 3306
}

def get_db_connection():
    """Crear conexión a la base de datos MySQL"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error conectando a MySQL: {e}")
        return None

def init_database():
    """Inicializar la base de datos con tablas y datos de ejemplo"""
    try:
        connection = get_db_connection()
        if connection and connection.is_connected():
            cursor = connection.cursor()
            
            # Crear tabla mensajes si no existe
            create_table_query = """
            CREATE TABLE IF NOT EXISTS mensajes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                mensaje VARCHAR(255) NOT NULL,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_query)
            
            # Verificar si hay datos
            cursor.execute("SELECT COUNT(*) FROM mensajes")
            count = cursor.fetchone()[0]
            
            # Insertar datos de ejemplo si la tabla está vacía
            if count == 0:
                insert_query = """
                INSERT INTO mensajes (mensaje) VALUES 
                ('¡Hola Mundo desde Python + Flask!'),
                ('Aplicación creada con Docker Compose'),
                ('Python + Flask + MySQL funcionando correctamente'),
                ('¡Bienvenido a tu aplicación Python containerizada!')
                """
                cursor.execute(insert_query)
                connection.commit()
            
            cursor.close()
            connection.close()
            return True
            
    except Error as e:
        print(f"Error inicializando la base de datos: {e}")
        return False

@app.route('/')
def hello_world():
    """Página principal de la aplicación"""
    # Variables para la respuesta
    connection_status = "❌ Error de conexión"
    messages = []
    error_message = ""
    db_info = {}
    
    try:
        connection = get_db_connection()
        if connection and connection.is_connected():
            # Inicializar base de datos
            init_database()
            
            cursor = connection.cursor(dictionary=True)
            
            # Obtener información de la conexión
            cursor.execute("SELECT DATABASE() as db_name")
            db_info = cursor.fetchone()
            
            # Obtener mensajes
            cursor.execute("SELECT * FROM mensajes ORDER BY fecha_creacion DESC")
            messages = cursor.fetchall()
            
            connection_status = "✅ Conexión exitosa a MySQL"
            
            cursor.close()
            connection.close()
            
    except Error as e:
        error_message = str(e)
    
    # Template HTML
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola Mundo Python - Docker + MySQL</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            .success {
                color: #155724;
                background-color: #d4edda;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #c3e6cb;
                margin: 15px 0;
            }
            .error {
                color: #721c24;
                background-color: #f8d7da;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #f5c6cb;
                margin: 15px 0;
            }
            .mensaje {
                background: linear-gradient(45deg, #f8f9fa, #e9ecef);
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
                border-left: 4px solid #007bff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
                font-size: 2.5em;
            }
            .info {
                background: linear-gradient(45deg, #e3f2fd, #bbdefb);
                padding: 20px;
                border-radius: 8px;
                margin: 20px 0;
                border-left: 4px solid #2196f3;
            }
            .python-badge {
                background: linear-gradient(45deg, #3776ab, #ffd43b);
                color: white;
                padding: 10px 20px;
                border-radius: 20px;
                display: inline-block;
                margin: 10px 0;
                font-weight: bold;
            }
            .tech-stack {
                display: flex;
                justify-content: space-around;
                flex-wrap: wrap;
                margin: 20px 0;
            }
            .tech-item {
                background: #f8f9fa;
                padding: 10px 15px;
                border-radius: 10px;
                margin: 5px;
                border: 2px solid #dee2e6;
                text-align: center;
                min-width: 120px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🐍 Hola Mundo Python + Flask</h1>
            
            <div class="python-badge">
                🚀 Powered by Python {{ python_version }} & Flask
            </div>
            
            {% if connection_status.startswith('✅') %}
                <div class="success">
                    <strong>{{ connection_status }}</strong><br>
                    Base de datos: {{ db_info.db_name if db_info else 'hola_mundo_db' }}<br>
                    Host: mysql (Docker container)
                </div>
                
                <div class="info">
                    <h3>📋 Mensajes desde MySQL:</h3>
                    {% for mensaje in messages %}
                        <div class="mensaje">
                            <strong>{{ mensaje.mensaje }}</strong><br>
                            <small>🕒 Creado: {{ mensaje.fecha_creacion }}</small>
                        </div>
                    {% endfor %}
                </div>
                
            {% else %}
                <div class="error">
                    <strong>{{ connection_status }}</strong><br>
                    {% if error_message %}
                        Error: {{ error_message }}
                    {% endif %}
                </div>
            {% endif %}
            
            <div class="info">
                <h3>🛠️ Stack Tecnológico:</h3>
                <div class="tech-stack">
                    <div class="tech-item">
                        <strong>🐍 Python</strong><br>
                        {{ python_version }}
                    </div>
                    <div class="tech-item">
                        <strong>🌶️ Flask</strong><br>
                        {{ flask_version }}
                    </div>
                    <div class="tech-item">
                        <strong>🐬 MySQL</strong><br>
                        Connector
                    </div>
                    <div class="tech-item">
                        <strong>🐳 Docker</strong><br>
                        Compose
                    </div>
                </div>
            </div>
            
            <div class="info">
                <h3>ℹ️ Información del sistema:</h3>
                <ul>
                    <li><strong>Python Version:</strong> {{ python_version }}</li>
                    <li><strong>Flask Version:</strong> {{ flask_version }}</li>
                    <li><strong>Fecha actual:</strong> {{ current_time }}</li>
                    <li><strong>Puerto:</strong> 5000</li>
                </ul>
            </div>
            
            <div class="info">
                <p><strong>🐳 Esta aplicación está ejecutándose en Docker!</strong></p>
                <p>Servicios: Python/Flask + MySQL</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Obtener versiones
    import platform
    import flask
    
    return render_template_string(
        html_template,
        connection_status=connection_status,
        messages=messages,
        error_message=error_message,
        db_info=db_info,
        python_version=platform.python_version(),
        flask_version=flask.__version__,
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)