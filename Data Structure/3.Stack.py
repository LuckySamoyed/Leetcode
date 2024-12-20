from collections import deque
# 使用 deque 实现栈
stack = deque()

# 1. push(x) 入栈
x = 1
stack.append(x)
# 2. pop() 出栈
stack.pop()
# 3. peek() 取栈顶元素
stack[-1]
# 4. is_empty() 判断是否为空
len(stack) == 0
# 5. size() 取大小
len(stack)

class Stack:
    def __init__(self):
        """初始化一个空栈"""
        self.stack = deque()

    def push(self, x):
        """将元素压入栈顶"""
        self.stack.append(x)

    def pop(self):
        """弹出栈顶元素并返回它；如果栈为空则抛出异常"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self.stack.pop()

    def peek(self):
        """返回栈顶元素但不移除它；如果栈为空则抛出异常"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        """检查栈是否为空，返回布尔值"""
        return len(self.stack) == 0

    def size(self):
        """返回栈中元素的数量"""
        return len(self.stack)