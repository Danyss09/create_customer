from flask import Flask
from controllers.customer_controller import customer_bp
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(customer_bp)

if __name__ == '__main__':
    # Opcional: Verificar que las variables de entorno están cargadas
    print("DB_HOST:", os.getenv("DB_HOST"))
    print("DB_PORT:", os.getenv("DB_PORT"))
    
    app.run(host='0.0.0.0', port=5000)
