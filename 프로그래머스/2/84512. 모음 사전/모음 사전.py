def put(dictionary, word, length):
    if length == 6: return
    if word != '': dictionary.append(word)
    for i in ['A','E','I','O','U']:
        put(dictionary, ''.join([word, i]), length+1)

def solution(word):
    answer = 0
    dictionary = []
    put(dictionary, '',0)
    for i in range(len(dictionary)):
        if dictionary[i] == word:
            answer = i+1
            break
    return answer