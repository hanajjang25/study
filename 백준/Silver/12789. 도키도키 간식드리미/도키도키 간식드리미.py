N = int(input())
students = list(map(int, input().split()))

count = 1
stack = []

for i in range(N):
  if students[i] == count:
    count += 1
    for j in range(len(stack)):
      if stack[-1] == count:
        stack.pop()
        count += 1
      else:
        break
    continue
  else:
    if stack and stack[-1] < students[i]:
      tmp = stack.pop()
      stack.append(students[i])
      stack.append(tmp)
    else:
      stack.append(students[i])
  
if len(stack) == 0:
  print("Nice")
else:
  print("Sad")