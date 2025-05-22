import sys
input = sys.stdin.readline

def find(u):
	if parent[u] != u: # 현재 자신과 자신의 부모가 같지 않다면 자신이 집합의 루트가 아니라는 것이다.
		parent[u] = find(parent[u]) # 재귀적으로 루트를 찾아서 부모 노드를 루트로 갱신한다.
	return parent[u] # 루트 노드를 반환한다.

def union(u, v):
	# 합치고자 하는 두 노드가 속해 있는 집합의 루트를 구한다.
	root_u = find(u)
	root_v = find(v)

	# 루트가 같다면 집합이 이미 같다는 뜻이다.
	if root_u == root_v:
		return False

	# 루트가 다르다면 루트의 번호가 큰 쪽이 작은 쪽의 집합 밑으로 들어가게 한다.
	if root_u < root_v:
		parent[root_v] = root_u
	else:
		parent[root_u] = root_v
	return True

N, M = map(int, input().split())

parent = [i for i in range(N + 1)] # 처음에는 자기 자신을 부모로 가지게끔 한다.
ct = N # 처음엔 N개의 집합이 있다.
for _ in range(M):
	a, b = map(int, input().split())
	if union(a, b): # a와 b가 합쳐진다면
		ct -= 1 # 집합의 개수는 하나 줄어든다.

print(ct)