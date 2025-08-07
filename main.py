from stats import wordCounter, charCounter

def getBookText(file_path):
    book_contents = ""

    with open(file_path) as f:
        book_contents = f.read()

    return book_contents


def main():
    book_contents = getBookText("./books/frankenstein.txt")
    print(f"{wordCounter(book_contents)} words found in the document")
    incidence_of_letters = charCounter(book_contents)
    print(f"{incidence_of_letters}")

main()
