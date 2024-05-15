s="pbbcggttciiippooaais"
print(len(s))
k=3
a = []
for i in s:
    if (len(a) > 0) and (a[-k+1:] == i):
        a.pop()

    else:
        a.append(i)
n = ''.join(a)
print(n)
print(len(n))