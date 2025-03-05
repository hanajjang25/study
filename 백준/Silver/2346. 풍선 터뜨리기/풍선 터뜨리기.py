
from collections import deque

N = int(input())

balloon = deque(enumerate(map(int, input().split())))
paper = []

for _ in range(N):
  remove = balloon[0][1] 
  if remove > 0:
    remove -= 1
  paper.append(balloon[0][0] + 1)
  balloon.popleft()
  balloon.rotate(-1*remove)

print(' '.join(map(str,paper)))