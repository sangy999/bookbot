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
    
def restructure_dick(dick):
    return [{'char': k, 'num': v} for k, v in dick.items()]
    
def sort_on(items):
    return items["num"]

def sort_chars(dick):
    restructured_dick = restructure_dick(dick)
    restructured_dick.sort(reverse=True, key=sort_on) 
    return restructured_dick 