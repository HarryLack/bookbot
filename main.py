def get_book_text(path: str):
    with open(path) as f:
        return f.read()


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


def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    chars = count_unique_chars(file_contents)

    chars_list = []

    for c in chars:
        chars_list.append({'char': c, 'count': chars[c]})

    chars_list.sort(reverse=True, key=sort_by)

    print(f"---- {book_path} ----")
    print(f"{word_count} words found")
    for c in chars_list:
        if c["char"].isalpha():
            print(f"The '{c['char']}' character was found {c['count']} times")
    print(f"---- End ----")


main()
