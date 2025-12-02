from bson.objectid import ObjectId


def get_all_employees(db):
    employees_collection = db["employees"]

    # Returns a list of employee docs
    employees = list(employees_collection.find({}))
    
    # Convert ObjectId to string for JSON output
    for emp in employees:
        emp["_id"] = str(emp["_id"])

    return employees