"""
Stack ADT: ArrayStack

This class implements the following methods:
    S.push(e)
    S.pop()
    S.peek()
    S.is_empty()
    len(S)

This class utilizes an array-based data structure,
a list, to store its data under the hood.
It only needs to keep track of that list.

This makes it an adapter class for the list,
since it adheres to the Stack ADT but does not change
the implementation of the underlying list type.
"""


class Empty(Exception):
    pass


class ArrayStack:
    """
    Implement the Stack ADT using an array-based data structure (list).
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def is_empty(self):
        """
        Check if empty. Don't bother calling our own __len__.
        Just do what is sensible.
        """
        return (len(self._data) == 0)

    def clear(self):
        """
        Recursive clear method
        """
        if (self.is_empty()):
            return
        else:
            self.pop()
            self.clear()

    def push(self, o):
        """
        Add an element to the top of the stack
        """
        self._data.append(o)

    def pop(self):
        """
        Pop the next item.
        This should handle an empty stack.
        """
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """
        Peek at the next item.
        This should handle an empty stack.
        """
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self._data[-1]

#question1

def get_tag(text):
    text_list = text.split()
    for i in range(len(text_list)):
        if text_list[i] == '<':
            for x in range(i, len(text_list)):
                if text_list[i] == '>':
                    yield ''.join(text_list[i-1:x+2])



def is_matched(expr):
    lefty = '({['
    righty = ']})'

    S = ArrayStack()
    for i in get_tag(expr):
        S.push()
    for token in expr:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty():
                return False
            from_S = S.top()
            if (righty.index(token) == lefty.index(from_S))
                S.pop()
            else:
                return False
        else:
            raise ValueError
    return S.is_empty()



 # question 2

def eval_postfix_boolean_exp(boolean_exp_str):
