def employee_details(name, emp_id, salary):
    result = (
        f"Employee Name : {name}\n"
        f"Employee ID   : {emp_id}\n"
        f"Employee Salary : {salary}\n"
    )

    if salary < 20000:
        result += "Message: Salary is less than 20,000\n"
    else:
        result += "Message: Salary is acceptable\n"

    return result


if __name__ == "__main__":
    # Default values (for Jenkins & Docker)
    name = "Rahul"
    emp_id = "EMP101"
    salary = 18000

    print(employee_details(name, emp_id, salary))