import sys
input = sys.stdin.readline
from bisect import bisect

N = int(input())
S = list(map(int, input().split()))

''' 세 가수의 팬클럽의 영향력을 각각 x, y, z
x + y >= z, x + z >= y, y + z >= x 를 만족해야 한다.
x와 y가 정해진다면, |x - y| <= z <= x + y 를 만족할 수 있는 z를 모두 찾으면 된다.
이는 브루트포스로 시도하면 시간 초과가 발생하고, z를 이분 탐색으로 찾아야 한다. '''

# 이분 탐색을 위해 S를 정렬
S.sort()

# x와 y가 되는 S_i와 S_j를 임의로 정한다.
ans = 0
for i in range(N - 2):
	for j in range(i + 1, N - 1):

		# |S_i - S_j| < S_j <= z <= S_i + S_j를 만족하는 z를 찾아야 한다.
		# S_i + S_j보다 작거나 같은 원소의 최대 인덱스를 찾는다.
		idx = bisect(S, S[i] + S[j]) - 1 # S_i + S_j을 초과하는 최초의 인덱스를 찾아 -1을 해준다.

		# 구간 [j+1, idx] 내에 있는 모든 원소는 z가 될 수 있다.
		ans += idx - j

print(ans)