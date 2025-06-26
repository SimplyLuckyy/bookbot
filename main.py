
from stats import count_words
from stats import count_characters
from stats import sorter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = count_words(get_book_text("books/frankenstein.txt"))
    sorted_list = sorter(count_characters(get_book_text("books/frankenstein.txt")))
    text_one = f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------"""
    print(text_one)
    for i in range(0, len(sorted_list)):
        if sorted_list[i]["char"].isalpha():
            print(f"{sorted_list[i]["char"]}: {sorted_list[i]["num"]}")
    print("============= END ===============")

main()