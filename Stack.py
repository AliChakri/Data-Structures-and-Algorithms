
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.length += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def pop(self):
        
        if self.head == None:
            print("Stack is Already Empty")
            return
        
        deleted_data = self.head.data
        
        if self.head.next == None:
            self.head = None
            self.length -= 1
            return deleted_data
        
        temp = self.head
        self.head = self.head.next
        temp = None
        self.length -= 1
        return deleted_data
    
    def peek(self):
        
        if self.head == None:
            return
        return self.head.data
    
    def is_empty(self):
        return self.head == None
    
    # Deleting immediately O(1)
    def clear(self):
        self.head = None
        # Set it to Zero
        self.size = 0

    def display(self):
        current = self.head
        while current:
            print(f"""|  {current.data}  |\n""")
            current = current.next
