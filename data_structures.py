# QuickSelect Algorithm (Find ith Order Statistic)
def quickselect(arr, left, right, i):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if i == pivot_index:
        return arr[i]
    elif i < pivot_index:
        return quickselect(arr, left, pivot_index - 1, i)
    else:
        return quickselect(arr, pivot_index + 1, right, i)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# -------------------------------------------------
# Stack (Fixed-Size Array)
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [0] * max_size
        self.top = -1

    def push(self, value):
        if self.top == self.max_size - 1:
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return -1
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        return "Stack is Empty" if self.top == -1 else self.stack[self.top]

    def is_empty(self):
        return self.top == -1

# -------------------------------------------------
# Queue (Fixed-Size Circular Array)
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [0] * max_size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue Underflow")
            return -1
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset queue
        else:
            self.front = (self.front + 1) % self.max_size
        return value

    def front_value(self):
        return "Queue is Empty" if self.front == -1 else self.queue[self.front]

# -------------------------------------------------
# Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        while temp:
            if temp.value == value:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return
            prev = temp
            temp = temp.next

    def search(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.value, "->", end=" ")
            temp = temp.next
        print("NULL")

# -------------------------------------------------
# Menu-Driven Program
def main():
    stack = Stack(5)
    queue = Queue(5)
    linked_list = SinglyLinkedList()

    while True:
        print("\n===== MENU =====")
        print("1. Find ith Order Statistic (QuickSelect)")
        print("2. Stack Operations")
        print("3. Queue Operations")
        print("4. Linked List Operations")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
            i = int(input("Enter i (0-based index) for ith order statistic: "))
            if 0 <= i < len(arr):
                print(f"{i+1}th smallest element:", quickselect(arr, 0, len(arr) - 1, i))
            else:
                print("Invalid index!")

        elif choice == '2':
            while True:
                print("\nStack Operations:")
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
                print("4. Back to Main Menu")
                stack_choice = input("Enter choice: ")

                if stack_choice == '1':
                    value = int(input("Enter value to push: "))
                    stack.push(value)
                elif stack_choice == '2':
                    print("Popped:", stack.pop())
                elif stack_choice == '3':
                    print("Top element:", stack.peek())
                elif stack_choice == '4':
                    break

        elif choice == '3':
            while True:
                print("\nQueue Operations:")
                print("1. Enqueue")
                print("2. Dequeue")
                print("3. Front")
                print("4. Back to Main Menu")
                queue_choice = input("Enter choice: ")

                if queue_choice == '1':
                    value = int(input("Enter value to enqueue: "))
                    queue.enqueue(value)
                elif queue_choice == '2':
                    print("Dequeued:", queue.dequeue())
                elif queue_choice == '3':
                    print("Front element:", queue.front_value())
                elif queue_choice == '4':
                    break

        elif choice == '4':
            while True:
                print("\nLinked List Operations:")
                print("1. Insert")
                print("2. Delete")
                print("3. Search")
                print("4. Display")
                print("5. Back to Main Menu")
                ll_choice = input("Enter choice: ")

                if ll_choice == '1':
                    value = int(input("Enter value to insert: "))
                    linked_list.insert(value)
                elif ll_choice == '2':
                    value = int(input("Enter value to delete: "))
                    linked_list.delete(value)
                elif ll_choice == '3':
                    value = int(input("Enter value to search: "))
                    print("Found" if linked_list.search(value) else "Not Found")
                elif ll_choice == '4':
                    linked_list.display()
                elif ll_choice == '5':
                    break

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")

# Run the menu program
if __name__ == "__main__":
    main()
