from stats import get_word_count
from stats import char_count

def main():
    path = "books/frankenstein.txt"
    book_contents = get_book_text(path)
    word_count = get_word_count(book_contents)
    
    print_word_count = f"Found {word_count} total words"
    print(print_word_count)
    
    chars = char_count(book_contents)
    print(chars)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()
