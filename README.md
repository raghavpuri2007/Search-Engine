# Search Engine Project

This project implements a simple search engine using Python. The search engine supports text-based queries and returns results based on **Term Frequency-Inverse Document Frequency (TF-IDF)**, a statistical measure used to evaluate the relevance of documents in a corpus.

## Features

- **Document Representation**: The `Document` class handles the representation of individual text documents, including term frequency calculations.
- **Search Engine**: The `SearchEngine` class aggregates the documents in a corpus and performs searches based on TF-IDF relevance.
- **Console Interaction**: A user-friendly command-line interface allows users to input queries and view ranked search results.
- **Custom Test Corpus**: Users can create their own test document directories to evaluate search functionality.

## How It Works

The search engine processes a directory of text documents, normalizing the content to remove punctuation and case differences. When a query is entered, the engine calculates the TF-IDF score for each document relative to the query terms and returns the most relevant results.

### Example Output

```plaintext
Please enter the name of a directory: small_text
Building Search Engine...

Enter a search term to query (Enter=Quit): Elvis
Displaying results for 'Elvis':
    1. small_text/Viacom - Wikipedia.txt
    2. small_text/Federal Bureau of Investigation - Wikipedia.txt
    ...

Enter a search term to query (Enter=Quit): notinanydocument
Displaying results for 'notinanydocument':
    No results :(

Enter a search term to query (Enter=Quit): 
Thank you for searching.
