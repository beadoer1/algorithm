# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

# 풀이 : 체스판에 접근 불가한 부분들을 체크하고 재귀식에 보내주려했는데 어려움이 많다. 다른 방법을 찾아봐야겠다.
#       표를 copy 모듈 없이 별도로 만들어보려고했는데 번번이 실패했다.(mutable 객체라 어려운 듯 하다. [:]을 두 번 쓰면 되려나..)
import sys
import copy

def n_queen(step_n,tot_n,tot_count,mat):

    if step_n == tot_n-1:
        for i in range(tot_n):
            if mat[step_n][i] == 0:
                tot_count += 1
        return tot_count
    next_mat = []
    for i in range(tot_n):
        next_mat = copy.deepcopy(mat)  # 이거 말고 방법이 있을거 같은데 ㅠㅠ
        if mat[step_n][i] == 0:
            # Queen 아래 직선 좌표의 값 변경
            for j in range(step_n,tot_n):
                next_mat[j][i] = 1 # 아래 직선
            print('step_n',step_n,'i',i,'straight',next_mat)
            # Queen 왼편 대각선 좌표의 값 변경
            tmp_step = step_n    
            if step_n+i < tot_n: # 좌표는 (step_n,index)  
                for k in range(i,-1,-1): 
                    next_mat[step_n][k] = 1
                    step_n += 1
            else:
                for l in range(step_n,tot_n):
                    index = i
                    next_mat[l][index] = 1
                    index -= 1
            step_n = tmp_step
            print('step_n',step_n,'i',i,'left',next_mat)
            # Queen 오른편 대각선 좌표의 값 변경
            if step_n > i: # 좌표는 (step_n,index)  
                for step in range(step_n,tot_n):
                    index = i
                    next_mat[step][index] = 1
                    index += 1
            else:
                for k in range(i,tot_n): 
                    next_mat[step_n][k] = 1
                    step_n += 1
            step_n = tmp_step
            print('step_n',step_n,'i',i,'right',next_mat)

            # 재귀를 이용하여 다음단계 탐색
            tot_count += n_queen(step_n+1,tot_n,tot_count,next_mat)
            print('tot_count',tot_count,'if end',next_mat)
    return tot_count        

            
num = int(sys.stdin.readline())

matrix = []

for i in range(num):
    matrix.append([0] * (num))
matrix2 = matrix.copy()
step_num = 0
tot_num = num
tot_count = 0
print(n_queen(0,tot_num,0,matrix))
print(matrix)
print(matrix2)


