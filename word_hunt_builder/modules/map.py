from random import choice
from string import ascii_lowercase

class WordHuntMap:
    def __init__(self, length: int, heigth: int):
        self.word_hunt_map = list()
        for _ in range(heigth):
            word_hunt_map_line = list()
            for _ in range(length):
                word_hunt_map_line.append(choice(ascii_lowercase))
            self.word_hunt_map.append(word_hunt_map_line)
    
    def insert_letter(self, line: int, column: int, letter: str):
        self.word_hunt_map[line][column] = letter

    def __str__(self):
        return '\n'.join([' '.join(line) for line in self.word_hunt_map])