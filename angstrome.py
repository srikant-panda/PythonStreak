num = int(input(""))

sum = 0
for i in str(num):
    sum = int(i)**3 + sum

if int(sum) == num:
    print('It is a armstrong number.')
else:
    print('It is not a angstrome number.')