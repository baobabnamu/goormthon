import sys
input = sys.stdin.readline

# 에라토스테네스의 체 O(K log log K)
def sieve():
    # 100,000의 제곱근까지만 확인한다.
    for i in range(2, int(100000 ** 0.5) + 1):
        if is_prime[i]: # i가 소수라면, i의 모든 배수들은 소수가 아니다.
            for j in range(i ** 2, 100001, i): # i의 제곱 전까지는 이미 처리가 된 상태이다.
                is_prime[j] = False

N = int(input())
A = [int(input()) for _ in range(N)]

# 판타스틱한 갑옷은 결국 소수인 점수를 가지고 있어야 한다.
is_prime = [True] * 100001
sieve()
for i in range(N):
    if is_prime[A[i]]:
        print('Yes')
    else:
        print('No')

# 핵심 아이디어
# 1. 에라토스테네스의 핵심은 소수의 배수는 소수가 아니라는 점을 이용한다.
# 2. 소수의 배수를 체크하는 것은 소수의 제곱부터 시작하면 된다.

# 여러 수를 판별해야 하고 범위가 작다(~10^6) → 에라토스테네스의 체
# 큰 수 하나를 판별하거나 메모리 제약 있음 → 소수 판정 알고리즘