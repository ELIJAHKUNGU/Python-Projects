class Listiterator:
    def __init__(self, list):
        self.__list = list
        self.index = index = -1

    def __iter__(self):
         return self
    def __next__(self):
         self.index += 1
         if self.index == len(self.__list):
             raise StopIteration
         return self.__list[self.index]


a = [1,2,3,4,6,7,8,9,0]
mylist = Listiterator(a)
it = iter (mylist)

for i in  it:
    print(i)