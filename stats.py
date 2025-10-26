def get_word_count(book_contents):
    words = book_contents.split()
    return len(words)
    
def char_count(book_contents):
    low_rida = book_contents.lower()
    
    char_count = {}
    for char in low_rida:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count