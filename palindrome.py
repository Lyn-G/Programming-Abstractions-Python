class Stack():
    def __init__(self):
         self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def is_palindrome(s):
    stack = Stack()
    for char in s:  # this line should be present in your code only once!!!
        stack.push(char)

    reverse = ''
    
    while not stack.isEmpty():
        reverse += stack.pop()
    
    if reverse == s:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))  
