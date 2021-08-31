def is_palindrome(string: str) -> bool:
    return string == string[::-1]


if __name__ == '__main__':
    print(is_palindrome("abba"))  # true
    print(is_palindrome("abcba"))  # true
    print(is_palindrome("abca"))  # false
