
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DeQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def add_front(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
            self.length += 1
            return
        
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node
        self.length += 1
    
    def add_rear(self, value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
            self.rear = new_node
            self.length += 1
            return
        
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
        self.length += 1
    
    def remove_front(self):
        
        if self.front == None:
            print("Queue is Already Empty")
            return
        
        deleted_data = self.front.data
        
        if self.front.next == None:
            self.front = None
            self.rear = None
            self.length -= 1
            return deleted_data
        
        temp = self.front
        self.front = self.front.next
        self.front.prev = None
        temp = None
        self.length -= 1
        return deleted_data
    
    def remove_rear(self):
        
        if self.front == None:
            print("Queue is Already Empty")
            return
        
        deleted_data = self.rear.data
        
        if self.front.next == None:
            self.front = None
            self.rear = None
            self.length -= 1
            return deleted_data
        
        temp = self.rear
        self.rear = self.rear.prev
        self.rear.next = None
        temp = None
        self.length -= 1
        return deleted_data

    def is_empty(self):
        return self.front == None
    
    def peek_front(self):
        
        if self.front == None:
            return
        
        return self.front.data
    
    def peek_rear(self):
        
        if self.front == None:
            return
        
        return self.rear.data

