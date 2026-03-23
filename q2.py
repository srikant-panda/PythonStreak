# WAP to check prime or not
# import time

num = int(input("enter a num: "))

mid = num //2
# print(mid)
result = False
if num == 0:
    print(f"{num} is neither a prime nor not prime")
    exit()
if num == 1:
    result = True
else:
    for i in range(2,mid+1):
        if num%i == 0:
            result = False
            break
        else:
            result = True

if result:
    print('prime')
else:
    print('Not prime')
# result = False
# l = []
# for j in range(1,101):
#     num = j
#     # if num == 0:
#     #     print(f"{num} is neither a prime nor not prime")
#     #     # exit()
#     if num == 1:
#         result = True
#     else:
#         for i in range(2,num):
#             if num%i == 0:
#                 result = False
#                 break
#             else:
#                 result = True
#                 l.append(i)

# # if result:
# #     # print('prime')
# #     # l.append()
# # else:
# #     print('Not prime')

# print(l)