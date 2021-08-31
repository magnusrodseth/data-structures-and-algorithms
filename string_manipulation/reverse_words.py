def reverse_words(words: str) -> str:
    """
    Reverse the order of words in a sentence
    :param words:
    :return:
    """
    split = words.split(" ")

    reversed = []

    for i in range(len(split) - 1, -1, -1):
        reversed.append(split[i])

    return " ".join(reversed)


if __name__ == "__main__":
    print(reverse_words("Trees are beautiful"))
