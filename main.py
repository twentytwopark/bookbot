import sys
from stats import get_num_words, get_num_all_chars, sort_on

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py <file_path>')
        sys.exit(1)
    else:  
        filepath = sys.argv[1]
    if filepath:
        book_text = get_book_text(filepath)
        num_words = get_num_words(book_text)
        num_letters = get_num_all_chars(book_text)
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at {filepath}...')
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        print('--------- Character Count -------')
        num_letters = sort_on(num_letters)
        for item in num_letters:
            print(f'{item[0]}: {item[1]}')
        print('============= END ===============')

    # print(f'{num_words} words found in the document')
    # print(f'{num_letters} letters found in the document')
    # print(num_letters.items())

if __name__ == '__main__':
    main()
