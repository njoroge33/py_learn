# Create a class called Employee that includes three instance variables — a first name (type String),
# a last name (type String) and a monthly salary (double)
# Provide a constructor that initializes the three instance variables
# Provide a set and a get method for each instance variable
# If the monthly salary is not positive, set its value to 0
# Round off salary value to two decimal places
# for more info on this quiz, go to this url: http://www.programmr.com/employee-class-2


class Employee:
    def __init__(self, first_name, last_name, monthly_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.monthly_salary = float(monthly_salary)

    @property
    def fullname(self):
        return f'{self.first_name}' + ' '+ f'{self.last_name}'

    @property
    def salary(self):
        if self.monthly_salary > 0:
            return self.monthly_salary
        else:
            return 0

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @salary.setter
    def salary(self, amount):
        monthly_salary = amount
        self.monthly_salary = float(round(monthly_salary, 2))


emp_1 = Employee('john', 'njoroge', '4000')

emp_1.fullname = 'mark kamau'
emp_1.salary = 5000.986


print(emp_1.fullname)
print(emp_1.salary)
