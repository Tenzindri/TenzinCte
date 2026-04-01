class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__size = 0
        print("Created new LinkedQueue")

    def is_empty(self):
        return self.__front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.__front = self.__rear = new_node
        else:
            self.__rear.next = new_node
            self.__rear = new_node
        self.__size += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        
        removed_data = self.__front.data
        self.__front = self.__front.next
        
        # If the queue becomes empty after dequeue
        if self.__front is None:
            self.__rear = None
            
        self.__size -= 1
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.__front.data

    def size(self):
        return self.__size

    def display(self):
        if self.is_empty():
            print("Display queue:[]")
            return
        
        elements = []
        current = self.__front
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Display queue:[{','.join(elements)}]")

    def display_linked_format(self):
        # Specifically for the "Current queue: 20 -> 30 -> null" format
        current = self.__front
        output = "Current queue: "
        while current:
            output += f"{current.data} -> "
            current = current.next
        output += "null"
        print(output)

# --- Test Execution matching Example Output ---

if __name__ == "__main__":
    # Task 3 Initialization
    lq = LinkedQueue()
    print(f"Queue is empty: {lq.is_empty()}")

    # Task 4 Operations
    print("") # Formatting space
    lq.enqueue(10)
    lq.display()
    
    lq.enqueue(20)
    lq.display()
    
    lq.enqueue(30)
    lq.display()

    print(f"Front element: {lq.peek()}")
    
    removed = lq.dequeue()
    print(f"Dequeued element: {removed}")

    lq.display_linked_format()
    print(f"Queue size: {lq.size()}")
