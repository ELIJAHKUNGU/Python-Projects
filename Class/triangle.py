from polgon import Polgon
from  Shape import Shape


class Triangle(Polgon, Shape):
    def area(self):
        return self.get_width() * self.get_height() / 2
