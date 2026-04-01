#Queue Implementation using Array

class ArrayQueue:
    def __init__(self, capacity=4):
        # Private array initialized with None
        self.__queue = [None] * capacity
        self.__capacity = capacity
        self.__front = 0
        self.__rear = 0
        self.__count = 0
        print(f"Created new Queue with capacity: {self.__capacity}")

    def is_empty(self):
        return self.__count == 0

    def is_full(self):
        return self.__count == self.__capacity

    def enqueue(self, element):
        if self.is_full():
            print("Queue Overflow: Cannot add element.")
            return
        
        self.__queue[self.__rear] = element
        # Move rear index circularly
        self.__rear = (self.__rear + 1) % self.__capacity
        self.__count += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: Queue is empty.")
            return None
        
        element = self.__queue[self.__front]
        self.__queue[self.__front] = None  # Clear the slot
        # Move front index circularly
        self.__front = (self.__front + 1) % self.__capacity
        self.__count -= 1
        return element

    def peek(self):
        if self.is_empty():
            return None
        return self.__queue[self.__front]

    def size(self):
        return self.__count

    def display(self):
        if self.is_empty():
            print("Display queue: []")
            return
        
        # Extract elements in the correct order for display
        elements = []
        for i in range(self.__count):
            index = (self.__front + i) % self.__capacity
            elements.append(self.__queue[index])
        print(f"Display queue: {elements}")

# --- Testing the implementation based on Example Output ---

if __name__ == "__main__":
    # Task 1 initialization
    my_queue = ArrayQueue(10)
    print(f"Queue is empty: {my_queue.is_empty()}")

    print("\n--- Task 2: Operations ---")
    # Enqueue elements
    my_queue.enqueue(10)
    my_queue.display()
    
    my_queue.enqueue(20)
    my_queue.display()
    
    my_queue.enqueue(30)
    my_queue.display()
    my_queue.enqueue(40)
    my_queue.display()

    my_queue.enqueue(50)
    my_queue.display()

    my_queue.enqueue(60)
    my_queue.display()

    # Peek
    print(f"Front element: {my_queue.peek()}")

    # Dequeue
    removed = my_queue.dequeue()
    print(f"Dequeued element: {removed}")

    removed = my_queue.dequeue()
    print(f"Dequeued element: {removed}")

    # Final state
    my_queue.display()
    print(f"Queue size: {my_queue.size()}")
