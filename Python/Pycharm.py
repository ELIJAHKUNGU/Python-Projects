class Car:
    pass
ford=Car()
honda=Car()#object
audi=Car()


ford.speed =200#data
honda.speed= 220
audi.speed =250

ford.color ='red'
honda.color= 'Green'
audi.color ='Pale'

print(ford.speed)
print(ford.color)

ford.speed = 300
ford.color = 'Orange'


#to change the data in the method
print(ford.speed)
print(ford.color)
