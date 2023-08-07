# derlivering the responsibility of one class to other becasue there is no is a and has a relation between them so we use
#  composition


class Salary:
    def __init__(self, pay, bonus) -> None:
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay*12 + self.bonus


class Employee:
    def __init__(self, name, age, pay, bonus) -> None:
        self.name = name
        self.age = age
        self.salary_obj = Salary(pay,bonus)

    def total_salary(self):
        return self.salary_obj.annual_salary()
    

emp = Employee("Khan", "24", 180000, 0)

print(emp.total_salary())