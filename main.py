
def main():
        book_path = 'books/frankenstein.txt'
        text = get_book_text(book_path)
        count = get_num_words(text)
        print(f'{count} is the number of words in the document')
        letter_count = count_letters(text)
        print(letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
     words = text.split()
     return len(words)

def count_letters(text):
    count_dict = {}
    text = text.lower()
    chars = list(text)
    for char in chars:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

main()