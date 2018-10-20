"""
Stack implementation based on array (list)
"""
class StackArray:
    
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)==0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if is_empty():
            raise Empty("Stack is empty!")
        else:
            return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty!")