def solution(price, money, count):
    answer = 0
    
    fee = 0
    
    for i in range(count):
        fee += price*(i+1)

    if (fee - money) > 0:
        answer = fee - money
    return answer