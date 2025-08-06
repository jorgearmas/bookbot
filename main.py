def getBookText(file_path):
    book_contents = ""

    with open(file_path) as f:
        book_contents = f.read()

    return book_contents

def wordCounter(book_contents):
    single_words = book_contents.split()
    return len(single_words)


def main():
    book_contents = getBookText("./books/frankenstein.txt")
    print(f"{wordCounter(book_contents)} words found in the document")

main()
