import heapq
# 1. 小顶堆，python默认实现的是小顶堆
class MinHeap:
    def __init__(self):
        """初始化一个空的最小堆"""
        self.heap = heapq.heapify([])   # 列表转化成堆

    def push(self, item):
        """将元素压入堆中"""
        heapq.heappush(self.heap, item)

    def pop(self):
        """弹出并返回堆中的最小元素；如果堆为空则抛出异常"""
        if self.is_empty():
            raise IndexError("pop from empty heap")
        return heapq.heappop(self.heap)

    def peek(self):
        """返回堆顶元素但不移除它；如果堆为空则抛出异常"""
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def is_empty(self):
        """检查堆是否为空，返回布尔值"""
        return len(self.heap) == 0

    def size(self):
        """返回堆中元素的数量"""
        return len(self.heap)

# 2. 大顶堆，通过取负值实现，压入和取数时都取个负号
class MaxHeap:
    def __init__(self):
        """初始化一个空的最大堆"""
        self.heap = []

    def push(self, item):
        """将元素压入堆中（取负值）"""
        heapq.heappush(self.heap, -item)

    def pop(self):
        """弹出并返回堆中的最大元素；如果堆为空则抛出异常（取正值）"""
        if self.is_empty():
            raise IndexError("pop from empty max heap")
        return -heapq.heappop(self.heap)

    def peek(self):
        """返回堆顶元素但不移除它；如果堆为空则抛出异常（取正值）"""
        if self.is_empty():
            raise IndexError("peek from empty max heap")
        return -self.heap[0]

    def is_empty(self):
        """检查堆是否为空，返回布尔值"""
        return len(self.heap) == 0

    def size(self):
        """返回堆中元素的数量"""
        return len(self.heap)