import sys
sys.setrecursionlimit(2000)

def assignment(i, answer):
    if i not in answer:
        answer[i] = i + 1
        return i
    empty = assignment(answer[i], answer)
    answer[i] = empty + 1
    return empty
    
def solution(k, room_number):
    answer = dict()
    for i in room_number:
        check = assignment(i, answer)
    return list(answer)