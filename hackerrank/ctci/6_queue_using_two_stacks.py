#https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
#https://stackoverflow.com/a/39089983

class MyQueue(object):
    def __init__(self):
        self.first = [] #for enqueue or put operation
        self.second = [] #for dequeue or pop operation
    
    def _push_to_output_stack(self):
        while self.first:
                self.second.append(self.first.pop())
                
    def peek(self):
        if not self.second:
            self._push_to_output_stack()
        return self.second[-1]        
        
    def pop(self):
        if not self.second:
            self._push_to_output_stack()
        return self.second.pop()
        
    def put(self, value):
        self.first.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
