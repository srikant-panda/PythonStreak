

n = int(input("Enter the length of fibonacii series : "))
a, b =0,1

# for i in range(n+1):
#     if i == 0:
#         print(0,end=' ')
#         continue

#     if i ==1 :
#         print(1,end=' ')
#         continue

#     a,b = b,a+b
#     print(b,end=' ')

for i in range(n+1):
    print(a,end=' ')
    a,b = b,a+b