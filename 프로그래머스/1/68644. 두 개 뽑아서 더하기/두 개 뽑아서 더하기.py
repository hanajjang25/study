def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)
                
    answer.sort()
                
    return answer