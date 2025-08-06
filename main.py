from stats import wordCounter

def getBookText(file_path):
    book_contents = ""

    with open(file_path) as f:
        book_contents = f.read()

    return book_contents


def main():
    book_contents = getBookText("./books/frankenstein.txt")
    print(f"{wordCounter(book_contents)} words found in the document")

main()
