def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0]  = sizes[i][1]
            sizes[i][1] = temp
    
    maxfirst = sizes[0][0]
    maxsec = sizes[0][1]
    for i in range(len(sizes)-1):
        if maxfirst < sizes[i+1][0]:
            maxfirst = sizes[i+1][0]
        if maxsec < sizes[i+1][1]:
            maxsec = sizes[i+1][1]
            
    answer = maxfirst * maxsec
    return answer