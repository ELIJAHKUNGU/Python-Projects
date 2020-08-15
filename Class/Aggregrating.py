class Salary :
    def __init__(self, pay,bonus):
        self.pay =pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12)+ self.bonus
class Emolyee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        #compostion (dedicating Obligation to other classes)
        self.obj_salary = salary


    def total_salary(self):
        return self.obj_salary.annual_salary()

salary =Salary( 40000, 80000)
emp = Emolyee('Elijah ' ,34,salary)
print(emp.total_salary())
