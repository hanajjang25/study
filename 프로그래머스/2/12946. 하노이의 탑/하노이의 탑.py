def hanoi(n, start, dst, mid, answer):
    if n == 1:
        return answer.append([start, dst])
    hanoi(n-1, start, mid, dst, answer)
    answer.append([start, dst])
    hanoi(n-1, mid, dst, start, answer)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer