import sys
input = sys.stdin.readline
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 인접한 네 방향

# (sx, sy)에서 (ex, ey)로 가는 최단 거리를 BFS로 구해 반환
def bfs(sx, sy, ex, ey):
	dist = [[-1] * N for _ in range(N)] # -1은 방문하지 않은 상태를 의미한다.
	dist[sy][sx] = 0 # 시작 위치에서 시작 위치까지의 거리는 0이다.
	dq = deque()
	dq.append((sy, sx))

	while dq:
		y, x = dq.popleft()
		for dy, dx in dir:
			if 0 <= y + dy < N and 0 <= x + dx < N and dist[y + dy][x + dx] == -1 and not A[y + dy][x + dx]:
				dist[y + dy][x + dx] = dist[y][x] + 1
				dq.append((y + dy, x + dx))

	return dist[ey][ex]

N, M = map(int, input().split())
X, Y, Z = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

a = []
b = []
c = []
d = []
for _ in range(M):
	ai, bi, ci, di = map(int, input().split())
	a.append(ai)
	b.append(bi)
	c.append(ci)
	d.append(di)

# N과 M의 제한이 작으므로, 손님의 승하차 지점마다 BFS를 두 번 돌리는 시뮬레이션으로도 충분하다.
x = a[0] - 1; y = b[0] - 1 # 구름이의 첫 위치는 첫 번째 손님의 승차 지점이다.
res = 0
for i in range(M):
	move = bfs(x, y, a[i] - 1, b[i] - 1) # 손님을 태우러 가는 거리
	work = bfs(a[i] - 1, b[i] - 1, c[i] - 1, d[i] - 1) # 손님을 태우고 가는 거리
	x = c[i] - 1
	y = d[i] - 1 # 구름이의 위치는 이번 손님의 하차 지점이 된다.

	# 손님에게 받는 요금을 계산한다.
	if work <= 5:
		res += X
	else:
		res += X + (work - 5) * Y

	# 통행료를 계산한다.
	res -= (move + work) * Z

print(res)