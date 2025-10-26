from stats import get_word_count
from stats import char_count
from stats import sort_chars
import sys

def main():
    path = ""
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    
    book_contents = get_book_text(path)
    word_count = get_word_count(book_contents)
    char_count_dick = char_count(book_contents)
    sorted_dick = sort_chars(char_count_dick)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dick in sorted_dick:
        if dick['char'].isalpha():
            print(f"{dick['char']}: {dick['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()
