import spacy
from spacy_syllables import SpacySyllables

def get_words_as_list():
    with open('wordlist.10000.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words

def get_syllables(word):
    # code from spacy syllables website
    # determine the syllables of a word is very hard, so this results in imperfect results
    # however the results should be good enough for this project
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("syllables", after="tagger")
    assert nlp.pipe_names == ["tok2vec", "tagger", "syllables", "parser", "attribute_ruler", "lemmatizer", "ner"]
    doc = nlp(word)
    data = [(token.text, token._.syllables, token._.syllables_count) for token in doc]
    print(data[0][1])

if __name__ == '__main__':
    get_syllables("accomplish")
