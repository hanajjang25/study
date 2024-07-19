# 교점 찾기
def interaction(a,b):
    coord = []
    if a[0]*b[1] - a[1]*b[0] == 0:
        return None
    x = (a[1]*b[2] - a[2]*b[1])/ (a[0]*b[1] - a[1]*b[0])
    y = (a[2]*b[0] - a[0]*b[2])/ (a[0]*b[1] - a[1]*b[0])
    if x == int(x) and y == int(y):
        coord.append(int(x))
        coord.append(int(y))
    else:
        return None
    return coord

def solution(line):
    answer = []
    n = len(line)
    meet = []
    
    min_x = min_y = int(1e15)
    max_x = max_y = -int(1e15)
     
    # 교점 찾기
    for i in range(n):
        for j in range(i+1, n):
            dot = interaction(line[i], line[j])
            if dot is not None:
                meet.append(dot)
            
                # 사각형 만들기
                if dot[0] > max_x: max_x = dot[0]
                if dot[0] < min_x: min_x = dot[0]
                if dot[1] > max_y: max_y = dot[1]
                if dot[1] < min_y: min_y = dot[1]
            
    len_x = max_x - min_x + 1
    len_y = max_y - min_y + 1
    
    coord = [['.'] * len_x for _ in range(len_y)]
    
    for x, y in meet:
        star_x = x + abs(min_x) if min_x < 0 else x - min_x
        star_y = y + abs(min_y) if min_y < 0 else y - min_y
        coord[star_y][star_x] = "*"
        
    for result in coord:
        answer.append(''.join(result))
    
    return answer[::-1]