#prime number contains only 2 factors
#eg:19 -> div by 1 and 19 only

n=int(input("enter number to check:"))
count=0
if (n>1):
    for i in range(1, n + 1):
        if (n % i == 0):
            count = count + 1
    if (count == 2):
        print("prime number")
    else:
        print("not a prime number")
