def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    nbr = words_nbr(text)
    print(nbr)
    chars_dict = get_chars_dict(text)
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

cpt = 0
def words_nbr(text):
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

main()