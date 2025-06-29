import sys
from stats import get_word_count, get_char_count, sort_dictionary


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookpath = sys.argv[1]
    frankenstein = get_book_text(bookpath)
    num_words = get_word_count(frankenstein)
    char_count = get_char_count(frankenstein)
    char_count_list = sort_dictionary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for rec in char_count_list:
        if rec["char"].isalpha():
            print(f"{rec['char']}: {rec['num']}")
    print("============= END ===============")


main()
