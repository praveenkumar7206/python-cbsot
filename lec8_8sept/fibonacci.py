print("hello",end=" ")
print("world")
# if we want to print in same line use end command
n= int(input("enter ur number for fibonaccci series"))

#1 methods
# a = 0
# b = 1
# c= 0
# for i in range(2,n+1):
#     i = a+b
#     c= i
#     a=b
#     b=c
#     print(i)

#2 method

a = 0
b = 1
c= 0
for i in range(n+1):
    i = a+b
    c= i
    print(a,end=" ")
    a=b
    b=c

# 3rd method do using while loop
