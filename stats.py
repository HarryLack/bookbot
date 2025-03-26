def count_words(text: str):
    words = text.split()
    return len(words)


def count_unique_chars(text: str):
    chars = {}
    lowered = text.lower()
    for c in lowered:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars