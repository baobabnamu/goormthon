N, M, x = map(int, input().split())
H = list(map(int, input().split()))
Q = int(input())
D = input().split()

x -= 1 # 0-based index
ans = 0
for i in range(Q):

	# 1. 벌목할 수 있으면 벌목
	if H[x] + i >= M: # 나무의 높이는 i만큼 자랐다.
		ans += H[x] + i
		H[x] -= H[x] + i

	# 2. 움직이기
	if D[i] == 'L':
		x = (x - 1) % N
	elif D[i] == 'R':
		x = (x + 1) % N

	# 나무들의 높이가 1씩 자라는 것은 i로 생각하면 된다.

print(ans)