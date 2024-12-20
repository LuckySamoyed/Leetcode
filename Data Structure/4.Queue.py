from collections import deque
# 1. 单向队列
class Queue:
    def __init__(self):
        """初始化一个空队列"""
        self.queue = deque()

    def enqueue(self, item):
        """将元素加入队尾"""
        self.queue.append(item)

    def dequeue(self):
        """从队头移除并返回元素；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()

    def peek(self):
        """返回队头元素但不移除它；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        """检查队列是否为空，返回布尔值"""
        return len(self.queue) == 0

    def size(self):
        """返回队列中元素的数量"""
        return len(self.queue)

# 2. 双向队列
class Deque:
    def __init__(self):
        """初始化一个空的双向队列"""
        self.deque = deque()

    def add_first(self, item):
        """将元素添加到队头"""
        self.deque.appendleft(item)

    def add_last(self, item):
        """将元素添加到队尾"""
        self.deque.append(item)

    def remove_first(self):
        """从队头移除并返回元素；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("remove_first from empty deque")
        return self.deque.popleft()

    def remove_last(self):
        """从队尾移除并返回元素；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("remove_last from empty deque")
        return self.deque.pop()

    def peek_first(self):
        """返回队头元素但不移除它；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("peek_first from empty deque")
        return self.deque[0]

    def peek_last(self):
        """返回队尾元素但不移除它；如果队列为空则抛出异常"""
        if self.is_empty():
            raise IndexError("peek_last from empty deque")
        return self.deque[-1]

    def is_empty(self):
        """检查双向队列是否为空，返回布尔值"""
        return len(self.deque) == 0

    def size(self):
        """返回双向队列中元素的数量"""
        return len(self.deque)