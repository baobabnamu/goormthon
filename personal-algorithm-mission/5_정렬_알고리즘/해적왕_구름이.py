import sys
input = sys.stdin.readline

N = int(input())
islands = []
for i in range(N):
	x, y = map(int, input().split())
	islands.append(((x, y), i))

# 좌표를 기준으로 오름차순 정렬했을 때, 뒤쪽에 위치한 섬들을 약탈할 수 있다.
islands.sort()

# 1번부터 차례대로 결과를 출력해야 하기 때문에, 결과를 저장할 배열을 만들어 준다.
res = [0] * N

# 정렬한 섬 순서대로, 자신보다 뒤쪽에 위치한 섬들의 개수를 res에 섬의 인덱스의 맞게 저장한다.
for i in range(N):
	(x, y), idx = islands[i]
	res[idx] = N - i - 1

for i in range(N):
	print(res[i])

# 핵심 아이디어
# 1. 좌표를 기준으로 오름차순 정렬했을 때, 뒤쪽에 위치한 섬들을 약탈할 수 있다.
# 2. 좌표를 기준으로 오름차순 정렬했을 때, 뒤쪽에 위치한 섬들의 개수를 res에 섬의 인덱스의 맞게 저장한다.
# 1 ~ 2번 과정을 쉽게 구현하기 위해서는 내부에 좌표(x, y)를 저장하는 튜플, 외부에 좌표, 인덱스((x,y), index)를 사용해야 한다.
# 예시)
# islands = [((1, 2), 0), ((2, 3), 1), ((3, 4), 2)]
# islands.sort()
# print(islands)
# 출력: [((1, 2), 0), ((2, 3), 1), ((3, 4), 2)]

