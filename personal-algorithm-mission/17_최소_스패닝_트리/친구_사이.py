import sys
input = sys.stdin.readline
from heapq import heappop, heappush

''' 이 문제는 결국 N개의 정점과 M개의 간선이 있는 그래프를 연결 그래프로 만들기 위한 필요한 간선들을 가중치 합이 최소가 되게 구하는 것이다.
프림으로 접근한다면 M개의 간선은 처음부터 이어져 있는 간선이라서 곧 가중치가 0인 간선으로 간주할 수 있다.
그러므로 M개의 간선은 가중치가 0으로 간주해서 K개의 간선과 합해서 그래프를 만들어주고
1번 정점부터 시작해서 MST를 만들어나가면 된다. '''

N = int(input())
G = [[] for _ in range(N)] # N개의 정점이 있는 그래프를 인접 그래프로 표현한다.

# 가중치가 0인 간선들
M = int(input())
for _ in range(M):
	a, b = map(int, input().split())
	a -= 1
	b -= 1
	G[a].append((b, 0))
	G[b].append((a, 0))

# 일반 간선들
K = int(input())
for _ in range(K):
	u, v, w = map(int, input().split())
	u -= 1
	v -= 1
	G[u].append((v, w))
	G[v].append((u, w))

# 0번 정점부터 MST를 만들어 나간다.
pq = [(0, 0)]
visited = [False] * N
res = 0 # 친분을 쌓는 시간의 합

while pq:
	d, u = heappop(pq)
	if visited[u]: # 이미 MST에 포함된 정점이라면 넘어간다.
		continue
	visited[u] = True
	res += d
	for v, w in G[u]:
		if visited[v]: # 이미 MST에 포함된 정점이라면 넘어간다.
			continue
		heappush(pq, (w, v))

# MST에 포함되지 않은 정점이 있다면 모든 정점이 연결되지 않았다는 의미이다.
for i in range(N):
	if not visited[i]:
		print(-1)
		exit()

print(res)