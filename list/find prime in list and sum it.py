a = []
b = []
n = int(input("how many?"))
for i in range(n):
    a.append(int(input()))
count = 0
for num in a:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            b.append(num)
print(count)
print(b)
tot=sum(b)
print(tot)

