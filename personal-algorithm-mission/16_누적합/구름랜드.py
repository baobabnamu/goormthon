import sys
input = sys.stdin.readline

N = int(input())
F = list(map(int, input().split()))

# L, R이 주어질 때마다 L <= i <= R인 모든 F_i의 합을 구해야 한다.
# 이는 누적 합 배열로 해결할 수 있다.

# 누적 합 배열 만들기
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
	prefix_sum[i] = prefix_sum[i - 1] + F[i - 1]

# 구간 [L, R]에 대한 합은 prefix_sum[R] - prefix_sum[L - 1]로 구할 수 있다.
# prefix_sum[R] - prefix_sum[L - 1] = (F_1 + ... + F_R) - (F_1 + ... + F_{L-1}) = F_L + ... + F_R
for _ in range(int(input())):
	L, R = map(int, input().split())
	print(prefix_sum[R] - prefix_sum[L - 1])