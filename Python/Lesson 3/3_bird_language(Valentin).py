VOWELS = "aeiouy"


def translate(text: str) -> str:
    human_phrase = []  # Initialization  list with sorted words
    i = 0
    while i < len(text):
        human_phrase.append(text[i])
        if text[i] in VOWELS:  # If vowels skip 3 symbol
            i += 3
        elif text[i] == ' ':  # Skip space
            i += 1
        else:  # Go to next symbol
            i += 2
    return ''.join(human_phrase)


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
