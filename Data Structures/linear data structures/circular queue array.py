maxz=5
rear=front=-1
queue=[0]*5
def insert():
    global rear,front
    if((rear+1)%maxz==front):
        print('queue full: overflow')

    elif(front==-1 and rear==-1):
        front=rear=0
        num=int(input('enter data:'))
        queue[rear]=num

    else:
        #r+=1 kuduka kudathu because circular la 5 ku aprm 0th pos ku ponum.indha cond padi 5 ku aprm 5 ku poirum so
        rear=(rear+1)%maxz
        num=int(input('enter data:'))
        queue[rear]=num
def delete():
    global front,rear
    if(front==-1 and rear==-1):
        print('queue empty: underflow')
    elif(front==0 and rear==0):#or front==rear:
        print(queue[front],'is deleted')
        front=rear=-1
    else:
        print('the deleted element is',queue[front])
        front+=1  #delete from front
def peek():
    global front, rear
    if (front == -1 and rear == -1):
        print('queue empty: underflow')
    else:
        print('the peek elemenet is:',queue[front])

def display():
    i=0
    if(front==-1 and rear==-1):
        print('underflow')
    else:
        while(i!=rear):
            print(queue[i],end=' ')
            i=(i+1)%maxz
        print(queue[i])

print('choice 1:insert,2:delete,3:peek,4:display,5:exit')
while(1):
    ch = int(input('enter ch:'))
    if(ch==1):
        insert()
    if(ch==2):
        delete()
    if(ch==3):
        peek()
    if(ch==4):
        display()
    if(ch==5):
        break

