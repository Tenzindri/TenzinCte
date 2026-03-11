class CustomList:
    def __init__(self, capacity=10):
        self.__storage = [None] * capacity
        self.__capacity = capacity
        self.__size = 0
        print(f"Created new CustomList with capacity: {self.__capacity}")
        print(f"Current size: {self.__size}")

    def append(self, element):
        if self.__size < self.__capacity:
            self.__storage[self.__size] = element
            self.__size += 1
            print(f"Appended {element} to the list")
        else:
            print("Error: Capacity reached")

    def get(self, index):
        if 0 <= index < self.__size:
            return self.__storage[index]
        raise IndexError("Index out of range")

    def set(self, index, element):
        if 0 <= index < self.__size:
            self.__storage[index] = element
            print(f"Set element at index {index} to {element}")
        else:
            raise IndexError("Index out of range")

    def size(self):
        return self.__size

# Testing the implementation
my_list = CustomList()
my_list.append(5)
print(f"Element at index 0: {my_list.get(0)}")
my_list.set(0, 10)
print(f"Element at index 0: {my_list.get(0)}")
print(f"Current size: {my_list.size()}")
