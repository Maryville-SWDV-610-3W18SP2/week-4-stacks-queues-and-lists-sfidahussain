from node import *

# Implement a queue using linked lists
class Queue:
    def __init__(self):
        self.length = 0
        self.front = None
        self.rear = None
        
    def enqueue(self, item):
        self.length += 1
        # set node with the new item
        n = Node(item)
        n.next = None
        # if there is no items
        if self.rear == None:
            self.front = n
            self.rear = n
        else:
            # sets new node after rear
            self.rear.next = n
            # moves rear to new node
            self.rear = n 
    
    def dequeue(self):
        if self.front == None:
            print('Cannot delete from an empty queue.')
        else:
            # store front data to return later
            n = self.front.data
            # moving front one node ahead
            self.front = self.front.next
            self.length -= 1
            return n
        
    def isEmpty(self):
        return self.front == None
    
    def size(self):
        return self.length
    
def main():
    q = Queue()
    
# Queue Testing
    print()
    print('QUEUE TESTING')
    print(q.isEmpty()) # True
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size()) # 3
    print(q.isEmpty()) # False
    q.enqueue(8.4) 
    print(q.dequeue()) # 4
    print(q.dequeue()) # dog
    print(q.size()) # 2

main()


