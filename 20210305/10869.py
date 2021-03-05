# 문제
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
# 예제 입력
# 7 3
# 예제 출력 
# 10
# 4
# 21
# 2  # a/b 가 아니라 a/b의 몫을 나타내라는 의미인 듯
# 1

# 풀이

# a,b를 입력받아 공백으로 구분
a,b = input().split()
# a,b를 숫자로 변환 -> int() str->int 정수로 바꾸는 int(소수)
a = int(a)
b = int(b)
# a,b 연간 결과를 출력
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)