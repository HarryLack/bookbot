from stats import count_unique_chars, count_words


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def sort_by(dict):
    return dict["count"]


def main():
    print("greetings boots")
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    chars = count_unique_chars(file_contents)

    chars_list = []

    for c in chars:
        chars_list.append({'char': c, 'count': chars[c]})

    chars_list.sort(reverse=True, key=sort_by)

    print(f"---- {book_path} ----")
    print(f"{word_count} words found in the document")
    for c in chars_list:
        if c["char"].isalpha():
            print(f"The '{c['char']}' character was found {c['count']} times")
    print(f"---- End ----")


main()
