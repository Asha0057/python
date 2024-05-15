class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self):
        size=int(input("enter size"))
        for i in range(size):
            data=int(input("Enter data:"))
            newnode=Node(data)
            newnode.next=None
            if(self.head==None):
                self.head=newnode
                self.temp=newnode
            else:
                self.temp.next=newnode
                self.temp=newnode
    '''def reverse(self):
        k=int(input())
        c = 1
        s=self.head
        m=self.head.next
        curr = self.head
        while (c < k and curr.next != None):
            curr = curr.next
            c = c + 1
        curr.next = None
        c1=1
        while(c1!=k):
            self.head=s.next
            s.next=curr.next
            s=self.head
            c1=c1+1'''
    def reverse(self):
        k=int(input("enter k:"))
        prev=None
        current=self.head
        temp1=current
        temp2=current
        for i in range(k):
            temp1=current.next
            current.next=prev
            prev=current
            current=temp1
        temp2.next=temp1
        self.head=prev


    def display(self):
        self.temp = self.head
        while self.temp!= None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
obj=Linkedlist()
while True:
    print("enter choice 1:create 2:Display 3:reverse 4:exit")
    choice=int(input('enter:'))
    if(choice==1):
        obj.create()
    if(choice==2):
        obj.display()
    if(choice==3):
        obj.reverse()
    if(choice==4):
        break