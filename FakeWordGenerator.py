import spacy
from spacy_syllables import SpacySyllables
from WeightedDirectedGraph import *
import random
import json

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
    print(word)
    syllables = get_syllables(word)

    # indicate start
    graph.increment_edge_weight("*", syllables[0])

    for i in range(0, len(syllables) - 1):
        graph.increment_edge_weight(syllables[i], syllables[i + 1])

    # indicate end
    graph.increment_edge_weight(syllables[-1], ".")

# traverses the graph by following a single edge using a weighted random decision
def take_random_step(graph, start):
    keys, weights = zip(*graph.adj_matrix[start].items())
    return random.choices(keys, weights=weights)[0]

# creating the graph takes a lot of time, so we save it in memory for the future
def create_and_save_graph():
    english_words = get_words_as_list()[:20]
    graph = WeightedDirectedGraph()

    for word in english_words:
        update_weights(graph, word)

    # save to a JSON file
    with open('syllable_graph.json', 'w') as f:
        json.dump(graph.adj_matrix, f)

def generate_random_word():
    with open('syllable_graph.json', 'r') as f:
        syllable_graph = json.load(f)

    graph = WeightedDirectedGraph()
    graph.adj_matrix = syllable_graph

    random_word = ""
    syllable = "*"
    while syllable != ".":
        if syllable != "*":
            random_word += syllable
        syllable = take_random_step(graph, syllable)


    print(random_word)
    return random_word

if __name__ == '__main__':
    create_and_save_graph()

