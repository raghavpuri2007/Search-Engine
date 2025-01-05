"""
Raghav Puri
Intermediate Data Programming
"""
import math
import os
from document import Document
from cse163_utils import normalize_token, normalize_paths


class SearchEngine:
    '''
    Search Engine class that indexes text files from a directory
    '''

    def __init__(self, path):
        '''
        Initalizes the SearchEngine with a path to a directory containing text files
        '''
        self._inverted = {}  # Maps terms to document paths that contain terms
        self._documents = {}  # Storage of Document Objects

        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            self._index_file(file_path)

    def _index_file(self, file_path):
        '''
        Indexes a single file and updates the inverted index and dictionary of documents
        '''
        normalized_path = normalize_paths(file_path)
        # normalizes the path and adds to document field
        if normalized_path not in self._documents:
            self._documents[normalized_path] = Document(normalized_path)

        document = self._documents[normalized_path]
        unique_words = document.get_words()
        for word in unique_words:
            if word not in self._inverted:
                self._inverted[word] = []
            self._inverted[word].append(normalized_path)

    def _calculate_idf(self, str):
        '''
        Calculates the idf for a given string
        '''
        if str not in self._inverted:
            return 0

        return math.log(len(self._documents) / len(self._inverted[str]))

    def search(self, query):
        '''
        Searches for a query and returns a ranked list of documents based on TF-IDF scores.
        '''
        query_terms = [normalize_token(term) for term in query.split()]
        doc_scores = {}

        for term in query_terms:
            if term in self._inverted:
                for document_path in self._inverted[term]:
                    tf = self._documents[document_path].term_frequency(term)
                    idf = self._calculate_idf(term)
                    # checking for multi-term query's
                    if document_path not in doc_scores:
                        doc_scores[document_path] = tf * idf
                    else:
                        doc_scores[document_path] += tf * idf

        # if all scores are 0, then return a blank list
        if all(score == 0 for score in doc_scores.values()):
            return []

        # sorts the dictionary by values and returns the keys as a list (in reverse)
        ranked_docs = sorted(doc_scores, key=doc_scores.get, reverse=True)
        return ranked_docs