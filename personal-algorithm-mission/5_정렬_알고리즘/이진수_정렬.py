def count_binary_one(n):
	count = 0
	while n:
		count += n & 1
		n >>= 1
	return count

N, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(key=lambda x: (count_binary_one(x), x), reverse=True)

print(nums[K - 1])

# 핵심 아이디어
# 1. 이진수에서 1의 개수를 세는 함수를 만든다.
# - AND 연산자(&)를 사용하여 1과 연산(=역할 : 마지막 수에서 1과 1이 만나면 1이 증가됨)하고, 시프트 연산자를 사용해 체크한 마지막 수를 제거함.
# 2. 이진수에서 1의 개수를 기준으로 정렬한다.
# - 이진수에서 1의 개수를 기준으로 정렬하고, 같은 경우 원래 수를 기준으로 정렬함. 이때, 내림차순을 사용함.
# 3. 정렬된 배열에서 K번째 원소를 출력한다.
