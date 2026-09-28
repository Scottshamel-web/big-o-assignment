from collections import deque


# ==================================================
# Part 1 - Linked List
# ==================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

        print("None")

    def delete(self, target):
        """Remove the first node with the given value.
        Return True if found, False if not.
        """

        if self.head is None:
            return False

        # Target is the first node
        if self.head.value == target:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next.value == target:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def length(self):
        """Return the number of nodes in the list. O(n) time."""

        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    def to_list(self):
        """Convert the linked list to a Python list."""

        values = []
        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values


# Test Part 1

print("PART 1 - LINKED LIST")

ll = LinkedList()

for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

ll.display()
# 10 -> 20 -> 30 -> 40 -> 50 -> None

print(ll.length())
# 5

ll.delete(30)

ll.display()
# 10 -> 20 -> 40 -> 50 -> None

print(ll.to_list())
# [10, 20, 40, 50]


# ==================================================
# Part 2 - Stack: Bracket Validator
# ==================================================

def is_balanced(text):
    """Return True if all brackets in text are properly matched.
    Handles: (), [], {}
    """

    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    opening_brackets = {"(", "[", "{"}

    for char in text:

        if char in opening_brackets:
            stack.append(char)

        elif char in matching:

            # Closing bracket with no opening bracket
            if not stack:
                return False

            top = stack.pop()

            if top != matching[char]:
                return False

    return len(stack) == 0


# Test Part 2

print("\nPART 2 - BRACKET VALIDATOR")

print(is_balanced("()"))             # True
print(is_balanced("({[]})"))         # True
print(is_balanced("(]"))             # False
print(is_balanced("([)]"))           # False
print(is_balanced("hello (world)"))  # True


# ==================================================
# Part 3 - Queue: Task Processor
# ==================================================

class TaskProcessor:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, name):
        """Add a new task to the end of the queue."""
        self.tasks.append(name)

    def process_next(self):
        """Return the oldest unprocessed task or None if empty."""

        if not self.tasks:
            return None

        return self.tasks.popleft()


# Test Part 3

print("\nPART 3 - TASK PROCESSOR")

processor = TaskProcessor()

processor.add_task("Send email")
processor.add_task("Generate report")
processor.add_task("Backup files")

print(processor.process_next())  # Send email
print(processor.process_next())  # Generate report
print(processor.process_next())  # Backup files
print(processor.process_next())  # None