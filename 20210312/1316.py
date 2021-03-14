# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 풀이 1 : 동적계획법으로 풀면 좋을 것 같다.
import sys

def check_group_word(word_check):
    already_did = []
    current_char = ''
    for char in word_check:
        if char == current_char:
            continue
        else:
            if char in already_did:
                return False
            else:
                current_char = char
                already_did.append(char)
    return True

num_tot_word = int(sys.stdin.readline())
words_list = []
for i in range(num_tot_word):
    word = sys.stdin.readline()
    words_list.append(word)
count = 0
for word in words_list:
    if check_group_word(word):
        count += 1
print(count)

# 풀이 2 : 타인의 답변(정찬엽)
# loop = int(input())
# count = loop 
# for x in range(loop):
#     word = input() 
#     for y in range(len(word) - 1):
#         if word[y] != word[y+1]:
#             if word[y] in word[y+1:]:
#                 count -= 1
#                 break
# print(count)