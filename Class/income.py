#compostion

class Salary :
    def __init__(self, pay,bonus):
        self.pay =pay
        self.bonus = bonus
    def annual_salary(self):
        return (self.pay*12)+ self.bonus
class Emolyee:
    def __init__(self,name,age,pay ,bonus):
        self.name = name
        self.age = age
        #compostion (dedicating Obligation to other classes)
        self.obj_salary = Salary(pay, bonus)


    def total_salary(self):
        return self.obj_salary.annual_salary()
emp = Emolyee('Elijah ' ,34, 40000, 80000)
print(emp.total_salary())
