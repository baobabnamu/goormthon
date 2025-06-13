import sys
input = sys.stdin.readline
from math import inf

N, S = input().split()
N = int(N)

# 업데이트가 없는 배열에서 구간 처리를 하는 문제는 누적 합을 사용해야 한다.
# 알파벳 소문자마다 개수를 누적하는 누적 합 배열을 만든다.
prefix_sum = [[0] * 26 for _ in range(N + 1)]
for i in range(1, N + 1):
	prefix_sum[i][ord(S[i - 1]) - 97] += 1 # // a-z는 97~122의 값을 가진다. 또한, 누적 합 배열을 위해 1-based index로 개수를 저장한다.
	for j in range(26): # 누적 합 배열을 채운다.
		prefix_sum[i][j] += prefix_sum[i - 1][j]

Q = int(input())
for _ in range(Q):
	l, r, M, T = input().split()
	l = int(l); r = int(r); M = int(M)

	# T에서 소문자마다 개수를 센다.
	ct = [0] * 26
	for i in range(M):
		ct[ord(T[i]) - 97] += 1

	# a부터 차례대로 필요한 소문자라면, 구간 [l, r]에 포함된 개수를 필요한 개수를 나누면 그 소문자에 대한 만들 수 있는 개수가 된다.
	# 그 개수의 최솟값이 만들 수 있는 도장의 개수가 된다.
	ans = inf
	for i in range(26):
		if ct[i]:
			ans = min(ans, (prefix_sum[r][i] - prefix_sum[l - 1][i]) // ct[i])

	print(ans)