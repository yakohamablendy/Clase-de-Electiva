from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>¡Hola Mundo!</h1>
    <p>Esta es mi aplicación web para la práctica final de DevOps</p>
    
    '''

@app.route('/health')
def health():
    return {'status': 'OK', 'message': 'La aplicación está funcionando correctamente'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # Forzando la ejecución del pipeline con los secretos correctos