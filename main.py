"""
Raghav Puri
Intermediate Data Programming
"""
from search_engine import SearchEngine


def main():
    """
    This is the starting point for this Search Engine.
    It initializes a SearchEngine instance, asks the user for query's, 
    and displays ranked search results.
    """

    # Prompt the user for the path to the directory containing the text files
    directory = input("Please enter the name of a directory: ")
    print("Building Search Engine...\n")

    # checks if the inputted directory is valid
    try:
        search_engine = SearchEngine(directory)
    except FileNotFoundError:
        print("Error: Directory not found.")
        # returning exits the main function
        return

    while True:
        # prompt the user for a search
        query = input("Enter a search term to query (Enter=Quit): ")

        # check if the user wants to exit
        if query.strip() == "":
            print("Thank you for searching.")
            break

        print('Displaying results for \'' + query + '\':')
        results = search_engine.search(query)
        if len(results) == 0:
            print("No results :(")
        else:
            index = 1
            # prints top 10 document results
            for document in results:
                if index > 10:
                    break
                print(str(index) + ". " + document)
                index += 1


if __name__ == '__main__':
    main()