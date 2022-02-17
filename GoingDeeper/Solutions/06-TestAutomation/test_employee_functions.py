from company import Employee


def test_pay_raise():
    # Arrange
    emp = Employee("Person", 12000)
    # Act
    emp.payRaise(5000)
    # Assert
    assert emp._salary == 17000


def test_minimum_salary_overrides_lowball():
    # Arrange/Act
    emp = Employee("Person", 10000)
    # Assert
    assert emp._salary == 12000


def test_minimum_salary_can_be_changed():
    Employee.setMinimumSalary(10000)
    emp = Employee("Person", 10000)
    assert emp._salary == 10000
    Employee.setMinimumSalary(12000)
