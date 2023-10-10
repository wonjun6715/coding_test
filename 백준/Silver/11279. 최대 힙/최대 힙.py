import sys

class Heap:
    def __init__(self):
        self.heap = []
        self.heap.append(None)
        self.flag = 0
        
    def check_swap_up(self, idx):
        if idx <= 1:
            return False
        
        parent_idx = idx // 2
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        return False
    
    def insert(self, data):
        self.heap.append(data)
        idx = len(self.heap) - 1
        
        while self.check_swap_up(idx):
            parent_idx = idx // 2
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        return True
    
    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        
        if left_idx >= len(self.heap):
            return False
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
        else:
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1
                    return True
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2
                    return True
        return False
                    
    def pop(self):
        if len(self.heap) <= 1:
            return None
        
        max_val = self.heap[1]
        
        self.heap[1] = self.heap[-1]
        del self.heap[-1]
        
        self.flag = 0
        idx = 1
        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1
            
            if self.flag == 1:
                self.heap[left_idx], self.heap[idx] = self.heap[idx], self.heap[left_idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[right_idx], self.heap[idx] = self.heap[idx], self.heap[right_idx]
                idx = right_idx
        return max_val

if __name__ == '__main__':
    max_heap = Heap()
    input = sys.stdin.readline
    
    N = int(input())
    
    for _ in range(N):
        x = int(input())
        if x == 0:
            max_element = max_heap.pop()
            if max_element is not None:
                print(max_element)
            else:
                print(0)
        else:
            max_heap.insert(x)