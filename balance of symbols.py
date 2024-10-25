
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_value = self.head.data
        self.head = self.head.next
        return popped_value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

def is_matching_pair(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '{' and closing == '}':
        return True
    if opening == '[' and closing == ']':
        return True
    return False

def is_balanced(expression):
    stack = Stack()
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False  
            if not is_matching_pair(stack.pop(), char):
                return False  

    return stack.is_empty()

def process_expressions(n, expressions):
    for i, expr in enumerate(expressions, 1):
        if is_balanced(expr):
            print(f"Balanced")
        else:
            print(f"Not Balanced")

if __name__ == "__main__":
    n = int(input())
    expressions = [input() for i in range(n)]
    process_expressions(n, expressions)
