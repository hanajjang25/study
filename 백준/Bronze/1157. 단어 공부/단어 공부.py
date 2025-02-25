word = input()
dic = {}
word = word.upper()

for one in word:
  dic[one] = dic.get(one, 0) + 1

if len([k for k,v in dic.items() if max(dic.values()) == v]) > 1:
  print("?")
else:
  print(max(dic,key=dic.get))