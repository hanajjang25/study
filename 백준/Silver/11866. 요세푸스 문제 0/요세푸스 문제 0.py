from collections import deque

N,K = map(int, input().split())
around = deque([i+1 for i in range(N)])
result = []

while len(around) != 0:
  for _ in range(K-1):
    around.append(around.popleft())
  result.append(str(around.popleft()))

print("<"+', '.join(result)+">")