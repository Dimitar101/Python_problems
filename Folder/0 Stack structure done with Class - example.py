# s = []
#
# # s.append(1)
# # s.append(2)
# # s.append(3)
#
# [s.append(x) for x in range(5)]
#
# while s:
#     print(s.pop())
#
# print(s)


class Stack:
    def __init__(self):
        self.internal_values = []

    def push(self, value):
        return self.internal_values.append(value)
    def pop(self):
        return self.internal_values.pop()
    def peek(self):
        return self.internal_values[-1]
    def is_empty(self):
        return len(self.internal_values) == 0

s = Stack()
[s.push(x) for x in range(5)]

while not s.is_empty():
    print(s.pop())
