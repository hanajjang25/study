import sys
from collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
# stack은 무시해도됨. deque만.

M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
deq = deque()

count = 0
result = []

for i in range(N):
  if A[i] == 0:
    deq.append(B[i])
    count += 1

for j in range(M):
  deq.append(C[j])
  if count > 1:
    deq.rotate(-(count-1))
  if deq:
    result.append(deq.popleft())

print(' '.join(map(str, result)))
 