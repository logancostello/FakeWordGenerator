import spacy
from spacy_syllables import SpacySyllables
from WeightedDirectedGraph import *
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
    return data[0][1]

def update_weights(graph, word):
    syllables = get_syllables(word)

    # indicate start
    graph.increment_edge_weight("*", syllables[0])

    for i in range(0, len(syllables) - 1):
        graph.increment_edge_weight(syllables[i], syllables[i + 1])

    # indicate end
    graph.increment_edge_weight(syllables[-1], ".")


if __name__ == '__main__':
    graph = WeightedDirectedGraph()
    update_weights(graph, "alphabet")
    print(graph)
