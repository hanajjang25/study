from itertools import permutations

def primenumber(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False 
    return True
        
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    arr = []
    
    for i in range(1, len(numbers)+1):
        arr.append(list(permutations(numbers, i)))
    
    arr = [int(''.join(y)) for x in arr for y in x]
        
    arr = set(arr)
    
    for i in arr:
        if primenumber(i):
            answer = answer + 1

        
    return answer