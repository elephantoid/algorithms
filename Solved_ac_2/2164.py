n= 6
import sys
from collections import deque
N = 6
queue=deque()
for i in range(N): 
    queue.append(i + 1)

while len(queue)>1:
    queue.popleft()
    print(queue)
    queue.append(queue.popleft())
    print(queue)
    
print(queue.pop())