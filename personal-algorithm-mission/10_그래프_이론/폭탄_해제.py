import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# A, B : 전선마다 연결된 두 기폭장치의 번호를 관리
# ind : 각 기폭장치에 연결된 전선의 개수를 관리
A = []
B = []
ind = [0] * N

# 정점마다 차수를 계산한다
for _ in range(M):
	Ai, Bi = map(int, input().split())
	Ai -= 1; Bi -= 1
	A.append(Ai)
	B.append(Bi)
	ind[Ai] += 1; ind[Bi] += 1

# 간선의 양 끝 정점의 차수가 하나라도 1이면 그 간선은 끊지 못한다.
least_one = False
for i in range(M):
	if ind[A[i]] == 1 or ind[B[i]] == 1:
		continue
	least_one = True
	print(i + 1, end = ' ')

if not least_one:
	print(-1)