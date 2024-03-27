def solution(t, p):
    answer = 0
    part = [t[i:i+len(p)] for i in range(0, len(t)-(len(p)-1))]
    for i in range(0, len(part)):
        if part[i] <= p:
            answer += 1
    return answer