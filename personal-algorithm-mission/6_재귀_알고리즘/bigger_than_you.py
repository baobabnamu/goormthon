import sys
input = sys.stdin.readline
from math import inf

# A의 원소로 이루어져 있으며 K보다 큰, 최솟값 찾기
def solve(now):
	if now > K: # 현재 숫자가 K보다 크다면 더이상 진행할 이유가 없다. 정답을 갱신하고 중단
		global ans
		ans = min(ans, now)
		return
	for i in range(N):
		nxt = now * 10 + A[i] # 다음 숫자를 구한다.
		if not nxt: # 다음 숫자가 0이 되는 경우가 있을 수 있다. 이때, 예외 처리를 하지 않으면 무한 루프에 걸린다.
			continue
		solve(nxt)

N = int(input())
A = list(map(int, input().split()))
K = int(input())

ans = inf # 초기 정답 값은 무한대로 잡는다.
solve(0)
print(ans)

# 핵심 아이디어
# 재귀를 사용하여 모든 가능한 조합을 탐색
# now * 10 + A[i]로 숫자를 이어붙임

# 실행 과정
# solve(0)
#   → 0 * 10 + 1 = 1
#     → 1 * 10 + 1 = 11
#     → 1 * 10 + 2 = 12
#     → 1 * 10 + 3 = 13
#   → 0 * 10 + 2 = 2
#     → 2 * 10 + 1 = 21
#     → 2 * 10 + 2 = 22
#     → 2 * 10 + 3 = 23
#   → 0 * 10 + 3 = 3
#     → 3 * 10 + 1 = 31
#     → 3 * 10 + 2 = 32
#     → 3 * 10 + 3 = 33

# K보다 큰 수를 찾으면 즉시 정답 갱신
# 0이 되는 경우는 건너뛰어 무한 루프 방지