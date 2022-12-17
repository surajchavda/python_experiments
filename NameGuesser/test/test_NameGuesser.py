from unittest import TestCase

from pandas import read_csv

from src.NameGuesser import Trie


class TestTrie(TestCase):
    def test_search_pattern(self):
        # Read name data from CSV file
        name_dataset = read_csv('../resources/Indian_Names.csv')
        # Drop empty value records
        name_dataset.dropna(inplace=True)
        # Store all the names in a set to avoid duplicates if any
        firstname_set = set(name_dataset["Name"].tolist())
        # Create trie for the name set
        firstname_trie = Trie(firstname_set)
        result = set()
        firstname_trie.search_pattern(None, 0, "su*aj", result)
        self.assertEqual(result, set(['suraj']))
        result = set()
        firstname_trie.search_pattern(None, 0, "ni**sh", result)
        self.assertEqual(result, set(['nitish', 'nitesh', 'nilesh', 'nimesh']))
