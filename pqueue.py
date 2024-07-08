from stack import Stack

class PQueue:
    def __init__(self):
        self.stack = Stack()

    def __str__(self):
        return str(self.stack)

    def empty(self):
        return self.stack.isEmpty()

    def enqueue(self, item):
        if self.stack.size() == 0 or item > self.stack.peek():
            self.stack.push(item)
        else:
            x = self.stack.pop()
            self.enqueue(item)

            self.stack.push(x)
        
    def dequeue(self):
        if self.stack.size == 0:
            print('Priority queue is empty!')
        else:
            return self.stack.pop() 
    
if __name__ == '__main__':
    pq = PQueue()
    data = [1, 3, 5, 2, 0, 6, 4]
    for i in data:
        pq.enqueue(i)
        print('adding', i)
        print(pq)
        
    while not pq.empty():
        print('removing', pq.dequeue())
        print(pq)