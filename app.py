# Interactive dictionary searches a word from loaded dataset and gives its definition to the user.

import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):

    if w.lower() in data:
        print(" ".join(data[w]))
    elif w.capitalize() in data:
        print(" ".join(data[w.title()]))
    elif w.upper() in data:
        print(" ".join(data[w.up]))
    elif len(get_close_matches(w, data.keys())) > 0:
            yn = input("Did you mean {}? Enter Y if Yes, N if No. ".format(get_close_matches(w, data.keys())[0]))
            if yn == "Y":
                ans = data[get_close_matches(w, data.keys())[0]]
                print(" ".join(ans))
            elif yn == "N":
                print("The word doesn't exist in the dictionary. Please, double check it.")
            else:
                print("We didn't understand your query.")
    else:
        print("The word doesn't exist in the dictionary. Please, double check it.")


word = input("Enter word: ")

translate(word)


