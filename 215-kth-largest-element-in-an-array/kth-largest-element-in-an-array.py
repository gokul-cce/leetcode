class Solution:
    def bubble_down(self,heap,index):
        while index < len(heap):
            left = (index*2)+1
            right = (index*2)+2
            smallest = index

            if left < len(heap) and heap[left] < heap[smallest]:
                smallest = left
            if right < len(heap) and heap[right] < heap[smallest]:
                smallest = right
            
            if index == smallest:
                break
            heap[index],heap[smallest] = heap[smallest],heap[index]
            index = smallest

    def remove(self,heap):
        heap[0],heap[-1] = heap[-1],heap[0]
        heap.pop()
        self.bubble_down(heap,0)
        
    def insert(self,heap,index,k):
        parent = (index-1) // 2
        while index > 0 and heap[parent] > heap[index]:
            heap[parent],heap[index] = heap[index],heap[parent]
            index = parent
            parent = (index-1) // 2

    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heap.append(nums[i])
            self.insert(heap,len(heap)-1,k)
            if len(heap) > k:
                self.remove(heap)
        return heap[0]

            

        