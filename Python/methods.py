class Method:
     def __init__(self ,name):
         self.a =10
         self._b = 20
         self.__c = 30
     def public_method(self):
         print(self.a)
         print(self.__c)
         print("Public")
         self.__private_method()   
     def __private_method(self):
         print('private')


hello = Method ('Name')
print(hello.a)
print(hello._b)
print.public_method()
#because it is private cannot be accessed
hello.__private_method()
