class Stack:
    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> None:
        return self.data.pop()

    def top(self) -> None:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self) -> str:
        final = ", ".join(reversed(self.data))
        return f"[{final}]"

import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()