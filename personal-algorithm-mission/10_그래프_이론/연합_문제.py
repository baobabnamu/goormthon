import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

# 임의의 두 섬 사이에 다리가 있는지 저장하는 인접행렬
# edge[i][j]가 참이라면 i번 섬에서 j번 섬으로 가는 단방향 다리가 있는 것이다.
edge = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
	s, e = map(int, input().split())
	edge[s][e] = True

# 두 섬 사이에 양방향으로 이동할 수 있어야 두 섬이 연합을 결성할 수 있다.
# 이는 두 섬 사이에 단방향 간선이 각 방향으로 하나씩 있어야 된다는 의미가 된다.
# 모든 두 섬을 검사해서 그 두 섬 사이에 단방향 간선이 각 방향으로 하나씩 있다면 양방향 간선을 그래프에 추가한다.
graph = [[] for _ in range(N + 1)]
for i in range(1, N):
	for j in range(i + 1, N + 1):
		if edge[i][j] and edge[j][i]:
			graph[i].append(j)
			graph[j].append(i)

# 방문하지 않은 임의의 섬에서 시작하여 방문할 수 있는 모든 섬을 방문한다.
# 이때, 방문한 섬 전체가 하나의 연합을 이루게 된다.
visited = [False] * (N + 1) # 방문 배열
ct = 0 # 연합의 개수
for i in range(1, N + 1):
	if not visited[i]: # 방문하지 않은 섬을 찾았다면 그 섬에서 그래프 탐색을 시작한다.
		ct += 1 # i번 섬에서 방문할 수 있는 모든 섬이 하나의 연합을 이룬다.
		dq = deque() # BFS에 사용될 큐 (파이썬에선 덱)
		dq.append(i) # i번 섬에서 시작한다.
		visited[i] = True # 시작하는 섬은 처음에 방문처리를 한다.
		while dq:
			cur = dq.popleft()
			for nxt in graph[cur]:
				if not visited[nxt]: # 현재 섬과 인접한 nxt번 섬이 방문하지 않았다면
					dq.append(nxt) # nxt번 섬으로 이동한다.
					visited[nxt] = True # 방문처리도 같이 한다.

print(ct)