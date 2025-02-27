word = []
for i in range(5):
  string = input()
  word.append(list(string))

max_length = max(len(line) for line in word)

out = []
for i in range(max_length):
  for j in range(5):
    if i < len(word[j]): 
       out.append(word[j][i])

print("".join(out))