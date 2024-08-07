def solution(s):
    answer = {}
    s = sorted(s[2:-2].split("},{"), key=len)
    for data in s:
        items = data.split(",")
        for item in items:
            number = int(item)
            if number not in answer:
                answer[number] = 1
    return list(answer)