class Polgon:
    __width = None#There are private due two underscore
    __height = None
    #method to set the values of the height and width

    def set_values(self, width ,height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height



class Rectangle(Polgon) :
    def area (self):
        return self.get_width() * self.get_height()
class Triangle(Polgon) :
    def area (self):
      return self.get_width() * self.get_height() /2


rect = Rectangle()
tri = Triangle () 

rect.set_values(70 ,40)
tri .set_values (50 ,40)

print(rect.area()," Area of Rectangle")
print(tri.area()," Area of Triangle")
