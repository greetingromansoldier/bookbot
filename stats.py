
def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words (text_input):
    text = text_input.split()
    num_words = len(text)
    return num_words

def count_chars (text_input):
    words = text_input.split()
    chars_dict = {}
    for word in words:
        word = word.lower()
        # use list() method to split word into characters
        chars_in_word = list(word)
        for char in chars_in_word:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1

    return chars_dict

def dict_sort (chars_dict):
    def sort_on (dict):
        return dict["count"]

    chars_dict = [{"char": char, "count": count} for char, count in chars_dict.items()]
    chars_dict.sort(reverse=True, key=sort_on) # interesting that we don't provide here sort_on as we would for a standard function
    return chars_dict
