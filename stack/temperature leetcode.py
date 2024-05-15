t=[89,62,70,58,47,47,46,76,100,70]
stack = []
result = [0] * len(t)
for i in range(len(t)):
    while stack and t[i] > t[stack[-1]]:
        prev_index = stack.pop()
        result[prev_index] = i - prev_index

    stack.append(i)

print(result)
