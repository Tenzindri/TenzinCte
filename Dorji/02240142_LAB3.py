# Stack implementation using array.
class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity   # underlying array
        self.top = -1                    # index of top element
        self.capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow!")
            return
        self.top += 1
        self.stack[self.top] = element
        print(f"Pushed {element} to the stack")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
            return None
        element = self.stack[self.top]
        self.top -= 1
        print(f"Popped element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top]

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Display stack:", self.stack[:self.top+1])

# Example usage
s = ArrayStack()

print("Stack is empty:", s.is_empty())

s.push(10)
s.display()

s.push(20)
s.display()

s.push(30)
s.display()

print("Top element:", s.peek())

s.pop()
print("Stack size:", s.size())

s.display()