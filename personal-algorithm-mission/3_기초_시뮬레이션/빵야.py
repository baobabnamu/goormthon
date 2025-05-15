import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))

ans = 0 # 정답
ct = 0 # 권총이 발사된 횟수

for i in range(N):

	# 권총이 주는 피해가 1이 될 때까지 그리고 적의 체력이 남아있는 동안 권총을 발사한다.
	while ct and H[i] > 0:
		H[i] -= ct + 1
		ct = (ct + 1) % 4
		ans += 1

	# 적이 쓰러졌다면 넘어간다.
	if H[i] <= 0:
		continue

	# 1,2,3,4 총 네 번의 발사가 반복되는 것을 한 번에 계산한다.
	q, H[i] = divmod(H[i], 10)
	ans += q * 4

	# 적이 쓰러지지 않았다면 체력은 10 미만이므로, 적의 체력이 남아있는 동안 권총을 발사한다.
	while H[i] > 0:
		H[i] -= ct + 1
		ct = (ct + 1) % 4
		ans += 1

print(ans)

# 핵심 아이디어
# 해당 문제에서는 4번(1,2,3,4)의 발사를 통해 10의 피해를 주므로 10의 배수로 나누어 몇 번의 발사가 필요한지 알 수 있다.
# 체력이 10 미만이면 적의 체력이 남아있는 동안 권총을 발사한다.