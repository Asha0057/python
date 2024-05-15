class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doubly:
    def __init__(self):
        self.head=None
        self.tail=None
    def create(self):
        size=int(input())
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
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.next
        print()
    def rev(self):
        temp=self.tail
        while(temp!=None):
            print(temp.data,end=' ')
            temp=temp.prev
        print()
    def insertfront(self):
        newnode=Node(int(input('enter :')))
        if(self.head==None):
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def insertend(self):
        newnode = Node(int(input('Enter data to insert:')))
        if(self.tail==None):
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode
    def search(self):
        s = int(input("enter elemant to search:"))
        self.temp = self.head
        i=0
        while (self.temp!=None):
            i=i+1
            if (self.temp.data == s):
                print(s, " is prestent at position:",i)
                return
            self.temp = self.temp.next
        print(s, " not found")
    def delbeg(self):
        temp=self.head
        self.head=self.head.next
        del temp
    def delend(self):
        temp=self.head
        while(temp!=None):
            temp=temp.next
        del temp





obj=doubly()
obj.create()
obj.display()
obj.rev()
obj.insertfront()
obj.display()
obj.insertend()
obj.display()
obj.search()
obj.display()
obj.delbeg()
obj.display()