def count_words(fullwork):
    num_words = 0
    words = fullwork.split()
    for word in words:
        num_words += 1
    return num_words

def count_characters(fullwork):
    num_characters = {}
    characters = list(fullwork.lower())

    for character in characters:
        if character in num_characters:
            num_characters[character] += 1
        else:
            num_characters[character] = 1
    return num_characters

def sorter(initial_dict):
    new_list = []
    for char, num in initial_dict.items():
        new_list.append({"char": char,"num": num})

    def sort_on(items):
        return items["num"]
        
    new_list.sort(reverse=True, key=sort_on)
    return new_list
