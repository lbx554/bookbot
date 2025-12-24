def number_of_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]

def chars(text):
    words = text.lower()
    characters = {}
    for c in words:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters 

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
