
ary = []
attend = list(range(1, 31))

for i in range(28):
  ary.append(int(input()))

for i in ary:
  if i in attend:
    attend.remove(i)

for num in attend:
  print(num)