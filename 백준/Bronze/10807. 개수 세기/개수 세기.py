num = int(input())

ary = list(map(int, input().split()))

find = int(input())
count = 0

for i in range(num):
  if(find == ary[i]):
    count += 1

print(count)