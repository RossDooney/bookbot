
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = list(chars_dict.items())
    get_report(book_path, num_words, chars_list)

            

def get_report(book_path, num_words, chars_list):
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document") 

    for char in sorted(chars_list, key=lambda x: x[1], reverse=True):
        if char[0].isalpha():
            print(f"The {char[0]} character was found {char[1]} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()