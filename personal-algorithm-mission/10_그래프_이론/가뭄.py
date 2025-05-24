import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	N, M = map(int, input().split())
	edges = [tuple(map(int, input().split())) for _ in range(M)]

	''' 모든 지점은 수로를 통해 서로 연결됨이 보장되어 있다.
	최소 개수의 정비된 수로만을 통해 서로 연결되게 하려면 트리 형태를 이루어야 하고
	트리는 (정점의 개수) -(간선의 개수) = 1을 만족한다.
	즉, 주어진 (정점의 개수) - 1개만큼 수로를 선택해 정비하면 된다. '''
	print(N - 1)