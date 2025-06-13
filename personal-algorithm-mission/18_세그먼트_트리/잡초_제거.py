import sys
input = sys.stdin.readline
from math import ceil, log2

# 구간 합, 원소 업데이트를 처리해야 하므로 세그먼트 트리로 풀어내야 한다.

# 세그먼트 트리 만들기
# node : 현재 노드 번호, [start, end] : 현재 노드에 저장되는 합의 범위
def init(node, start, end):
	if start == end: # start와 end가 같다면 현재 노드는 리프 노드다.
		tree[node] = A[start] # 리프 노드에는 배열의 그 원소를 그대로 저장하면 된다.
	else:
		mid = (start + end) // 2 # 현재 범위를 반으로 나눈다.
		init(node * 2, start, mid) # 현재 노드의 왼쪽 자식에는 [start, mid] 범위의 합을 구한다.
		init(node * 2 + 1, mid + 1, end) # 현재 노드의 오른쪽 자식에는 [mid + 1, end] 범위의 합을 구한다.
		tree[node] = tree[node * 2] + tree[node * 2 + 1] # 현재 노드에 저장되는 범위에 대한 합은 양쪽 자식에 저장된 값을 더하면 구할 수 있다.

# 원소 업데이트
# node : 현재 노드 번호, [start, end] : 현재 노드에 저장된 합의 범위, index : 변경해야 하는 원소의 인덱스, val : 원소에 더할 값
def update(node, start, end, idx, val):
	if idx < start or end < idx: # 현재 노드에 저장된 범위에 index가 포함되어 있지 않다면, 현재 노드와 자식들의 값은 변하지 않는다.
		return # 탐색을 종료한다.
	tree[node] += val # 현재 노드에 저장된 범위에 index가 포함되어 있으므로, 현재 노드에 저장된 값이 val만큼 더해진다.
	if start != end: # 현재 노드가 리프 노드가 아닐 경우, 자식들을 탐색해야 한다.
		mid = (start + end) // 2 # 현재 범위를 반으로 나눈다.
		update(node * 2, start, mid, idx, val) # 왼쪽 자식을 루트로 한 서브 트리에서 탐색을 다시 시작한다.
		update(node * 2 + 1, mid + 1, end, idx, val) # 오른쪽 자식을 루트로 한 서브 트리에서 탐색을 다시 시작한다.

# 구간 합
# node : 현재 노드 번호, [start, end] : 현재 노드에 저장된 합의 범위, [left, right] : 합을 구해야 하는 범위
def query(node, start, end, left, right):
	if right < start or end < left:
		return 0
	if left <= start and end <= right:
		return tree[node]
	mid = (start + end) // 2
	left_sum = query(node * 2, start, mid, left, right) # 왼쪽 자식을 루트로 한 서브 트리에서 탐색을 다시 시작한다.
	right_sum = query(node * 2 + 1, mid + 1, end, left, right); # 오른쪽 자식을 루트로 한 서브 트리에서 탐색을 다시 시작한다.
	return left_sum + right_sum

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 세그먼트 트리는 완전 이진 트리의 구조를 가진다.
# 즉, 노드가 N개가 있다면 높이 H는 ceil(log2(N))가 된다.
# 그러면 세그먼트 트리의 크기는 2^(H+1)-1가 되어야 한다.
M = 2 ** ceil(log2(N) + 1) #  1-based index를 위해 크기를 2^(H+1)로 잡는다.
tree = [0] * M

# 세그먼트 트리 만들기
init(1, 0, N - 1)

for _ in range(Q):
	q = list(map(int, input().split()))
	if q[0] == 1: # 1번 쿼리 (구간 합 쿼리)
		l = q[1] - 1
		r = q[2] - 1
		print(query(1, 0, N - 1, l, r))
	elif q[0] == 2: # 2번 쿼리 (원소 업데이트)
		i = q[1] - 1
		x = q[2]
		update(1, 0, N - 1, i, x) # i번 잡초의 크기가 x만큼 늘어난다.
	else: # 3번 쿼리 (원소 업데이트)
		i = q[1] - 1
		x = q[2]
		update(1, 0, N - 1, i, -x) # i번 잡초의 크기가 x만큼 줄어든다.