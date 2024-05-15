"""b = [" " for i in range(9)]
row1 = "|{}|{}|{}|".format(b[0], b[1], b[2])
row2 = "|{}|{}|{}|".format(b[3], b[4], b[5])
row3 = "|{}|{}|{}|".format(b[6], b[7], b[8])

print(row1)
print(row2)
print(row3)"""
b = [[0 for i in range(3)]for j in range(3)]
for i in b:
    for j in b:
        print(j, end="\t")
    print()

for i in range(9):
    pos = int(input('enter pos:'))
    ele = input('enter x or o:')
    row = pos // 3
    col = pos % 3
    if b[row][col] == 0:
        b[row][col] = ele
        print(b)
    else:
        print('pos alrdy taken')
    if (b[row][0] == b[row][1] == b[row][2] == ele) or \
            (b[0][col] == b[1][col] == b[2][col] == ele) or \
            (b[0][0] == b[1][1] == b[2][2] == ele) or \
            (b[0][2] == b[1][1] == b[2][0] == ele):
        print(f'Player {ele} wins!')
        break

