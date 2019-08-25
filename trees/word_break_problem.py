from typing import Dict
import copy


class Trie:
    def __init__(self, is_leaf=False) -> None:
        self.is_leaf: bool = is_leaf
        self.children: Dict[Trie] = {}

    def insert(self, word):
        if len(word) > 0:
            child = self.children.get(word[0], Trie())
            self.children[word[0]] = child
            if len(word) == 1:
                child.is_leaf = True
            else:
                child.insert(word[1:])

    def search(self, word):
        if len(word) == 0 and self.is_leaf:
            return True

        if len(word) == 0:
            return False

        child = self.children.get(word[0])

        if not child:
            return False

        return child.search(word[1:])


calculated_breaks = {}


def get_all_breaks(trie, suffix):
    current_breaks = []
    for i in range(len(suffix) + 1):
        if trie.search(suffix[0:i]):
            if i == len(suffix):
                current_breaks.append([suffix[0:i]])
            else:
                breaks = copy.deepcopy(calculated_breaks.get(suffix[i:]))
                if not breaks:
                    breaks = get_all_breaks(trie, suffix[i:])
                for word_break in breaks:
                    word_break.append(suffix[0:i])
                current_breaks += breaks
    calculated_breaks[suffix] = [el.copy() for el in current_breaks]
    return current_breaks


def get_all_breaks_simple(trie, suffix):
    current_breaks = []
    for i in range(len(suffix) + 1):
        if trie.search(suffix[0:i]):
            if i == len(suffix):
                current_breaks.append([suffix[0:i]])
            else:
                breaks = get_all_breaks_simple(trie, suffix[i:])
                for word_break in breaks:
                    word_break.append(suffix[0:i])
                current_breaks += breaks

    return current_breaks


if __name__ == '__main__':
    words = ["this", "th", "is", "famous", "word", "break", "b", "r",
             "e", "a", "k", "br", "bre", "brea", "ak", "prob", "lem"]

    sentence = "wordbreakproblem"

    trie = Trie()
    for w in words:
        trie.insert(w)

    # for w in words + ["not", "there"]:
    #     print(trie.search(w))

    suffix_done = [False for _ in range(len(sentence))]
    result = [list(reversed(el)) for el in get_all_breaks_simple(trie, sentence)]
    print(len(result))
    print(result)
