departments = [
    {"department_id": 1, "department_name": "IT"},
    {"department_id": 2, "department_name": "HR"},
    {"department_id": 3, "department_name": "Finance"},
]

employees = [
    {"employee_id": 101, "name": "Ava Patel", "department_id": 1},
    {"employee_id": 102, "name": "Noah Kim", "department_id": 2},
    {"employee_id": 103, "name": "Mia Chen", "department_id": 1},
    {"employee_id": 104, "name": "Ethan Jones", "department_id": 3},
]

print("DEPARTMENTS")
print(f"{'ID':<5} Department")
for department in departments:
    print(f"{department['department_id']:<5} {department['department_name']}")

print("\nEMPLOYEES")
print(f"{'ID':<5} {'Name':<15} Department ID")
for employee in employees:
    print(
        f"{employee['employee_id']:<5} "
        f"{employee['name']:<15} "
        f"{employee['department_id']}"
    )

it_department_ids = {
    department["department_id"]
    for department in departments
    if department["department_name"] == "IT"
}
it_employees = [
    employee
    for employee in employees
    if employee["department_id"] in it_department_ids
]

print("\nEmployees in the IT team:")
for employee in it_employees:
    print(f"- {employee['name']}")