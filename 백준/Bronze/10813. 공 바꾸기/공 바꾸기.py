
N, M = input().split()

N = int(N)
M = int(M)

ary = [0] * N

for i in range(N):
  ary[i] = i+1

for i in range(M):
  a, b = input().split()
  a = int(a)
  b = int(b)
  temp = ary[a-1]
  ary[a-1] = ary[b-1]
  ary[b-1] = temp

for i in range(N):
  print(ary[i], end=' ')
