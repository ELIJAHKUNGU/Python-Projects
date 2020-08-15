from polgon  import Polgon
from  Shape import Shape


class Rectangle(Polgon, Shape) :
    def area (self):
        return self.get_width() * self.get_height()