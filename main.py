from stats import count_number_words, count_number_characters


def get_book_text(filepath):
    with open(filepath) as f:
        content_in_file = f.read()
    return content_in_file

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary_to_sort):
    sorting_dictionary = []
    
    for item in dictionary_to_sort:
        sorting_dictionary.append({"char": item, "num": dictionary_to_sort[item]})

    
    sorting_dictionary.sort(reverse=True, key=sort_on)

    return sorting_dictionary

def print_characters(item_to_print):
    for item in item_to_print:
        if(item["char"].isalpha()):
            character = item["char"]
            amount = item["num"]
            print(f"{character}: {amount}")



def main():
    filepath_frankenstein = "books/frankenstein.txt"

    book_text_frankenstein = get_book_text(filepath_frankenstein)
    
    count_words_frankenstein = count_number_words(book_text_frankenstein)

    print("============ BOOKBOT ============ \n" \
        "Analyzing book found at books/frankenstein.txt... \n" \
        "----------- Word Count ----------")
    print(f"Found {count_words_frankenstein} total words")

    # this is where you count and sort the characters in the book before you display it
    count_characters_frankenstein = count_number_characters(book_text_frankenstein)

    sorted_characters_frankenstein = sort_dictionary(count_characters_frankenstein)

    print("--------- Character Count -------")

    print_characters(sorted_characters_frankenstein)

    print("============= END ===============")
    




main()