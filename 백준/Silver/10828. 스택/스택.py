import sys

input = sys.stdin.read

data = input().splitlines()

n = int(data[0])

stack = []

for i in range(1, n+1):
  command = data[i].split()
  operation = command[0]
  
  if operation == "push":
    stack.append(command[1])
  elif operation == "pop":
    if stack:
      print(stack[len(stack) - 1])
      stack.pop(len(stack) - 1)
    else:
      print(-1)
  elif operation == "size":
    print(len(stack))
  elif operation == "empty":
    if stack:
      print(0)
    else:
      print(1)
  elif operation == "top":
    if stack:
      print(stack[len(stack) - 1])
    else:
      print(-1)
  else:
    print("error")
    break