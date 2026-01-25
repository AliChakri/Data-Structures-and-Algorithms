
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        # Increment size Auto
        self.size += 1
    
    def insert_at_end(self, data):
        
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            # Increment size Auto
            self.size += 1
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        # Increment size Auto
        self.size += 1

    def add(self, data, index=None):
        
        if index == None:
            self.insert_at_end(data)
            return
        
        new_node = Node(data)
        
        if index <= 0:
            raise Exception("Index Must Be Positive")
        if self.head == None:
            self.head = new_node
            # Increment size Auto
            self.size += 1
            return
            
        if index == 1:
            self.insert_at_beginning(data)
            new_node = None
            return
        else:
            i = 1
            before = self.head
            current = self.head
            while current.next and i < index:
                before = current
                current = current.next
                i += 1
            if i == index:
                before.next = new_node
                new_node.next = current
                # Increment size Auto
                self.size += 1
            else:
                raise Exception("Size Exceeded")

    def delete_at_beginning(self):
        temp = self.head
        self.head = self.head.next
        del temp
        # Decrement size Auto
        self.size -= 1

    def delete_at_end(self):
        
        if not self.head:
            return None
        
        if self.head.next == None:
            self.head = None
            # Decrement size Auto
            self.size -= 1
            return
        
        last = self.head
        before = self.head
        
        while last.next:
            before = last
            last = last.next
        before.next = None
        last = None
        # Decrement size Auto
        self.size -= 1

    def remove(self, index=None):
        
        if index == None:
            self.delete_at_end()
            return
        
        if index <= 0:
            raise Exception("Index Must Be Strictly Greater than One")
        if self.head == None:
            print('List Already Empty')
            return
        
        if self.head.next == None:
            self.deleteAll()
            return 
            
        if index == 1:
            self.delete_at_beginning()
            return
        else:
            i = 1
            before = self.head
            current = self.head
            while current.next and i < index:
                before = current
                current = current.next
                i += 1
            if i == index:
                before.next = current.next
                current = None
                # Decrement size Auto
                self.size -= 1
            else:
                raise Exception("Size Exceeded")

    # Looping through Elements O(n) 
    def clear(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp = None
        # Set it to Zero
        self.size = 0

    # Deleting immediately O(1)
    def deleteAll(self):
        self.head = None
        # Set it to Zero
        self.size = 0
        
    def search(self, value):
        if self.head == None:
            return False
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        
        return False
        
    # Reversing using Another LinkedList
    def reverse(self):
        newList = LinkedList()
        if self.head == None:
            print("List Empty")
            return
        last = self.head
        while last:
            newList.insert_at_beginning(last.data)
            last = last.next
        
        return newList
    
    # Reversing by Flipping Pointers next
    def flip(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
        
    def empty(self):
        return self.head == None

    # Looping through all Nodes O(n) Complexity
    def size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size
    
    # Looping through all Nodes O(n) Complexity
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("null")
