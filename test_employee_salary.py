from employee_salary import employee_details

def test_salary_below_20000():
    output = employee_details("Rahul", "EMP101", 18000)
    assert "Salary is less than 20,000" in output

def test_salary_above_20000():
    output = employee_details("Amit", "EMP102", 25000)
    assert "Salary is acceptable" in output 