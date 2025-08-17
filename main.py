def get_book_text(filepath):
    with open(filepath) as f:
        content_in_file = f.read()
    return content_in_file


def main():
    filepath = "books/frankenstein.txt"
    print(f"{get_book_text(filepath)}")


main()