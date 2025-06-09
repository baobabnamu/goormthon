import sys
input = sys.stdin.readline
sys.setrecursionlimit(11111)

def dfs(i, p):
	for j in G[i]:
		if j == p:
			continue
		dist[j] = dist[i] + 1
		dfs(j, i)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
	u, v = map(int, input().split())
	u -= 1; v -= 1
	G[u].append(v)
	G[v].append(u)

# 탐방할 수 있는 맛집의 최대 개수는 곧, 트리의 지름 + 1과 같다.

# 트리의 지름을 이루는 두 정점이 u, v이면, dist(u, v)가 트리 상에서 가장 긴 거리를 이룬다.
# 일단 임의의 정점 i에서 가장 먼 정점을 찾자. 찾은 정점은 반드시 u, v 중 하나가 된다. 만약 찾은 정점이 u, v가 아니라면 찾은 정점을 j라 했을 때,
# dist(u, i) + dist(i, v) > dist(u, i) + dist(i, j)과 dist(u, i) + dist(i, v) > dist(j, i) + dist(i, v)를 만족해야 한다.
# 하지만 i에서 제일 먼 정점을 찾은 것이기 때문에 두 부등식을 만족할 수 없다.
dist = [0] * N
dfs(0, -1)
u = 0
for i in range(1, N):
	if dist[u] < dist[i]:
		u = i

# u를 찾았다면 이제 u에서 가장 먼 정점을 찾으면 된다. 찾은 정점은 반드시 v가 된다.
# 만약 찾은 정점이 v가 아니라면 찾은 정점을 j라 했을 때,
# dist(u, j) < dist(u, v)를 만족해야 하지만, u에서 가장 먼 정점을 찾은 것이기 때문에 모순이 된다.
dist = [0] * N
dfs(u, -1)
v = 0
for i in range(1, N):
	if dist[v] < dist[i]:
		v = i

# dist(u, v) + 1을 출력한다.
print(dist[v] + 1)