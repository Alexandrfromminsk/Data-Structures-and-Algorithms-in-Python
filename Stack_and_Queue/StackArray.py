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