def solution(new_id):
    lowID = new_id.lower()
    
    newID = []
    for i in lowID:
        if i.isalpha() or i.isdigit() or i in ('-','_','.'):
            newID.append(i)
    answer = ''.join(newID)
    
    while '..' in answer:
        answer = answer.replace('..','.')
    
    answer = answer.strip('.')
    
    if answer == '':
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.strip('.')
    
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer
    