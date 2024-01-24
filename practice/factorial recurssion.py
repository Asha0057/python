
def factorial(n):
#    if(n==0 or n==1):
#       return 1
#    else:
#        return n * factorial(n-1)

#ternary opertation:

    return 1 if(n==0 or n==1) else n*factorial(n-1)
num=int(input("enter num:"))
print("factorial is:",factorial(num))