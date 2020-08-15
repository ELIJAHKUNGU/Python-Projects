class Car:
   def __init__(self,speed,color):
       print(speed)
       print(color)
       print("The self method is called")
       self.speed = speed
       self.color = color



       
ford=Car(200,"Red")
honda=Car(90," Blue")#object
audi=Car(900, " Orange")

print(ford.color)
print(ford.speed)



 
