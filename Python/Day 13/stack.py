#Stack Implementation using list 
class Stack:
    def __init__(self):
        self.stack = []  

    def push(self, element):
        """Adds an element to the top of the stack."""
        self.stack.append(element)
        print(f"Pushed: {element}")

    def pop(self):
        """Removes and returns the top element of the stack."""
        if not self.is_empty():
            element = self.stack.pop()
            print(f"Popped: {element}")
            return element
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        """Returns the top element of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.stack)

    def display(self):
        """Prints the current elements in the stack."""
        print("Stack:", self.stack)


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.display()  

print("Top element:", my_stack.peek())  

my_stack.pop()
my_stack.pop()
my_stack.display()  


print("Is stack empty?", my_stack.is_empty())  

my_stack.pop()
print("Is stack empty?", my_stack.is_empty())  
