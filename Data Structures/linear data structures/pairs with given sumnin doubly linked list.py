class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self,size):
        for i in range(size):
            data=int(input())
            newnode=Node(data)
            newnode.next=None
            if(self.head==None):
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next=newnode
                newnode.prev=self.tail
                self.tail=newnode
    def sums(self,size,s):
        temp=self.head
        while temp:
            temp2 = temp.next
            while temp2:
                if temp.data + temp2.data == s:
                    print('t:',temp.data,temp2.data)
                temp2 = temp2.next
            temp = temp.next
        #print(ans)
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()



obj=doubly()
while True:
    print("enter choice 1:create 2:Display 3:sum,4:exit")
    choice=int(input('enter:'))
    if(choice==1):
        size = int(input("size:"))
        obj.create(size)
    if(choice==2):
        obj.display()
    if(choice==3):
        s = int(input('s:'))
        obj.sums(s,size)
    if(choice==4):
        break