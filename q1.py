# WAP a programm to find the sum of a digit 

num = input("Enter a number : ")
Resut = 0

# while num>0:
#     # Resut = int(i)+int(Resut)
#     Resut = Resut+ num % 10
#     # print(Resut)
#     num//=10
#     # print(num)

# print(Resut)

l = [int(i) for i in num]
print(sum(l))