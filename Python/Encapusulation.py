class Car :
    def __init__(self,speed,color):
        self.__speed = speed #To make it private 
        self.__color = color


        
    def set_speed(self,value):
        self.__speed = value
        
    def get_speed(self):
        return self.__speed


    
    def set_color(self,value):
          self.color = value
            
    def get_color(self):
        return self.__color

ford = Car(200 , 'Red')
Honda = Car (250 ,'Blue')
Audi = Car (700 , "Orange")


ford.set_speed(300)
ford.set_color("Pale")
 

print(ford.get_speed())
print(ford.get_color())
