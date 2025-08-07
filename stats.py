def wordCounter(book_contents):
    single_words = book_contents.split()
    return len(single_words)

def charCounter(book_contents):
    single_chars_dict = {}
    book_contents_lower = book_contents.lower()
    counter = 0
    for character in book_contents_lower:
        
        if character not in single_chars_dict:
            counter = 1
            single_chars_dict[character] = counter
        else:
            single_chars_dict[character] = single_chars_dict[character] + 1
    
    return single_chars_dict

def charReport(single_chars_dict):
    report_list = []
    
    for item in single_chars_dict:
        #print(item," -> ",single_chars_dict[item])
        contents_of_list_dict = {}
        contents_of_list_dict["char"] = item
        contents_of_list_dict["num"] = single_chars_dict[item]
        report_list.append(contents_of_list_dict)
    
    report_list.sort(reverse=True, key=sort_on)

    return report_list

def sort_on(items):
    return items["num"]

