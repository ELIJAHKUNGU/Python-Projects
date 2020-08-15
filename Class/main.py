from triangle import  Triangle
from rectangle import Rectangle
from  Shape import Shape

rect = Rectangle()
tri = Triangle ()


rect.set_values(70 ,40 )
tri .set_values (50 ,40)
rect.set_color('Red')
tri.set_color('blue')

print(rect.area()," Area of Rectangle")
print(tri.area()," Area of Triangle")
print(rect.get_color())
print(tri.get_color())
