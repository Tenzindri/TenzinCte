
# Stack implementation using linked list in Python

# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack class using Linked List
class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1
        print(f"Pushed {data} to the stack")
        self.display_list_format()

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None
        
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        print(f"Popped element: {popped}")
        return popped

    # Peek (Top element)
    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        
        print(f"Top element: {self.top.data}")
        return self.top.data

    # Display in list format
    def display_list_format(self):
        temp = self.top
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        print(f"Display stack: {elements}")

    # Display in linked list format
    def display_linked_format(self):
        temp = self.top
        result = ""
        while temp:
            result += f"{temp.data} -> "
            temp = temp.next
        result += "null"
        print(f"Current stack: {result}")

    # Stack size
    def size(self):
        print(f"Stack size: {self.count}")
        return self.count


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.peek()
s.pop()

s.display_linked_format()
s.size()