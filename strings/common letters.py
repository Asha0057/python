n=input("enter string1:")
m=input("enter string2:")
s1=set(n) #removes duplicate alphabets
s2=set(m)
#print(s1)
#print(s2)
result=s1&s2
print("common letters are:",result)