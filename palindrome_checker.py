def is_palindrome(string):
    string = string.lower().replace(" ", "")
    if string == string[::-1]:
        return True
    else:
        return False
print(is_palindrome('racecar'))
print(is_palindrome('hello'))
print(is_palindrome('A man a plan a canal Panama'))