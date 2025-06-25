
from stats import count_words
from stats import count_characters 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    count_words(get_book_text("books/frankenstein.txt"))
    count_characters(get_book_text("books/frankenstein.txt"))

main()