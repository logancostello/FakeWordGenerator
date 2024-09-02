def get_words_as_list():
    with open('wordlist.10000.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words


if __name__ == '__main__':
    print(get_words_as_list())
