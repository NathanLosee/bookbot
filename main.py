from stats import get_word_count, get_character_counts, get_sorted_character_counts
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    character_counts = get_character_counts(book_text)
    sorted_character_counts = get_sorted_character_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in sorted_character_counts:
        for char, count in char_count.items():
            if char.isalpha():
                print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    main()