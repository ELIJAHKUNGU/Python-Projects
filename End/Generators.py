def my_function ():
    yield 'a'
    yield 'b'
    yield 'c'


x = my_function()
print(next(x))
print(next(x))
print(next(x))