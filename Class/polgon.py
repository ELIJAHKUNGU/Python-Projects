

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

