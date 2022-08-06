import argparse
from pyphonetics import RefinedSoundex
import pronouncing as pr

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-m', '--message')

args = parser.parse_args()



def modify_sentence(sentence):
    rs = RefinedSoundex()
    phrase = sentence

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

    sf = [find_best_word(pr.rhymes(word), word) for word in phrase.split(" ")]
    return " ".join(sf)

print(modify_sentence(args.message))


