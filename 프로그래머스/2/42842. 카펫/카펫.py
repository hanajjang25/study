import math

def solution(brown, yellow):
    answer = []
    S = int((brown/2) + 2)
    P = yellow + brown
    print(S)
    print(P)
    x = (S + math.sqrt(S**2 - 4*P)) / 2
    y = (S - math.sqrt(S**2 - 4*P)) / 2
    
    answer.append(x)
    answer.append(y)
    return answer
