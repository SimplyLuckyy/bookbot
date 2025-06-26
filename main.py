
from stats import count_words
from stats import count_characters
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    count_words(get_book_text("books/frankenstein.txt"))
    sorted_list(count_characters(get_book_text("books/frankenstein.txt")))

    

main()