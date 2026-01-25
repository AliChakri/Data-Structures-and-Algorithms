
from Queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None
    
    # Insert
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            return self.insert_node(self.root, value)
    
    def insert_node(self, current, value):
        
        if current.data == value:
            raise Exception("No Duplicates Values")
        
        if current.data > value:
            if current.left == None:
                current.left = Node(value)
            else:
                return self.insert_node(current.left, value)
        else:
            if current.right == None:
                current.right = Node(value)
            else:
                return self.insert_node(current.right, value)
    
    # ----- Delete -----
    
    def min_right(self, current):
        if current.left == None:
            return current.data
        else:
            return self.min_right(current.left)
    
    def max_left(self, current):
        if current.right == None:
            return current.data
        else:
            return self.max_left(current.right)
    
    def delete(self, value):
        self.root = self.delete_node(self.root, value)
    
    def delete_node(self, current, value):
        
        if current is None:
            return None
        
        if current.data > value:
            current.left = self.delete_node(current.left, value)
        elif current.data < value:
            current.right = self.delete_node(current.right, value)
        else:
            # Node has Only One Child
            if current.left == None:
                return current.right
            
            elif current.right == None:
                return current.left
            
            # Node Has Two Childs (Min of Right)
            min_val = self.min_right(current.right)
            current.data = min_val
            current.right = self.delete_node(current.right, min_val)
            
        return current

    # -----  Search  ----- 
    def search(self, value):
        if self.root is None:
            return False
        else:
            return self.search_node(self.root, value)
    
    def search_node(self, current, value):
        if current is None:
            return False
        elif current.data == value:
            return True
            
        elif current.data > value:
            return self.search_node(current.left, value)
        else:
            return self.search_node(current.right, value)
    
    # ----- Traversal Operations -----
    # PUBLIC FUCNTIONS
    def pre_traversal(self):
        if self.root == None:
            return
        else:
            self.pre_order_traversal(self.root)

    def traversal(self):
        if self.root == None:
            return
        else:
            self.in_order_traversal(self.root)

    def post_traversal(self):
        if self.root == None:
            return
        else:
            self.post_order_traversale(self.root)
    
    def pre_order_traversal(self, current):
        if current is None:
            return
        
        print(current.data)
        self.pre_order_traversal(current.left)
        self.pre_order_traversal(current.right)
    
    def in_order_traversal(self, current):
        if current is None:
            return
        
        self.in_order_traversal(current.left)
        print(current.data)
        self.in_order_traversal(current.right)
        
    def post_order_traversale(self, current):
        if current is None:
            return
        
        self.post_order_traversale(current.left)
        self.post_order_traversale(current.right)
        print(current.data)
    
    # Level-Order Traversal (BFS)
    def bfs(self):
        
        if self.root is None:
            print("Tree is empty")
            return
        
        queue = Queue()
        
        queue.add(self.root) 
        
        print("Level-Order:", end=" ")
        
        while not queue.is_empty():
            
            current = queue.remove_front()
            
            print(current.data, end=" ")
            
            if current.left:
                queue.add(current.left)
            if current.right:
                queue.add(current.right)
        print()
        
    # ----- Utility Operations -----
    
    # Minimum
    def min(self):
        if self.root == None:
            return None
        else:
            return self.find_min(self.root)
    
    def find_min(self, current):
        if current.left is None:
            return current.data
        return self.find_min(current.left)
    
    # Maximum
    def max(self):
        if self.root is None:
            return None
        else:
            return self.find_max(self.root)

    def find_max(self, current):
        if current.right == None:
            return current.data
        return self.find_max(current.right)
    
    # Height
    def height(self):
        if self.root is None:
            return -1
        return self.get_height(self.root)
    
    def get_height(self, current):
        if current is None:
            return -1
        
        left_node = self.get_height(current.left)
    
        right_node = self.get_height(current.right)
        
        return 1 + max(left_node, right_node)

    # Size
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.get_size(self.root)
    
    def get_size(self, current):
        if current is None:
            return 0
        else:
            return 1 + self.get_size(current.left) + self.get_size(current.right)
    
    def successor(self, target_val):
        current = self.root
        successor = None
        
        while current:
            if current.data > target_val:
                successor = current
                current = current.left
            elif current.data < target_val:
                current = current.right
            else:
                if current.right:
                    return self.find_min(current.right)
                break
        
        return successor.data if successor else None
    
    def predecessor(self, target_val):
        
        current = self.root
        pre_decessor = None
        
        while current:
            if current.data < target_val:
                pre_decessor = current
                current = current.right
            elif current.data > target_val:
                current = current.left
            else:
                if current.left:
                    return self.find_max(current.left)
                break
        
        return pre_decessor.data if pre_decessor else None

    def balance(self):
        
        nodes = []
        
        self.in_order_add(self.root, nodes)
        
        self.root = self.balace_tree(nodes)

    def balace_tree(self, nodes):
        
        if not nodes:
            return None
        
        mid = len(nodes) // 2
        
        new_node = Node(nodes[mid])
        
        new_node.left = self.balace_tree(nodes[:mid])
        new_node.right = self.balace_tree(nodes[mid+1:])
        
        return new_node

    # Is Valid
    def isvalid(self):
        nodes = []
        
        if self.root is None:
            return None
        
        self.in_order_add(self.root, nodes)
        
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i + 1]:
                return False
        
        return  True
    
    def in_order_add(self, current, nodes):
        if current:
            self.in_order_add(current.left, nodes)
            nodes.append(current.data)
            self.in_order_add(current.right, nodes)

