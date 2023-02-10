import string
import unicodedata

def cleanText(string):
    my_string = ""

    with open('character_list.txt') as f:
        array = f.read().splitlines()
        f.close

    # for i in array:
    #     string = string.replace(i,"")

    # my_string = my_string.join(e for e in string if e not in array)

    # my_string = my_string.join(e for e in string if e.isalpha())

    my_string = my_string.join(e for e in string if unicodedata.category(e) == "Lo")

    # for i in my_string:
    #     if i in array:
    #         my_string = my_string.replace(i,"")

    # for i in my_string:
    #     if unicodedata.category(i) != "Lo":
    #         my_string = my_string.replace(i,"")

    return my_string