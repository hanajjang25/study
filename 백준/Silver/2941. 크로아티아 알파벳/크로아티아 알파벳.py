cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in cr:
  word = word.replace(i,"c")

print(len(word))
