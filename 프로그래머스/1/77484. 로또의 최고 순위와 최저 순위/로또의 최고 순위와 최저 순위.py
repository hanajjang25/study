def check(correct):
    rank = 0
    
    if correct == 6:
        rank = 1
    elif correct == 5:
        rank = 2
    elif correct == 4:
        rank = 3
    elif correct == 3:
        rank = 4
    elif correct == 2:
        rank = 5
    else :
        rank = 6
        
    return rank

def solution(lottos, win_nums):
    answer = []
    correct = 0
    zero = 0
    highrank = 0
    lowrank = 0
    
    for i in lottos:
        if i in win_nums:
            correct = correct + 1
        if i == 0:
            zero = zero + 1

    lowrank = check(correct)
    highrank = check(correct + zero)
    
    answer.append(highrank)
    answer.append(lowrank)
        
    return answer