
total = int(input())
type = int(input())

sum = 0

for i in range(type):
  price, num = input().split()
  price = int(price)
  num = int(num) 
  sum += price*num

if sum==total:
  print("Yes")
else :
  print("No")
