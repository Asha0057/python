flag=0
b = [['-' for i in range(3)]for j in range(3)]
for row in b:
    for element in row:
        print(element, end="\t")
    print()

for i in range(9):
    pos = int(input('enter pos:'))#eg:pos = 5
    ele = input('enter x or o:')#ele = x
    row_id = pos // 3   #calculates the row eg:[1]
    col_id = pos % 3    #calculates the col eg:[2]
                        #then b[r][c] = b[1][2] =>5th pos (on 5th pos x is printed)
    if b[row_id][col_id] == '-':
        b[row_id][col_id] = ele
        for row in b:
            for element in row:
                print(element.upper(), end="\t")
            print()
    else:
        print('pos alrdy taken')
    if (b[row_id][0] == b[row_id][1] == b[row_id][2] == ele) or \
            (b[0][col_id] == b[1][col_id] == b[2][col_id] == ele) or \
            (b[0][0] == b[1][1] == b[2][2] == ele) or \
            (b[0][2] == b[1][1] == b[2][0] == ele):
        print(f'Player {ele.upper()} wins!')
        flag=1
        break
if(flag!=1):
    print('The Match is draw')
