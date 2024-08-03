def check(place):
    for row_idx, row in enumerate(place):
        for col_idx, col in enumerate(row):
            if col != 'P':
                continue
            
            isNotEndRow = row_idx != 4
            isNotEndCol = col_idx != 4
            isNotFirstCol = col_idx != 0
            isBeforeThirdRow = row_idx < 3
            isBeforeThirdCol = col_idx < 3
            
            if isNotEndRow:
                D = place[row_idx+1][col_idx]
                if D == 'P': return 0
                if isNotEndCol:
                    R = place[row_idx][col_idx+1]
                    RD = place[row_idx+1][col_idx+1]
                    if RD == 'P' and (D != 'X' or R != 'X'): return 0
                    if R == 'P': return 0
                if isNotFirstCol:
                    L = place[row_idx][col_idx - 1]
                    LD = place[row_idx + 1][col_idx - 1]
                    if L == 'P': return 0
                    if LD == 'P' and (L != 'X' or D != 'X'): return 0
                if isBeforeThirdRow:
                    D2 = place[row_idx + 2][col_idx]
                    if D2 == 'P' and D != 'X': return 0
            if isNotEndCol:
                R = place[row_idx][col_idx+1]
                if R == 'P': return 0
                if isBeforeThirdCol:
                    R2 = place[row_idx][col_idx+2]
                    if R2=='P' and R != 'X': return 0
                    
    return 1

def solution(places):
    answer = [check(place) for place in places]
    return answer