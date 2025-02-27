import sys

N = int(sys.stdin.readline())
stack = []

for i in range(N):
  command = sys.stdin.readline().split()
  if command[0] == '1':
    stack.append(command[1])
  elif command[0] == '2':
    if len(stack) != 0:
      print(stack[-1])
      stack.pop()
    else:
      print("-1")
  elif command[0] == '3':
    print(len(stack))
  elif command[0] == '4':
    if len(stack) != 0:
      print("0")
    else:
      print("1")
  elif command[0] == '5':
    if len(stack) != 0:
      print(stack[-1])
    else:
      print("-1")
