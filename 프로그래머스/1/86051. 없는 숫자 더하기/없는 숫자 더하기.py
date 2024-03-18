def solution(numbers):
    answer = -1
    total = 45
    for i in range(10):
        for j in range(len(numbers)):
            if numbers[j] == i:
                total -= i
            
    if total != 45:
        answer = total
    return answer