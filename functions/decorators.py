'''
Decorator are give the ability to modify a function without changing the funcion code
'''

'''______Decorator defing___________'''

'''___________first define the decorator__________'''

def my_decorator(func):
    def wrapper():
        print('Before decorator')
        func()
        print("after decorator")
    return wrapper 

@my_decorator
def say_hello():
    print("Hello")

say_hello()
say_hello()
