"""
Raghav Puri
Intermediate Data Programming
"""
from cse163_utils import normalize_token
import os


class Document:
    '''
    A class representing a document. This document is initialized with a file path,
    and it can load and normalize words, returning their term frequencies
    '''
    def __init__(self, path):
        '''
        Initializes a new Document object. If the given path is not a valid
        file, throws an exception
        '''
        if not os.path.exists(path):
            raise FileNotFoundError("The file at " + path + " does not exist")
        self._path = path
        self._words = self._load_words()

    def _load_words(self):
        '''
        Loads the words, normalizes them, and returns them
        '''
        words = {}
        with open(self._path, 'r', encoding='utf-8') as f:
            for line in f:
                # Split the line into words, normalizes them, and add to the dictionary
                for word in line.split():
                    normalized_word = normalize_token(word)
                    if normalized_word in words:
                        words[normalized_word] += 1
                    else:
                        words[normalized_word] = 1
        return words

    def get_words(self):
        '''
        Returns the list of normalized words in the document
        '''
        return list(self._words.keys())

    def get_path(self):
        '''
        Returns the path of the current document
        '''
        return self._path

    def term_frequency(self, term):
        '''
        Returns the term frequency value for this document
        Term Frequency is equivalent to the number of terms t divided by total number of words in document
        '''
        normalized_term = normalize_token(term)
        if (len(self._words) == 0) or (normalized_term not in self._words):
            return 0
        term_count = self._words[normalized_term]
        # summing all the values instead of caluclating len because of duplicates
        total_words = sum(self._words.values())
        # term frequency calculation
        return term_count / total_words