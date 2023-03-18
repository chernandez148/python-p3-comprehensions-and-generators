#!/usr/bin/env python3

def return_evens(num_list):
    return [n for n in num_list if n%2 == 0]

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]


# def make_exclamation(sentence_list):
#     every_word = [(words + "!") for words in sentence_list]
#     return every_word
# make_exclamation(["I like computers", "I require coffee", "Live long and prosper"])
