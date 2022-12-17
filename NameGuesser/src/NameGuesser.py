from collections import defaultdict
from pandas import read_csv


class TrieNode:
    def __init__(self, c='#'):
        self.c = c
        self.children = {}
        self.word = None


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.add_words(words)

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children.keys():
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.word = word

    def add_words(self, words):
        for word in words:
            if isinstance(word, str):
                self.add_word(word)

    def search_pattern(self, node, i, word, result):
        node = self.root if node is None else node
        while i < len(word):
            ch = word[i]
            if ch == '*':
                for child in node.children:
                    self.search_pattern(node.children[child], i + 1, word, result)
            if ch not in node.children:
                break
            node = node.children[ch]
            i += 1
        if node.word is not None and len(node.word) == len(word):
            result.add(node.word)


class NameGuesser:
    def __init__(self):
        # Read name data from CSV file
        name_dataset = read_csv('../Indian_Names.csv')
        # Drop empty value records
        name_dataset.dropna(inplace=True)
        # Store all the names in a set to avoid duplicates if any
        firstname_set = set(name_dataset["Name"].tolist())
        # Create trie for the name set
        firstname_trie = Trie(firstname_set)

        while True:
            print("========================================================")
            print("                      Name Guesser                      ")
            print("========================================================")
            print(" Enter a pattern for names to search in the format a*b**d where * represents the missing alphabets.")
            pattern = input(" Input pattern (enter 'q/Q' to quit) : ")
            if pattern == "q" or pattern == "Q":
                print(" Quitting program.")
                break
            print(f" Following names found matching the patter {pattern} : ")
            result = set()
            firstname_trie.search_pattern(None, 0, pattern, result)
            for i, val in enumerate(result):
                print(i + 1, val)


# Main executor
if __name__ == "__main__":
    name_guesser = NameGuesser()
