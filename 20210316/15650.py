# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 풀이
import sys
# 1,3 -> 2,4 -> 3,5 -> 4,6 -> 5,7 -> 6,8
def back_track(_str,start_num,max_num,n):   # str은 결과 출력, n은 재귀 종료 조건을 만들기 위함
    if  max_num == n:                       # 재귀 종료 조건
        for i in range(start_num,max_num+1):
            print(_str+str(i))
        return    

    tmp = _str
    print(tmp)
    for i in range(start_num,(max_num)+1):  # 수열의 첫 번째 수를 결정
        _str = _str + str(i) + ' '
        back_track(_str,i+1,max_num+1,n)    # 수열의 다음 번째 수를 결정하기 위한 재귀
        _str = tmp
        print(_str)
    return

N,M = map(int,sys.stdin.readline().split())
max_possible_num = N-M+1
back_track('',1,max_possible_num,N)

        

        
