try:
    int1 = input("enter a number: ")
    int2 = input('Enter another number: ')
    try:
        div = int(int1)/int(int2)
        print(f'Anser of {int1}/{int2} is : ',div)
    except ZeroDivisionError:
        print('Any number can\'t divided by zero.')
except ValueError:
    if type(int1) == str:
        print( 'int1 must be an intiger.')
    if type(int2) == str:
        print('int2  must be an integer.')
finally:
    print('Operation completed!')