N = int(input())

count = 0
dup = 0

for i in range(N):
  word = input()
  for j in range(len(word)-2):
    for k in range(j+2,len(word)):
      if word[j] == word[k] and word[j] != word[j+1]:
        dup = 1
  if dup == 0:
    count += 1
  else:
    dup = 0
    

print(count)