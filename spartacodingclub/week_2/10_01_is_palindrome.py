input = "abcba"

def is_palindrome(string):
    count = 0
    while True:
        if string[count] != string[len(string)-count-1]:
            return False
        if count >= len(string)//2:
            break
        count += 1
    return True
print(is_palindrome(input))