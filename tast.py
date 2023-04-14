import re

# Define the set of stop words to remove from the documents
stop_words = ["in", "is", "a", "and", "are", "the", "to", "of", "for"]

# Define the set of documents to index
documents = {
    "Doc 1": "new home sales top forecasts",
    "Doc 2": "home sales rise in July",
    "Doc 3": "increase in home sales in July",
    "Doc 4": "July new home sales rise"
}

# Initialize the inverted index as an empty dictionary
inverted_index = {}

# Iterate over each document and tokenize its contents
for doc_id, document in documents.items():
    # Remove punctuation and convert to lowercase
    document = re.sub(r'[^\w\s]', '', document.lower())
    # Tokenize the document
    tokens = document.split()
    # Remove stop words
    tokens = [token for token in tokens if token not in stop_words]
    # Add the document's tokens to the inverted index
    for token in tokens:
        if token not in inverted_index:
            inverted_index[token] = []
        inverted_index[token].append(doc_id)

# Get a search term from the user
search_term = input("Enter a search term: ").lower()

# Look up the search term in the inverted index and print the postings list
if search_term in inverted_index:
    postings_list = inverted_index[search_term]
    print("Postings list for {}: {}".format(search_term, ", ".join(postings_list)))
else:
    print("{} not found in any documents".format(search_term))    