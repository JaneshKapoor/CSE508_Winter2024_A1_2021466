import os
import pickle

def create_unigram_inverted_index(directory):
    inverted_index = {}
    # Filter to only include processed files
    processed_files = [f for f in os.listdir(directory) if f.startswith('processed_')]
    
    for file_name in processed_files:
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().split()
            for word in content:
                if word not in inverted_index:
                    inverted_index[word] = set()
                inverted_index[word].add(file_name)
    return inverted_index

# Specify the directory containing the preprocessed files
directory = r'C:\\Users\\kapoo\\Desktop\\IIIT DELHI\\IR Assignment\\outputq1'
inverted_index = create_unigram_inverted_index(directory)

# Step 2: Serialize the inverted index with pickle
index_path = 'inverted_index.pkl'
with open(index_path, 'wb') as f:
    pickle.dump(inverted_index, f)


def load_inverted_index(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def execute_query(inverted_index, query):
    # Simplify the query execution to match the basic requirements
    # This function needs to be extended for complex query parsing
    elements = query.split()
    result_set = None

    for element in elements:
        if element in inverted_index:
            if result_set is None:
                result_set = inverted_index[element]
            else:
                result_set = result_set.union(inverted_index[element])
        else:
            # For terms not found, consider how you want to handle these (e.g., ignore, treat as empty set)
            pass

    return result_set if result_set is not None else set()

# Load the inverted index
inverted_index = load_inverted_index(index_path)

# Example usage for a simple OR operation (extend this for AND, AND NOT, OR NOT)
query = "Coffee brewing techniques in cookbook"
results = execute_query(inverted_index, query)
print(f"Query: {query}")
print(f"Number of documents retrieved: {len(results)}")
print(f"Names of the documents retrieved: {', '.join(sorted(results))}")

def preprocess_query(query):
    # Convert to lowercase
    query_lower = query.lower()
    
    # Simple tokenization by splitting on spaces (for a more robust approach, consider using regex or nltk)
    tokens = query_lower.split()
    
    # Remove stopwords (define your list of stopwords or import from a library if available)
    stop_words = set(["the", "is", "at", "which", "on", "of", "and", "a", "to", "in"])  # Example stopwords
    tokens_no_stopwords = [word for word in tokens if word not in stop_words]
    
    # Remove punctuation
    tokens_no_punctuation = [word for word in tokens_no_stopwords if word.isalnum()]
    
    return tokens_no_punctuation


def process_queries(n, queries):
    for i in range(n):
        query_terms, operations = queries[i*2], queries[i*2 + 1].split(", ")
        # Preprocess query_terms similarly to how documents were preprocessed
        preprocessed_terms = preprocess_query(query_terms)  # Implement this
        results = execute_query(inverted_index, preprocessed_terms, operations)
        print(f"Query {i+1}: {' '.join(preprocessed_terms)}")
        print(f"Number of documents retrieved for query {i+1}: {len(results)}")
        print(f"Names of the documents retrieved for query {i+1}: {', '.join(sorted(results))}")
