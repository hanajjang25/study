
N,M = input().split()

N = int(N)
M = int(M)

ary = [0] * N

for i in range(M):
  a,b,c = input().split()
  a = int(a)
  b = int(b)
  c = int(c)

  start = a
  for j in range(b-a+1):
    ary[start - 1] = c
    start += 1

for i in range(N):
  print(ary[i], end=' ')
    