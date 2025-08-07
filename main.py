from stats import wordCounter, charCounter, charReport

def getBookText(file_path):
    book_contents = ""

    with open(file_path) as f:
        book_contents = f.read()

    return book_contents

def main():
    book_contents = getBookText("./books/frankenstein.txt")
    incidence_of_letters = charCounter(book_contents)
    
    report_list = charReport(incidence_of_letters)
    report_sub_list = []
    report_string = ""

    for item in report_list:
        report_sub_list.append([item["char"], item["num"]])

    for item in report_sub_list:
        if item[0].isalpha():
            report_string += f"{item[0]}: {item[1]}\n"

    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {wordCounter(book_contents)} total words\n--------- Character Count -------\n{report_string[:-1]}\n============= END ===============")

main()
