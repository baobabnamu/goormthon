import sys
input = sys.stdin.readline
from math import inf
from heapq import heappop, heappush
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 8방향

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

# 본사와 지사를 우선 찾는다.
for i in range(N):
	for j in range(M):
		if S[i][j] == 'S':
			start_i = i
			start_j = j
		elif S[i][j] == 'E':
			end_i = i
			end_j = j

''' 본사에서 지사로 가는 최단 시간을 찾아야 하며
각 칸에서 나아갈 때의 시간이 전부 다르기 때문에 다익스트라가 적합하다. '''

pq = [(0, start_i, start_j, 0)] # 거리, 행 번호, 열 번호, 방향
dist = [[[inf] * 8 for _ in range(M)] for _ in range(N)] # dist(i, j, k): (i, j)에 k번째 방향으로 도착했을 때의 최단 거리
for k in range(8): # 시작점에서는 모든 방향에 대해 최단 거리가 전부 0이다.
	dist[start_i][start_j][k] = 0

while pq:
	d, i, j, k = heappop(pq)
	if dist[i][j][k] < d:
		continue

	# (i, j)가 빈 곳인 경우
	if S[i][j].isdigit():
		next_i = i + dir[k][0]
		next_j = j + dir[k][1]
		if 0 <= next_i < N and 0 <= next_j < M and S[next_i][next_j] != '#' and dist[next_i][next_j][k] > dist[i][j][k] + int(S[i][j]):
			dist[next_i][next_j][k] = dist[i][j][k] + int(S[i][j])
			heappush(pq, (dist[next_i][next_j][k], next_i, next_j, k))

	# (i, j)가 빈 곳이 아닐 경우
	else:
		for nk in range(8): # 여덟 방향 중 아무 방향으로 보낼 수 있다.
			next_i = i + dir[nk][0]
			next_j = j + dir[nk][1]
			if 0 <= next_i < N and 0 <= next_j < M and S[next_i][next_j] != '#' and dist[next_i][next_j][nk] > dist[i][j][k] + 1:
				dist[next_i][next_j][nk] = dist[i][j][k] + 1
				heappush(pq, (dist[next_i][next_j][nk], next_i, next_j, nk))

res = inf
for k in range(8):
	res = min(res, dist[end_i][end_j][k])

if res < inf:
	print(res)
else:
	print(-1)