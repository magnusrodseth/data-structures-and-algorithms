def is_anagram(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False

    first = sorted(first)
    second = sorted(second)

    for i in range(len(first)):
        if first[i] != second[i]:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram("abcd", "adbc"))  # true
    print(is_anagram("abcd", "cadb"))  # true
    print(is_anagram("abcd", "abcd"))  # true
    print(is_anagram("abcd", "abce"))  # false
