# Hands-On 8: QuickSelect & Data Structures Python Program

This Python program implements the **QuickSelect algorithm** for finding the ith order statistic and provides implementations of **Stack, Queue, and Singly Linked List** using **fixed-size arrays**. The program offers the following functionalities:

### **Functionalities**
- **QuickSelect (ith Order Statistic)**: Finds the **ith smallest element** in an unsorted array using a **QuickSelect algorithm** (a variation of QuickSort).
- **Stack (Fixed-Size Array)**: Implements a stack with `push`, `pop`, and `peek` operations.
- **Queue (Circular Fixed-Size Array)**: Implements a circular queue with `enqueue`, `dequeue`, and `front` operations.
- **Singly Linked List**: Implements `insert`, `delete`, `search`, and `display` functions.

---

## **How to Run**
### **Step 1: Clone the Repository**
### **Step 2: Run the Python Program**

python data_structures.py
## Menu Options
Once you run the program, the following menu will be displayed:

## Find ith Order Statistic (QuickSelect)
When you select option 1, you will be prompted to enter:

A list of numbers.
The ith index (0-based) for the order statistic.
The program will then return the ith smallest element using QuickSelect.
## Stack Operations
When you select option 2, the following sub-options are available:

Push: Add an element to the stack.
Pop: Remove and return the top element.
Peek: View the top element without removing it.
## Queue Operations
When you select option 3, the following sub-options are available:

Enqueue: Add an element to the queue.
Dequeue: Remove and return the front element.
Front: View the front element without removing it.
## Linked List Operations
When you select option 4, the following sub-options are available:

Insert: Add an element at the head of the linked list.
Delete: Remove an element from the list.
Search: Check if an element exists in the list.
Display: Print the elements in the linked list.
## Exit
When you select option 5, the program will terminate.

## **Notes**
The QuickSelect algorithm efficiently finds the ith smallest element in O(n) expected time.
The Stack and Queue are implemented using fixed-size arrays, similar to C-style arrays.
The Queue is implemented as a circular queue for efficient wrap-around operations.
The Singly Linked List supports insertion, deletion, searching, and displaying elements.
The program is fully interactive, providing a menu-driven experience.
