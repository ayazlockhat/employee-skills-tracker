from flask import Blueprint

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['GET'])
def get_employees():
    employees = [
        {"name": "John Doe", "department": "IT", "skills": ["Python", "JavaScript", "SQL"]},
        {"name": "Jane Smith", "department": "HR", "skills": ["HR", "Management", "Leadership"]},
        {"name": "Jim Beam", "department": "Finance", "skills": ["Accounting", "Financial Analysis", "Taxation"]},
    ]
    return {"Status": "OK", "employees": employees}, 200