T = int(input())

for i in range(T):
  stack = []
  PS = input()
  for j in range(len(PS)):
    if j == 0:
      if PS[j] == ')':
        stack.append(PS[j])
        continue
      else:
        stack.append(PS[j])
    else:
      if PS[j] == '(':
        stack.append(PS[j])
      else:
        if len(stack) == 0:
          stack.append(PS[j])
        if stack[-1] == '(':
          stack.pop()
  
  if len(stack) == 0:
    print("YES")
  else:
    print("NO")
