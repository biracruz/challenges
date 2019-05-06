#https://leetcode.com/submissions/detail/227174536/

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.len = len(self.stack)

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop(self.len -1)

    def top(self) -> int:
        return self.stack[self.len - 1]

    def getMin(self) -> int:
        #O(n)
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


#minStack = MinStack()
#minStack.push(-2)
#minStack.push(0)
#minStack.push(-3)
#assert minStack.getMin() is -3
#minStack.pop()
#assert minStack.top() is 0
#assert minStack.getMin() is -2