import unicodedata

def cleanText(my_string):

    new_string = ""
    new_string = new_string.join(e for e in my_string if unicodedata.category(e) == "Lo" or e == 'ー')

    return new_string
