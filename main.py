
def main():
        book_path = 'books/frankenstein.txt'
        text = get_book_text(book_path)
        count = get_num_words(text)
        print(f'{count} is the number of words in the document')


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
     words = text.split()
     return len(words)

main()