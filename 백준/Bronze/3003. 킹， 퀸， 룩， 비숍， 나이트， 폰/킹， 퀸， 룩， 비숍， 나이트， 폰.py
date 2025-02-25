chess = [1, 1, 2, 2, 2, 8]

find = list(map(int, input().split()))

right = [ch - fi for ch,fi in zip(chess, find)]   # zip은 순회 가능한 객체를 인자로 받고 각 자료형의 각각의 요소를 나눈 후 인덱스끼리 잘라서 리스트 반환
print(' '.join(map(str,right)))