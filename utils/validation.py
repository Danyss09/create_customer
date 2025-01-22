def validate_customer_data(data):
    required_fields = ['FirstName', 'LastName', 'Email', 'PhoneNumber', 'Address']
    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Field '{field}' is required."
    return True, "Validation successful."
