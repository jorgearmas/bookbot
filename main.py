from stats import wordCounter, charCounter, charReport
import sys

def getBookText(file_path):
    book_contents = ""

    with open(file_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = getBookText(sys.argv[1])
    incidence_of_letters = charCounter(book_contents)
    
    report_list = charReport(incidence_of_letters)
    report_sub_list = []
    report_string = ""

    for item in report_list:
        report_sub_list.append([item["char"], item["num"]])

    for item in report_sub_list:
        if item[0].isalpha():
            report_string += f"{item[0]}: {item[1]}\n"

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {wordCounter(book_contents)} total words\n--------- Character Count -------\n{report_string[:-1]}\n============= END ===============")

main()
