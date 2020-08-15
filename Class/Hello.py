#mulitple  inheritance


class Parent:
    def __init__(self,name):
        print('Parent __init__', name)
class Parent2:
    def __init__(self,name):
        print('Parent2 __init__', name)
class Child (Parent ,Parent2):
    def __init__(self):
         print('child__init__')
         super().__init__('MAX')
chid = Child()
print(Child.mro()) #Method resolution Order

