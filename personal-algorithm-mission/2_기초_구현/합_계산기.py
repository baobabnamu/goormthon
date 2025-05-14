# 계산하는 함수 반환
def calc(expr):
	tokens = expr.split()
	a = int(tokens[0])
	op = tokens[1]
	b = int(tokens[2])
	
	if op == '+': return a + b
	elif op == '-': return a - b
	elif op == '*': return a * b
	elif op == '/': return a // b

# 계산 결과 누적 변수
sum = 0
		
T = int(input())
for _ in range(T):
	sum += calc(input())

print(sum)