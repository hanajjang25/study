def solution(answers):
    answer = []
    math_1 = [1,2,3,4,5]
    math_2 = [2,1,2,3,2,4,2,5]
    math_3 = [3,3,1,1,2,2,4,4,5,5]
    
    correct = [0, 0, 0]
    
    for idx, i in enumerate(answers):
        if i == math_1[idx % len(math_1)]:
            correct[0] += 1
        if i == math_2[idx % len(math_2)]:
            correct[1] += 1
        if i == math_3[idx % len(math_3)]:
            correct[2] += 1
    
    for idx, i in enumerate(correct):
        if i == max(correct):
            answer.append(idx+1)
    
    answer.sort()
    
    return answer