from random import sample, choice, randint

from word_hunt_builder.modules.map import WordHuntMap
from word_hunt_builder.modules.words import WordsAviable

length, heigth, qtd_words, min_word_len = 10, 10, 2, 4

whm = WordHuntMap(length, heigth)
wa = WordsAviable()


start_heigth, start_length = randint(0, heigth),  randint(0, length)
orientation, reverted = choice("hvdi"), choice([True, False])

orientation = 'h'
if orientation == 'h':
    start_length = start_length - max((min_word_len - (length - start_length)), 0)
    heigth, end_length = start_heigth, start_length + randint(min_word_len, length - start_length)
    word = wa.get_one(end_length-start_length, reverted)

    current_length_posix = start_length
    for letter in word:
        whm.insert_letter(heigth, current_length_posix, letter)
        current_length_posix += 1
        

print(whm)
