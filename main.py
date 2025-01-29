def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    
    return file_contents

def count_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    
    print(counter)

if __name__ == "__main__":
    text = main()
    count_words(text)