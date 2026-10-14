employee = {
    "name": "Alex Morgan",
    "job_title": "Software Engineer",
    "monthly_salary": 6000,
}

annual_salary = employee["monthly_salary"] * 12

print(f"Employee: {employee['name']}")
print(f"Job title: {employee['job_title']}")
print(f"Annual salary: ${annual_salary:,.2f}")
