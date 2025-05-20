N, M, K = map(int, input().split())

# 초기 판다 위치 입력
panda_pos = []  # 빈 리스트로 시작
for i in range(K):
    x, y = map(int, input().split())
    panda_pos.append((x, y))  # 튜플로 위치 저장

# 판다 불만족도 계산
ans = float('inf')

for r in range(1, N + 1):
	for c in range(1, M + 1):
		if (r, c) in panda_pos:
			continue
		
		point = 0
		
		for other_r, other_c in panda_pos:
			point += (r - other_r) ** 2 + (c - other_c) ** 2
			
		ans = min(ans, point)
		
print(ans)