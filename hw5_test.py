"""
Raghav Puri
Intermediate Data Programming
"""

import math
from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine


def test_search_single_document_match(engine):
    '''
    Test search where only one document matches the query.
    '''
    expected = ['raghav_corpus/doc1.txt']
    actual = engine.search('Raghav')
    assert_equals(expected, actual)


def test_multiple_match_search(engine):
    '''
    Test a query that matches multiple documents.
    '''
    expected = ['raghav_corpus/doc3.txt', 'raghav_corpus/doc5.txt']
    actual = engine.search('Python')
    assert_equals(expected, actual)


def test_search_edge_case_empty_query(engine):
    '''
    Test search functionality with an empty query.
    '''
    expected = []
    actual = engine.search('')
    assert_equals(expected, actual)


def test_search_no_results(engine):
    '''
    Test search functionality with a query that has no results.
    '''
    expected = []
    actual = engine.search('nonexistent query')
    assert_equals(expected, actual)


def test_large_query(engine):
    '''
    Test a very large query string that won't anything.
    '''
    large_query = 'a' * 1000  # Query with 1000 'a' characters
    expected = []
    actual = engine.search(large_query)
    assert_equals(expected, actual)


def test_calculate_idf_nothing(engine):
    '''
    Test _calculate_idf for a word not found in any documents.
    '''
    idf = engine._calculate_idf('nonexistentword')
    assert_equals(0, idf)  # If word doesn't exist, it should return 0


def test_calculate_idf_single(engine):
    '''
    Test calculate_idf for a word found in only one document.
    '''
    idf_single_doc = engine._calculate_idf('Puri')  # 'Puri' only in Document1.txt
    expected_idf = round(math.log(5 / 5), 5)
    assert_equals(expected_idf, round(idf_single_doc, 5))


def test_load_words(doc):
    '''
    Test load_words functionality to check if words are loaded correctly.
    '''
    expected_words = {'hello', 'my', 'name', 'is', 'raghav', 'puri'}
    assert_equals(expected_words, set(doc._words))


def test_get_path(doc):
    '''
    Test if get_path correctly returns the path for the document.
    '''
    expected_path = 'raghav_corpus/doc1.txt'
    assert_equals(expected_path, doc.get_path())


def test_get_words(doc):
    '''
    Test if get_words correctly returns the list of words from the document.
    '''
    expected_words = ['hello', 'my', 'name', 'is', 'raghav', 'puri']
    assert_equals(expected_words, doc.get_words())


def test_term_frequency(doc):
    '''
    Test term frequency calculation for a specific word in a document.
    '''
    tf_remember = doc.term_frequency('remember')
    # Remember appears 18 times in the 167 word document
    assert_equals(round(18 / 167, 2), round(tf_remember, 2))


def test_search():
    '''
    Function to test search engine class
    '''
    engine = SearchEngine('raghav_corpus')
    test_search_single_document_match(engine)
    test_multiple_match_search(engine)
    test_search_edge_case_empty_query(engine)
    test_search_no_results(engine)
    test_large_query(engine)
    test_calculate_idf_nothing(engine)
    test_calculate_idf_single(engine)


def test_document():
    '''
    Function to test document class.
    '''
    doc1 = Document('raghav_corpus/doc1.txt')
    doc2 = Document('raghav_corpus/doc2.txt')
    test_load_words(doc1)
    test_get_path(doc1)
    test_get_words(doc1)
    test_term_frequency(doc2)


def main():
    '''
    Main function to run all tests.
    '''
    test_search()
    test_document()
    print("All tests passed!")


if __name__ == '__main__':
    main()