
import sys
from collections import deque

N = int(sys.stdin.readline())
myqueue = deque()

for _ in range(N):
  command = sys.stdin.readline().split()

  if command[0] == 'push':
    num = int(command[1])
    myqueue.append(num)
  
  elif command[0] == 'pop':
    if len(myqueue) == 0:
      print("-1")
    else:
      print(myqueue.popleft())
  
  elif command[0] == 'size':
    print(len(myqueue))
  
  elif command[0] == 'empty':
    if len(myqueue) == 0:
      print("1")
    else:
      print("0")
  
  elif command[0] == 'front':
    if len(myqueue) == 0:
      print("-1")
    else:
      print(myqueue[0])
  
  elif command[0] == 'back':
    if len(myqueue) == 0:
      print("-1")
    else:
      print(myqueue[-1])

  