import re

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

def count_char(text):
    words = re.split(r"(\s+)", text)
    data_dict = {}
    
    for word in words:
        word = word.lower()
        counter = 0
        for character in word:
            if character in data_dict:
                counter = data_dict[character]
                counter += 1
                data_dict[character] = counter
            else:
                counter = 1
                data_dict[character] = counter
    
    return data_dict

def report(dictionary):        
    for k, v in dictionary.items():
        if k != ' ' and k != '.' and k != '#':
            print(f"The '{k}' character was found {v} times")

if __name__ == "__main__":
    text = main()
    count_words(text)
    dictionary = count_char(text)
    report(dictionary)