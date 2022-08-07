import json
from py_thesaurus import Thesaurus
import emoji as emoji_pkg



emoji_directory=json.load(open("/home/velo/Documents/Projects/LCS/emoji-directory.json","r"))
# what the fuc k happened here , I dont know
emoji_cat_list = [[emoji for emoji in emoji_directory[emoji_category]] for emoji_category in emoji_directory]
emoji_list = list()
for cat in emoji_cat_list:
    for emoji in cat:
        emoji_list.append(emoji)


phrase="I wou"

def emoji_for_word(word):
    return [e for e in emoji_list if word in e.split("_")]

def obfuscate_with_emojis(words):
    for (word, i) in  zip(words, range(len(words))): 
        tsi = Thesaurus(word)
        emoji_match = emoji_for_word(word)
        emoji_match_tsi = emoji_for_word(str(tsi.get_synonym())) 
        if len(emoji_match) > 0:
            words[i] = f":{emoji_match[0]}:"
        elif len(emoji_match_tsi) > 0:
            words[i] = f":{emoji_match_tsi[0]}:"
    

    return words


stop_switch = {
    "are": "r",
    "you": "u",
    "be": "b",
    "to": "2"
}

def obfuscate_stop_words(words):
    for (word, i) in zip(words, range(len(words))):
        words[i] = stop_switch.get(word.lower(), word)
    return words

# itterate over stages
phrase_ob0 = obfuscate_stop_words(phrase.split(" "))
phrase_ob1 = obfuscate_with_emojis(phrase_ob0)


full_obfuscated_sentence=emoji_pkg.emojize(" ".join(phrase_ob1))

print(full_obfuscated_sentence)
