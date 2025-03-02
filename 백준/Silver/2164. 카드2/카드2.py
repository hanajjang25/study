from collections import deque

N = int(input())

card = deque([i+1 for i in range(N)])

while(True):
  if len(card) == 1:
    break
  else:
    card.popleft()
    tmp = card.popleft()
    card.append(tmp)

print(card[0])