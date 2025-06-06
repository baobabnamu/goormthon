import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def dist(x, y): # 유클리드 거리의 제곱의 두 배
	return (x ** 2 + y ** 2) * 2

N = int(input())
L = []
R = []
for _ in range(N):
	X, Y, T = map(int, input().split())
	L.append(T)
	R.append(T + dist(X, Y)) # 미사일마다 외계인에 도착하는 시각을 저장

'''	미사일의 시작 시각과 도착 시각은 전부 짝수가 된다.
그리고 S도 짝수이어야 하므로, 결국 미사일의 시작, 도착 시각을 구간으로 나타냈을 때
구간이 가장 많이 겹치는 [i, i+2) 구간을 찾아 i를 S로 정해야 한다.
이는 힙에 시작, 도착 시각을 넣어서 현재 활성화 중인 구간의 개수를 관리하면 된다. '''

pq = []
for i in range(N):
	heappush(pq, (L[i], 1, i))
	heappush(pq, (R[i], 0, i))

ct = res = 0
while pq:
	t, on, i = heappop(pq)
	if on:
		ct += 1
	else:
		ct -= 1
	res = max(res, ct)

# 날아가는 시간의 합에서 겹치는 구간의 개수를 빼주면 된다.
ans = 0
for i in range(N):
	ans += R[i] - L[i]
ans -= res

print(ans)