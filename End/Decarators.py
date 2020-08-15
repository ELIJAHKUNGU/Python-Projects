def decorator_function(func):
    def wrapper_fun():
        print('X'*20)
        func()
        print('Y'*20)
    return wrapper_fun
@decorator_function
def say_hello():
    print("Hello world")


#hello = decorator_function(say_hello)
#hello()
say_hello()