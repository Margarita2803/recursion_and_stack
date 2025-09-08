class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Стек пуст"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Стек пуст"

    def is_empty(self):
            return len(self.stack) == 0

s = Stack()
s.push(3)
s.push(8)
print(s.pop())
print(s.peek())