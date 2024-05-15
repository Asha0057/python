class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def probing(self, arr, size):
        table = [None] * size
        for key in arr:
            index = (2 * key + 3) % size
            if table[index] is None:
                table[index] = Node(key)
            else:
                curr = self.head
                c = 0
                while curr.next is not None:
                    index = ((2 * key) + 3 % size) * c
                    if table[index] is None:
                        table[index] = Node(key)
                    else:
                        c = c + 1
                        curr = curr.next
                curr.next = Node(key)
        for i in table:
            curr = i
            while curr is not None:
                print(curr.key, end=' -> ')
                curr = curr.next
            print("None")

obj = LinkedList()
size = 10
arr = [12, 13, 11, 10, 2, 1]
obj.probing(arr, size)
