from stats import count_number_words, count_number_characters, sort_dictionary
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        content_in_file = f.read()
    return content_in_file

def print_characters(item_to_print):
    for item in item_to_print:
        if(item["char"].isalpha()):
            character = item["char"]
            amount = item["num"]
            print(f"{character}: {amount}")

def main():
    if(len(sys.argv) <= 1):
        raise Exception("Usage: python3 main.py <path_to_book>")

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    
    count_words = count_number_words(book_text)

    print("============ BOOKBOT ============ \n" \
        f"Analyzing book found at {sys.argv[1]} \n" \
        "----------- Word Count ----------")
    print(f"Found {count_words} total words")

    # this is where you count and sort the characters in the book before you display it
    count_characters_frankenstein = count_number_characters(book_text)

    sorted_characters_frankenstein = sort_dictionary(count_characters_frankenstein)

    print("--------- Character Count -------")

    print_characters(sorted_characters_frankenstein)

    print("============= END ===============")
    



try:
    main()

except Exception as e:
    print(e)
    sys.exit(1)