from random import sample
from collections import defaultdict

class WordsAviable:
    def __init__(self, path: str = "../files/words.txt", min_word_len: int = 4):
        words = [word for word in open(path).read().split("\n") if len(word) >= min_word_len]
        self.ordered_words = defaultdict(set)
        for word in words:
            self.ordered_words[len(word)].add(word)

    def get_one(self, word_size: int, reverted: bool):
        word = sample(self.ordered_words[word_size], 1)[0]
        self.ordered_words[word_size].remove(word)
        return word[::-1] if reverted else word