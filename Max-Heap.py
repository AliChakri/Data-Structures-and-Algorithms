class MaxHeap:
    
    def __init__(self):
        self.heap = []
    
    def get_parent_index(self, i): return (i - 1) // 2
    def get_left_child_index(self, i): return i * 2 + 1
    def get_right_child_index(self, i): return i * 2 + 2
    
    def push(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent = self.get_parent_index(index)
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)
    
    def pop(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self.heapify_down(0)
        return root
    
    def heapify_down(self, index):
        largest = index
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)
        
    def build_heap(self, array):
        self.heap = array[:]
        for i in range((len(self.heap) // 2 - 1), -1, -1):
            self.heapify_down(i)
        
    def heapsort(self, array):
        
        # Turing random array into Heap
        self.build_heap(array)
        
        sorted_array = []
        
        while len(self.heap) > 0:
            # Ascending Order
            sorted_array.insert(0, self.pop())
        
        return sorted_array
        
