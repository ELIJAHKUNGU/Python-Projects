def my_function (list):
    for i in list:
        yield i

a = [1,2,3,4,5,6]

mylist = my_function(a)
for x  in mylist:
    print(x)


#similiar to iterate but is smaller

