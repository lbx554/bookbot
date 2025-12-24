import sys

from stats import number_of_words, chars, chars_dict_to_sorted_list

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    num_chars = chars(text)
    num_chars_sorted = chars_dict_to_sorted_list(num_chars)
    print_report(book_path, num_words, num_chars_sorted)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, num_chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in num_chars_sorted:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")

    print("============= END ===============")

main()

