input = "abdecedba"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1]) # 계속 작아지는구나...으아

print(is_palindrome(input))