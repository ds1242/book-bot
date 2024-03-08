
def main():
        book_path = 'books/frankenstein.txt'
        text = get_book_text(book_path)
        count = get_num_words(text)
        print(f'{count} is the number of words in the document')
        letter_count = count_letters(text)
        converted = convert_dict(letter_count)
        converted.sort(key=sort_on)
        print(converted)


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

def convert_dict(dict):
     outputList = [{"letter": key, "num":value} for key, value in dict.items()]
     return outputList

def sort_on(dict):
     return dict['letter']


main()