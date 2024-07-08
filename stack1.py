# assignment: programming assignment 4
# author: Lynelle Goh
# date: 11/17/2022
# file: stack.py is a program that is basically a Stack ADT which mimics the behavior of a stack
# input: takes in values and respectively manipulates the stack with it
# output: outputs the function required from the stack, such as getting the size, appending an object, checking out the top value, and more

# most functions were copied and pasted from our assignment where we had to finish our own Stack ADT
class Stack:
    
    def __init__(self):
        self.items = [] 

    def isEmpty(self):
        # return true if there is nothing in the list
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        # if list is empty, return None
        if self.items == []:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
