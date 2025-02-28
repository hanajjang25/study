stack = []

K = int(input())

for i in range(K):
  num = int(input())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

total = 0

for i in stack:
  total += i

print(total)