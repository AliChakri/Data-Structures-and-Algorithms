class MinHeap:
    def __init__(self):
        self.heap = []
    
    def get_parent_index(self, i): return (i - 1) // 2
    def get_left_child_index(self, i): return i * 2 + 1
    def get_right_child_index(self, i): return i * 2 + 2
    
    def push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)
    
    def bubble_up(self, index):
        parent = self.get_parent_index(index)
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.bubble_up(parent)
    
    def pop(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root
    
    def bubble_down(self, index):
        
        largest = index
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        
        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.bubble_down(largest)
        
    def build_min_heap(self, array):
        self.heap = array[:]
        
        for i in range((len(self.heap) // 2 - 1), -1, -1):
            self.bubble_down(i)

    def heapsort(self, array):
        
        self.build_min_heap(array)
        
        sorted_list = []
        
        while len(self.heap):
            sorted_list.insert(0, self.pop())
        
        return sorted_list

min_heap = MinHeap()

list = [99, 12, 35, 4, 9]

new = min_heap.heapsort(list)

print(new)