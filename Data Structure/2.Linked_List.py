# python 中没有内置的链表结构，需要自己定义

# 1.单向链表（Singly Linked List）
#   首先定义一个节点类
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    # 初始化
    def __init__(self):
        self.head = Node()  # 头结点是虚拟节点
        self.length = 0

    # 获取指定index位置的数
    def get(self, index):
        # 判断下标为否有效
        if index < 0 or index >= self.length:
            return False
        search = self.head.next
        # 注意这里从next开始才是第0个，head相当于虚拟节点，后面函数里的search是从head开始，
        # 因为后面要找index下标的前一个节点，这里找的是index下标的节点
        for i in range(index):
            search = search.next
        return search.val

    # 在头部添加节点
    def addAtHead(self, val):
        new_node = Node(val=val, next=self.head.next)
        self.head.next = new_node
        self.length += 1

    # 在尾部添加节点
    def addAtTail(self, val):
        search = self.head
        while search.next != None:
            search = search.next
        search.next = Node(val=val)
        self.length += 1

    # 在index位置添加节点
    def addAtIndex(self, val, index):
        # 判断index是否有效
        if index < 0 or index > self.length:
            return False

        # 首先找到index前一个节点
        search = self.head
        for i in range(index):
            search = search.next
        # 先抓一下下一个节点
        next_node = search.next
        # 调整顺序
        search.next = Node(val=val, next=next_node)
        self.length += 1

    # 删除头部节点
    def deleteAtHead(self):
        # 判断是否有数
        if self.length == 0:
            return False

        # 抓一下新的头部节点
        new_head = self.head.next.next
        self.head.next = new_head
        self.length -= 1

    # 删除尾部节点
    def deleteAtTail(self):
        # 判断是否有数
        if self.length == 0:
            return False

        # 抓一下尾结点的前一个节点
        search = self.head
        while search.next.next != None:
            search = search.next
        '''两个循环都可
        for _ in range(self.length - 1):
            search = search.next
        '''
        # 此时search就是尾结点的前一个节点
        search.next = None
        self.length -= 1

    # 删除指定index位置的结点
    def deleteAtIndex(self, index):
        # 判断index是否有效
        if index < 0 or index >= self.length:
            return False
        # 抓一下index前一个节点
        search = self.head
        for _ in range(index):
            search = search.next
        # 抓一下index后一个节点
        new_next = search.next.next
        search.next = new_next
        self.length -= 1

    # 获取链表长度
    def get_len(self):
        return self.length

    # 打印链表
    def print_linklist(self):
        search = self.head
        for _ in range(self.length):
            search = search.next
            print(search.val,end="->" if search.next else '\n')

# 2. 双向链表
# 首先定义节点类
class Node_d:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    # 初始化
    def __init__(self):
        self.head = Node_d()    # 头结点是虚拟节点
        self.length = 0

    # 获取指定index位置的数
    def get(self, index):
        # 判断index 是否有效
        if index < 0 or index >= self.length:
            return False

        search = self.head.next
        for _ in range(index):
            search = search.next
        return search.val

    # 在头部添加节点
    def addAtHead(self, val):
        # 抓一下原来头部节点
        head = self.head.next   # 原头部节点
        new_head = Node_d(val=val,next=head,prev=self.head)     # 新节点，后指针指向原头结点，前指针指向虚拟节点
        head.prev = new_head    # 原节点的前指针
        self.head.next = new_head   # 虚拟节点的后指针
        self.length += 1

    # 在尾部添加节点
    def addAtTail(self, val):
        # 抓最后一个节点
        search = self.head
        while search.next != None:
            search = search.next
        # 此时search是最后一个节点，next指向None
        new_node =Node_d(val=val,next=None,prev=search)
        search.next = new_node
        self.length += 1

    # 在index位置添加节点
    def addAtIndex(self, val, index):
        # 判断index是否有效
        if index < 0 or index > self.length:    # =length相当于在最后添加
            return False
        # 还是抓index位置前一个节点，因为有可能是在最后尾部插入，不方便操作
        search = self.head
        for _ in range(index):
            search = search.next
        # 此时search是index前一个节点

        new_node = Node_d(val=val, next=search.next, prev=search)   # 新节点前指针指向search，后指针指向search.next
        search.next = new_node  # index -1 的后指针指向新节点
        if search.next.next:    # 如果 index后面有节点，就把那个节点的前指针指向新的节点
            search.next.next.prev = new_node
        self.length += 1

    # 删除头部节点
    def deleteAtHead(self):
        # 判断是否有数
        if self.length == 0:
            return False
        # 抓一下新的头部节点
        new_head = self.head.next.next
        self.head.next = new_head   # 虚拟节点的next 指向新的头结点
        if self.head.next.next:     # 如果不是None，要把他的前指针指向虚拟节点
            new_head.prev = self.head
        self.length -= 1

    # 删除尾部节点
    def deleteAtTail(self):
        # 判断是否有数
        if self.length == 0:
            return False
        # 抓一下原来的尾部节点
        search = self.head
        for _ in range(self.length):
            search = search.next
        new_tail = search.prev      # 新尾部节点为原尾部节点的前一个
        new_tail.next = None        # 新尾部的next指向None
        search.prev = None          # 断掉原尾部的prev指针
        self.length -= 1

    # 删除指定index位置的结点
    def deleteAtIndex(self, index):
        # 判断index是否有效
        if index < 0 or index >= self.length:
            return False
        # 抓取index前一个的结点
        search = self.head
        for _ in range(index):
            search = search.next
        # 抓一下index
        ind = search.next
        search.next = ind.next  # search 的 next 指向 ind 的 next
        ind.next = None         # 断掉 ind 的前后指针
        ind.prev = None
        if search.next:         # 如果有数，需要把他的前指针指向search也就是index前一个位置
            search.next.prev = search
        self.length -= 1

    # 获取链表长度
    def get_len(self):
        return self.length

    # 打印链表
    def print_linklist(self):
        search = self.head
        for _ in range(self.length):
            search = search.next
            print(search.val,end = '->' if search.next else '\n')

