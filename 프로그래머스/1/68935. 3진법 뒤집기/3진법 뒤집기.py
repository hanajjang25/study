def solution(n):
    answer = []
    while n:
        n, q = divmod(n, 3)
        answer.append(str(q))
    answer = ''.join(reversed(answer))
    answer = int(answer[::-1], 3)
    return answer