S = list(input())
min_time = 0

for i in range(len(S)):
  if S[i] == "A" or S[i] == "B" or S[i] == "C":
    min_time = min_time + 3
  elif S[i] == "D" or S[i] == "E" or S[i] == "F":
    min_time = min_time + 4
  elif S[i] == "G" or S[i] == "H" or S[i] == "I":
    min_time = min_time + 5
  elif S[i] == "J" or S[i] == "K" or S[i] == "L":
    min_time = min_time + 6
  elif S[i] == "M" or S[i] == "N" or S[i] == "O":
    min_time = min_time + 7
  elif S[i] == "P" or S[i] == "Q" or S[i] == "R" or S[i] == "S":
    min_time = min_time + 8
  elif S[i] == "T" or S[i] == "U" or S[i] == "V":
    min_time = min_time + 9
  elif S[i] == "W" or S[i] == "X" or S[i] == "Y" or S[i] == "Z":
    min_time = min_time + 10
  else:
    break

print(min_time)
