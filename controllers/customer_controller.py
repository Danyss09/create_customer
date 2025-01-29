from utils.validation import validate_customer_data
from flask import Blueprint, request, jsonify
from models.customer_model import create_customer, get_all_customers
customer_bp = Blueprint('customer', __name__)
#  Route to creating a customer
@customer_bp.route('/create_customer', methods=['POST'])
def create_customer_route():
    data = request.json
    is_valid, message = validate_customer_data(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    response = create_customer(
        data['FirstName'],
        data['LastName'],
        data['Email'],
        data['PhoneNumber'],
        data['Address']
    )

    return jsonify(response)

#  Route to get all customers
@customer_bp.route('/get_customers', methods=['GET'])
def get_customers_route():
    response = get_all_customers()
    if "error" in response:
        return jsonify({"error": response["error"]}), 500
    return jsonify({"customers": response})
    