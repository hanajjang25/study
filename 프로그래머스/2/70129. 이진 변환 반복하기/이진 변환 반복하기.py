def solution(s):
    change = 0
    zero = 0
    while s != '1':
        change += 1
        number = s.count('1')
        zero += len(s) - number
        s = bin(number)[2:]
    return [change, zero]