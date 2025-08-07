def wordCounter(book_contents):
    single_words = book_contents.split()
    return len(single_words)

def charCounter(book_contents):
    single_chars = {}
    book_contents_lower = book_contents.lower()
    counter = 0
    for character in book_contents_lower:
        
        if character not in single_chars:
            counter = 1
            single_chars[character] = counter
        else:
            single_chars[character] = single_chars[character] + 1
    
    return single_chars