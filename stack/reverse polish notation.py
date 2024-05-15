def rpn(n):
    stack=[]
    for i in n.split():
        if i.isdigit() or (i[0]=='-' and i[1:].isdigit()):
            #i is an index but i[0] means nested index
            # ex: i=-123 then i[0]='-', i[1]='1',i[1:]=123
            stack.append(int(i))
            #print(stack)
        else:
            operand2=stack.pop()
            operand1=stack.pop()
            #print(operand2)
            #print(operand1)
            if(i=='+'):
                stack.append(operand1+operand2)
            if(i=='-'):
                stack.append(operand1-operand2)
            if (i == '*'):
                stack.append(operand1 * operand2)
            if (i == '/'):
                stack.append(int(operand1/operand2))
    return stack.pop()
n=input()
res=rpn(n)
print(res)