import argparse
from pyphonetics import RefinedSoundex
import pronouncing as pr
import random

extras=[",", "!", "?", "."]
def remove_non_words(lst):
    def replace_extras_in_word(word, ext):
        for ex in ext:
            word = word.replace(ex, "")
        return word
    replace=list()
    for (i, word) in zip(range(len(lst)), lst):
        boolean_non_word = [(el in word) for el in extras]
        if True in boolean_non_word:
            non_word = extras[boolean_non_word.index(True)]
            if word.index(non_word) > len(word) * 0.5:
                replace.append((non_word, i))
                lst[i] = replace_extras_in_word(word, extras)
    return (lst, replace)

def modify_sentence(sentence, randomize=False):
    rs = RefinedSoundex()
    phrase = sentence

    split_phrase = phrase.split(" ")
    premod = remove_non_words(split_phrase)
    split_phrase = premod[0]

    
    def find_best_word(words, target):

        min_backup_distance = 5
        backup = target
        for word in words:
            distance = rs.distance(word, target)
            if distance < 1:
                return word
            elif distance < min_backup_distance:
                backup = word
                min_backup_distance = distance
        return backup


    def find_random_word(words, target):
        if len(words) > 0:
            return random.choice(words)
        else:
            return target

    if not randomize:
        sf = [find_best_word(pr.rhymes(word), word) for word in split_phrase]
    else:
        sf = [find_random_word(pr.rhymes(word), word) for word in split_phrase]


    # repair the list using replace / premod[1]

    for non_word in premod[1]:
        sf[non_word[1]] += non_word[0]

    return " ".join(sf)
