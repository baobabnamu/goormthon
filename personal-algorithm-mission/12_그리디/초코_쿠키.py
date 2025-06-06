import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

''' Ai를 Aj보다 x일 더 빨리 먹어야 하는 조건은 다음과 같다.
Ai(Aj-x) >= (Ai-x)Aj
이를 정리하면 Ai <= Aj 가 된다.
A1, ..., AN을 비내림차순으로 정렬하면 결국은 i<j인 모든 (i,j) 쌍에 대해 위 조건을 만족한다고 볼 수 있다. '''

B = [] # (Ai, i) 쌍을 담는다.
for i in range(N):
	B.append((A[i], i + 1))
B.sort() # 결과가 같은 순서가 여러 가지여도, 사전순으로 출력하게 된다.

# 단, 쿠키를 어떤 순서로 먹어도 반드시 곱이 0이 되는 경우가 있다.
# 이때에는 예외처리를 해서 출력은 반드시 1, 2, 3, ..., N으로 출력해야 한다.
for i in range(N):
	if B[i][0] - i <= 0: # i일이 지났을 때의 먹은 쿠키의 맛있는 정도가 0일 때
		for j in range(1, N + 1):
			print(j, end = ' ')
		exit()

for i in range(N):
	print(B[i][1] + 1, end = ' ')