import sys
from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import dict_sort


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    counted_words = count_words(book_text)
    counted_chars = count_chars(book_text)
    sorted_dict = dict_sort(counted_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")

    for pair in sorted_dict:
        if pair['char'].isalpha() == True:
            print(f"{pair['char']}: {pair['count']}")
        else:
            continue

    print("============= END ===============")


main()
