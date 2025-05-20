# itertools의 combinations를 사용하여 가능한 모든 조합을 생성
from itertools import combinations

# 입력 받기
N = int(input())  # 문자열의 길이
S = input()       # 분할할 문자열

# 가능한 모든 부분 문자열을 저장할 집합 생성
P = set()

# 문자열을 나눌 수 있는 위치들 생성 (1부터 N-1까지의 인덱스)
blank = [i for i in range(1, N)]
# 2개의 위치를 선택하는 모든 조합 생성
comb = list(combinations(blank, 2))

# 모든 가능한 부분 문자열 생성
for f, s in comb:
    # 문자열을 3등분하여 각 부분을 집합에 추가
    P.add(S[:f])      # 첫 번째 부분 (시작부터 f까지)
    P.add(S[f:s])     # 두 번째 부분 (f부터 s까지)
    P.add(S[s:])      # 세 번째 부분 (s부터 끝까지)

# 부분 문자열들을 사전 순으로 정렬
P = sorted(list(P))

# 최대 점수를 저장할 변수
result = 0

# 모든 가능한 분할 방법에 대해 점수 계산
for f, s in comb:
    temp = 0
    
    # 각 부분 문자열의 사전 순서를 구하여 점수 계산
    temp += P.index(S[:f]) + 1    # 첫 번째 부분의 순서
    temp += P.index(S[f:s]) + 1   # 두 번째 부분의 순서
    temp += P.index(S[s:]) + 1    # 세 번째 부분의 순서
    
    # 최대 점수 업데이트
    result = max(result, temp)

# 결과 출력
print(result)