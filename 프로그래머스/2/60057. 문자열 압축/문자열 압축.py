def solution(s):
    answer = len(s)
    for x in range(1, len(s)+1):
        cnt = 1
        cmp = ''
        cmp_len = 0
        for i in range(0, len(s)+1, x):
            tmp = s[i:i+x]
            if tmp == cmp:
                cnt += 1
            else:
                cmp_len += len(tmp)
                if cnt>1: cmp_len += len(str(cnt))
                cnt = 1
                cmp = tmp
        answer = min(answer, cmp_len)
                
    return answer