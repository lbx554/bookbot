"""def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
main()

def numbers():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        counter = 0
        for w in words:
            counter+=1
        #print(counter)
        return counter
        return len(words)
nums = numbers()"""

def sort_on(dict):
    return dict["num"]

def chars():
    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()
        word_count = len(words)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

        list_of_chars = []
        characters = {}

        for c in words:
            if c in list_of_chars:
                characters[c] += 1
            else:
                list_of_chars.append(c)
                characters[c] = 1

        list_of_dict = []
        for a in list_of_chars:
            if a.isalpha():
                list_of_dict.append({"char": a, "num": characters[a]})

        list_of_dict.sort(reverse=True, key=sort_on)

        for b in list_of_dict:
            print(f"The '{b.get("char")}' character was found {b.get("num")} times")
    print()
    print("--- End report ---")

chars()