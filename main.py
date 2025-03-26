from stats import chars_dict_to_sorted_list, count_unique_chars, count_words


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


def main():
    print("greetings boots")
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    chars = count_unique_chars(file_contents)

    chars_list = chars_dict_to_sorted_list(chars)

    print(f"---- {book_path} ----")
    print(f"Found {word_count} total words")
    for c in chars_list:
        if c["char"].isalpha():
            print(f"{c['char']}: {c['count']}")
    print(f"---- End ----")


main()
