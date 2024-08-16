def solution(phone_number):
    phone_number = list(phone_number)
    cnt = 0
    for i in range(len(phone_number)- 1, 0, -1):
        cnt += 1
        if cnt >= 4:
            phone_number[i-1] = '*'
    return ''.join(phone_number)