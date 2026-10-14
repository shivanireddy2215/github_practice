employees = [
    {
        "name": "Alex Morgan",
        "job_title": "Software Engineer",
        "monthly_salary": 6000,
    },
    {
        "name": "Priya Sharma",
        "job_title": "Data Analyst",
        "monthly_salary": 5200,
    },
    {
        "name": "Daniel Lee",
        "job_title": "Project Manager",
        "monthly_salary": 7500,
    },
]

for employee in employees:
    annual_salary = employee["monthly_salary"] * 12

    print(f"Employee: {employee['name']}")
    print(f"Job title: {employee['job_title']}")
    print(f"Annual salary: ${annual_salary:}")
    print("-" * 20)