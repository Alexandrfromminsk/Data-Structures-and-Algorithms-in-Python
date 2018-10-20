class QueueArray:

    DEFAULT_CAPACITY=10

    def __init__(self):
        self._data=[None]*QueueArray.DEFAULT_CAPACITY
        self._size=0
        self._front=0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size==0

    def first(self):
        if self.is_empty():
            raise Exception("Is EMPTY!")
        else:
            return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            raise Exception("Is EMPTY!")
        
        ans=self._data[self._front]
        self._data[self._front]=None
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        if 0< self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return ans

    def enqueue(self, val):
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=val
        self._size+=1

    def _resize(self, number):
        old = self._data
        self._data=[None]*number
        walk=self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk=(1+walk)%len(old)
        self._front=0
