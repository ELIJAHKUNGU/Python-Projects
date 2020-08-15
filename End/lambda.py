#def double (x):
    #return x *2
#def add(x,y):
   # return x +y
#def product(x,y,z):
   #return x*y*z
from functools import reduce

#Now using the  lambda function
double = lambda x : x * 2
add = lambda x,y : x + y
product = lambda   x ,y ,z : x *y* z

print(double(5))
print(add(5,7))
print(product(5,67,90))

#filter ,reduce and map
mylist = [1,2,4,9,4,6,7]
mylist2 = [90,96,40,68,79]
a= map(lambda  x :x* 2, mylist)
print(list(a))

b= map(lambda  x  ,y  :x* y , mylist, mylist2)
print(list(b))
c= filter(lambda x : x%2 ==0 , mylist)
print(list(c))
d = filter(lambda  x : True if x> 2 else False, mylist)
print(list(d))

e = reduce(lambda x, y : x +y , mylist2)
print(e)