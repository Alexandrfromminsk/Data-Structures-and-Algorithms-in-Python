class QueueLinkedList:

    class _Node:

        __slots__="_element", "_next"

        def __init__(self, element, next):
            self._element=element
            self._next=next

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def first(self):
        if self.is_empty():
            raise Exception("is empty!")
        return self.head._element

    def dequeue(self):
        if self.is_empty():
            raise Exception("is empty!")
        ans = self.head._element
        self.head=self.head._next
        self.size-=1
        if self.is_empty():
            self.tail=None
        return ans
    
    def enqueue(self, e):
        newest=_Node(e, None)
        if self.is_empty():
            self.head=newest
        else:
            self.tail._next=newest
        self.tail=newest
        self._size+=1


    
