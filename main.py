from stats import get_num_words,get_character_count
import sys

def sort_on(items):
    return items["num"]
print("============ BOOKBOT ============")
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]
print(f"Analyzing book found at {path_to_file}...")
num_words = get_num_words(path_to_file)
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
char_count = get_character_count(path_to_file)
print("--------- Character Count -------")
char_count.sort(reverse=True,key=sort_on)
for i in char_count:
    print(f'{i["char"]}: {i["num"]}')
