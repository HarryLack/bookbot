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


def sort_by(dict):
    return dict["count"]


def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for c in chars_dict:
        chars_list.append({'char': c, 'count': chars_dict[c]})
    chars_list.sort(reverse=True, key=sort_by)
    return chars_list
