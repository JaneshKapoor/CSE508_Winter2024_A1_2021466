import os
import pickle

# Assuming the preprocess_query function is defined similarly to Q1
def preprocess_query(query):
    # Placeholder for the actual preprocessing logic used in Q1
    # Convert to lowercase, tokenize, remove stopwords and punctuation
    query = query.lower().split()
    # Assuming stopwords removal is needed
    stopwords = {'the', 'is', 'in', 'on', 'and', 'a', 'to', 'of'}
    query = [word for word in query if word.isalnum() and word not in stopwords]
    return query

def create_positional_index(directory):
    positional_index = {}
    for filename in os.listdir(directory):
        if filename.startswith("processed_"):  # Ensure to work with preprocessed files
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read().split()
                for position, term in enumerate(content):
                    if term not in positional_index:
                        positional_index[term] = {}
                    if filename not in positional_index[term]:
                        positional_index[term][filename] = []
                    positional_index[term][filename].append(position)
    return positional_index

def save_positional_index(index, filename='positional_index.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump(index, file)

def load_positional_index(filename='positional_index.pkl'):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def find_phrase_in_index(positional_index, phrase):
    phrase_terms = preprocess_query(phrase)
    if not phrase_terms:
        return []
    
    # Initialize with the first term's postings
    if phrase_terms[0] not in positional_index:
        return []
    postings = positional_index[phrase_terms[0]]
    
    for term in phrase_terms[1:]:
        if term not in positional_index:
            return []
        current_postings = positional_index[term]
        temp_postings = {}
        
        for doc in postings:
            if doc in current_postings:
                for pos in postings[doc]:
                    if any(pos + 1 == next_pos for next_pos in current_postings[doc]):
                        if doc not in temp_postings:
                            temp_postings[doc] = [pos + 1]
                        else:
                            temp_postings[doc].append(pos + 1)
        
        postings = temp_postings
    
    return list(postings.keys())

def process_phrase_queries(queries, positional_index):
    for i, query in enumerate(queries, start=1):
        results = find_phrase_in_index(positional_index, query)
        print(f"Number of documents retrieved for query {i} using positional index: {len(results)}")
        print(f"Names of documents retrieved for query {i} using positional index: {', '.join(results)}")

# Assuming 'directory' is where your preprocessed files are located
directory = r'C:\Users\kapoo\Desktop\IIIT DELHI\IR Assignment\outputq1'
positional_index = create_positional_index(directory)

# Save and load the positional index
save_positional_index(positional_index)
loaded_positional_index = load_positional_index()

# Sample input format handling (replace with actual input handling as needed)
n_queries = int(input("Enter the number of queries: "))
queries = [input(f"Enter query {i+1}: ") for i in range(n_queries)]

# Process the phrase queries
process_phrase_queries(queries, loaded_positional_index)
