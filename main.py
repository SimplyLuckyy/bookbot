
from stats import count_words
from stats import count_characters
from stats import sorter
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        word_count = count_words(get_book_text(sys.argv[1]))
        sorted_list = sorter(count_characters(get_book_text(sys.argv[1])))
        text_one = f"""
        ============ BOOKBOT ============
        Analyzing book found at {sys.argv[1]}...
        ----------- Word Count ----------
        Found {word_count} total words
        --------- Character Count -------"""
        
        print(text_one)
        for i in range(0, len(sorted_list)):
            if sorted_list[i]["char"].isalpha():
                print(f"{sorted_list[i]["char"]}: {sorted_list[i]["num"]}")
        print("============= END ===============")

main()