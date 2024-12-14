#Queue Implementation
class Queue:
    def __init__(self):
        self.queue = []  
      
    def enqueue(self, element):
        """Adds an element to the end of the queue."""
        self.queue.append(element)
        print(f"Enqueued: {element}")

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if not self.is_empty():
            element = self.queue.pop(0)
            print(f"Dequeued: {element}")
            return element
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def peek(self):
        """Returns the front element of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Returns the number of elements in the queue."""
        return len(self.queue)

    def display(self):
        """Prints the current elements in the queue."""
        print("Queue:", self.queue)

my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.display()  

print("Front element:", my_queue.peek())  

my_queue.dequeue()
my_queue.dequeue()
my_queue.display()  

print("Is queue empty?", my_queue.is_empty())  

my_queue.dequeue()
print("Is queue empty?", my_queue.is_empty())  
