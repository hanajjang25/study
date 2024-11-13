def solution(s):
    answer = []
    stack = []
    for idx, letter in enumerate(s):
        if letter in stack:
            distances = [idx - i for i, ch in enumerate(stack) if ch == letter]
            answer.append(min(distances))
        else:
            answer.append(-1)
        stack.append(letter)
    return answer