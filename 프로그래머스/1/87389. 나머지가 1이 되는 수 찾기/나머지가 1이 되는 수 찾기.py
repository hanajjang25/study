def solution(n):
    for i in range(n+1):
        if (n-1) % (i+2) == 0:
            answer = i+2
            break
            
    return answer