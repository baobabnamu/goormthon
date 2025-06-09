import sys
input = sys.stdin.readline
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

R, C = map(int, input().split())
S = [input().strip() for _ in range(R)]

''' 불이 구름이에게 도달하는 최단 시간을 구하는 문제이다.
모든 불은 한 칸 움직일 때 시간 1씩 걸리므로 BFS가 적합하다. '''

dq = deque()
dist = [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
for i in range(R):
	for j in range(C):
		if S[i][j] == '@': # 불인 칸 모두 큐에 담는다.
			dq.append((i, j))
			visited[i][j] = True

while dq:
	i, j = dq.popleft()

	# 현재 정점으로부터 사방으로 뻗어나간다.
	for di, dj in dir:
		if 0 <= i + di < R and 0 <= j + dj < C and S[i + di][j + dj] != '#' and not visited[i + di][j + dj]:
			visited[i + di][j + dj] = True;
			dist[i + di][j + dj] = dist[i][j] + 1
			dq.append((i + di, j + dj))

for i in range(R):
	for j in range(C):
		if S[i][j] == '&':

			# 구름이가 있는 칸에 도달하지 못했을 경우 구름이와 인접한 칸에 불이 도달하지 못했다는 것이다.
			if not visited[i][j]:
				print(-1)

			# 불이 도달했다면, 인접한 칸까지의 거리를 구해야 하므로 거리-1 을 출력한다.
			else:
				print(dist[i][j] - 1)