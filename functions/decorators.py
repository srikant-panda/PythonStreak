import time,datetime


'''
Decorator are give the ability to modify a function without changing the funcion code
'''

'''______Decorator defing___________'''

'''___________first define the decorator__________'''

def my_decorator(func):
    def wrapper(*args,**kargs):
        start_time = time.time() 
        func(*args,**kargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f'It takes {total_time} to comple this program.')
        print(datetime.datetime.now())
        # print(f'completed at {date}')
    return wrapper 

@my_decorator
def say_hello(hello):
    print("Hello")

say_hello('hello')
# say_hello()
