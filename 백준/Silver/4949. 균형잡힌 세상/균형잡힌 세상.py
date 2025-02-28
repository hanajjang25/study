while(True):
  stack = []
  line = input()
  
  if line == '.':
    break

  for i in range(len(line)):
    if line[i] == '[':
      stack.append(line[i])
    elif line[i] == '(':
      stack.append(line[i])
    elif line[i] == ']':
      if len(stack) == 0:
        stack.append(line[i])
      if stack[-1] == '[':
        stack.pop()
      else:
        stack.append(line[i])
    elif line[i] == ')':
      if len(stack) == 0:
        stack.append(line[i])
      if stack[-1] == '(':
        stack.pop()
      else:
        stack.append(line[i])

  if len(stack) == 0:
    print('yes')
  else:
    print('no')