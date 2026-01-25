class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def insert_at_start(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def insert_at_end(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def add(self, value, index=None):
        
        if index == None:
            self.insert_at_end(value)
            return
        
        if index <= 0:
            raise Exception("Index Must Be Strictely Greater Than Zero")
        elif index == 1:
            self.insert_at_start(value)
            return
        
        new_node = Node(value)
        i = 1
        current = self.head
        while current and i < index:
            current = current.next
            i += 1
        if i == index:
            current.prev.next = new_node
            new_node.prev = current.prev
            new_node.next = current
            current.prev = new_node
            self.length += 1
            return
        else:
            raise Exception("Out of Bounds")
    
    def delete_at_start(self):
        
        if self.head == None:
            print("List Already Empty")
            return

        if self.head.next == None:
            self.clear()
            return
        
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        temp = None
        self.length -= 1
        
    def delete_at_end(self):
        
        if self.head == None:
            print("List Already Empty")
            return
        if self.head.next == None:
            self.clear()
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
    
    def remove(self, index=None):
        
        if index == None:
            self.delete_at_end()
            return
        
        if self.head.next == None:
            self.clear()
            return
        
        if index <= 0:
            raise Exception("Index Must Be Strictely Greater Than Zero")
        elif index == 1:
            self.delete_at_start()
            return
        elif index == self.length:
            self.delete_at_end()
            return
        
        i = 1
        current = self.head
        while current.next and i < index:
            current = current.next
            i += 1
        if i == index:
            current.prev.next = current.next
            current.next.prev = current.prev
            current = None
            self.length -= 1
            return
        else:
            raise Exception("Out of Bounds")
    
    def reverse(self):
        
        current = self.head
        temp = None

        while current:
            
            # Switch between Pointer next and prev
            temp = current.prev
            current.prev = current.next
            current.next = temp
            
            current = current.prev
        
        if temp:
            self.tail = self.head
            self.head = temp.prev
    
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def forward_traverse(self):
        current = self.head
        print(f"Doubly LinkedList Length {self.length} Forward Display: ")
        while current:
            print("<- " ,current.data, end=" -> ")
            current = current.next
        print("null")
        
    def backward_traverse(self):
        last = self.tail
        print(f"Doubly LinkedList Length {self.length} Backward Display: ")
        while last:
            print("<- ", last.data, end=" -> ")
            last = last.prev
        print("null")
        
# TEST Code
head = DoublyLinkedList()
