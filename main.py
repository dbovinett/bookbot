from stats import word_count
from stats import letter_count
from stats import dict_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
        if (len(sys.argv)) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        file = sys.argv[1]
        text = get_book_text(file)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file}...")
        print("----------- Word Count ----------")
        count = word_count(text)
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        letter_counts = letter_count(text)
        letters_sorted = dict_sort(letter_counts)
        for item in letters_sorted:
            print(f"{item}: {letters_sorted[item]}")
        print("============= END ===============")

    

main()