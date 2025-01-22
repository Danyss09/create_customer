from flask import Flask
from controllers.customer_controller import customer_bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(customer_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
