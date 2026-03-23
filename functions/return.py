'''
Return statement is used to exit a function and return a value to the caller. It can be used to return any type of data, including numbers, strings, lists, or even other functions. The return statement can also be used without a value to simply exit the function.
'''


def get_full_name(fname,lname):
    '''return a full name with neated format'''
    full_name=fname+' '+lname
    return full_name

full=get_full_name('Srikant','Panda')
print(full)

'''
Function name must be meaning full.
avoid global variables.
make a function short as much as you can but can be uderstandable by just seeing.
'''

'''
Local variable only built inside a function can't be access outside the function.
Global variable means it built outside the function and can be accesed in every where.
'''