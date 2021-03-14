# 문제
# 2차원 평면 위의 점 N개가 주어진다. 
# 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
# (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
# 입력     출력
# 5       1 -1
# 0 4     1 2
# 1 2     2 2
# 1 -1    3 3
# 2 2     0 4
# 3 3

# 풀이 1: 성공~!..4800ms
# import sys
# num = int(input())
# li_check = []
# for i in range(num):
#     x,y = map(int, input().split())
#     li_check.append([y,x])
# li_check.sort()
# for xy in li_check:
#     print(xy[1],xy[0])

# 풀이 2: input() 대신 sys.stdin.readline() 를 사용 속도가 10배는 빨라진다..440ms
import sys
num = int(sys.stdin.readline())
li_check = []
for i in range(num):
    x,y = map(int, sys.stdin.readline().split())
    li_check.append([y,x])
li_check.sort()
for xy in li_check:
    print(xy[1],xy[0])

# 풀이 2: 타인의 시선 lamda 식 사용
# import sys

# n = int(sys.stdin.readline())
# array = []

# for _ in range(n):
#     array.append(list(map(int, sys.stdin.readline().split())))

# array.sort(key=lambda x: (x[1], x[0]))

# for a in array:
#     print(a[0], a[1])