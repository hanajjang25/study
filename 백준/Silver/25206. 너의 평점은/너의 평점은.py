total_credit = 0.0
rating = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sum = 0.0

for i in range(20):
  sub, credit, grade = input().split(" ")
  if grade == 'P':
    continue

  credit = float(credit)
  total_credit += credit
  
  for key, val in rating.items():
    if grade == key:
      grade = val
  sum += (credit*grade)

total_sum = sum / total_credit  
print(total_sum)