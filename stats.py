def count_words(fullwork):
    num_words = 0
    words = fullwork.split()
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")

def count_characters(fullwork):
    num_characters = {}
    characters = list(fullwork.lower())

    for character in characters:
        if character in num_characters:
            num_characters[character] += 1
        else:
            num_characters[character] = 1
    print(num_characters)

