class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
class CoffeeTooColdException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class cofee :
    def __init__(self ,temparature):
        self.__temperature =temparature

    def drink_cofee (self):
        if self.__temperature >86:
            #print("The cofee is too hot")
            raise Exception('COFFEE TOO HOT: ' +str(self.__temperature))
        elif self.__temperature <69:
            raise ValueError('COFFEE TOO COLD', + str(self.__temperature))
            #print("The coffee is too cold")
        else:
            print("Drink") 
cup = cofee(101)
cup.drink_cofee()