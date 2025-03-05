import sys
from collections import deque

deq = deque()
N = int(sys.stdin.readline())

for i in range(N):
  command = sys.stdin.readline().split()

  if command[0] == '1':
    deq.appendleft(command[1])
  elif command[0] == '2':
    deq.append(command[1])
  elif command[0] == '3':
    if len(deq) == 0:
      print("-1")
    else:
      print(deq.popleft())
  elif command[0] == '4':
    if len(deq) == 0:
      print("-1")
    else:
      print(deq.pop())
  elif command[0] == '5':
    print(len(deq))
  elif command[0] == '6':
    if len(deq) == 0:
      print("1")
    else:
      print("0")
  elif command[0] == '7':
    if len(deq) != 0:
      print(deq[0])
    else:
      print("-1")
  elif command[0] == '8':
    if len(deq) != 0:
      print(deq[-1])
    else:
      print("-1")