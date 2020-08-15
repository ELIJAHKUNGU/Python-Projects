from time import time

def timing(func):
    def wrapper_func(*args,**kwargs):
        start = time()
        result = func (*args , **kwargs)
        end =time()
        print('Elapsed time : {}'.format(end - start))
        return result
    return wrapper_func

@timing
# def divide(x, y):
#     return  x / y
# print(divide(15,0))

def my_fun(num):
    sum = 0
    for i in range(num+1):
        sum +=i
    return sum
print(my_fun(20000000))