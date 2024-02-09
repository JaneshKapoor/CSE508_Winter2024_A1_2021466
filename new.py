import os
import string
from zipfile import ZipFile
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Function to preprocess text
def preprocess_text(text):
    # Lowercase the text
    text_lower = text.lower()
    
    # Tokenize the text
    tokens = word_tokenize(text_lower)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens_no_stopwords = [word for word in tokens if word not in stop_words]
    
    # Remove punctuation and non-alphanumeric tokens
    tokens_no_punctuation = [word for word in tokens_no_stopwords if word.isalnum()]
    
    return ' '.join(tokens_no_punctuation)  # Return processed text as a single string

# Function to process and save files
def process_and_save_files(zip_file_path, output_dir):
    # Extract the ZIP file
    with ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    # Counter for processed files
    files_processed = 0

    # Iterate over files in the output directory
    for file_name in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file_name)
        

    #######################Naya Code
        if (os.path.isfile(file_path) and files_processed < 9):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    text = file.read()
                
                # Display before preprocessing
                print(f"Before preprocessing {file_name}:")
                print(text[:500])  # Print the first 500 characters for demonstration
                
                # Preprocess the text
                processed_tokens = preprocess_text(text)
                processed_text = ' '.join(processed_tokens)
                
                # Display after preprocessing
                print(f"After preprocessing {file_name}:")
                print(''.join(processed_tokens[:100]))  # Print the first 100 tokens after preprocessing
                
                # Save the preprocessed text to a new file
                processed_file_path = os.path.join(output_dir, f"processed_{file_name}")
                with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
                    processed_file.write(processed_text)
                
                files_processed += 1
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")


        # Check if it's a file
        if os.path.isfile(file_path):
            # print(f"Processing {file_name}...")  # Debug print
            
            # Read the file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
            
            # Process the text
            processed_text = preprocess_text(text)
            
            # Save the processed text to a new file
            processed_file_path = os.path.join(output_dir, f"processed_{file_name}")
            with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
                processed_file.write(processed_text)
            
            files_processed += 1
            # print(f"Processed and saved {processed_file_path}")  # Debug print
            
        #New Code
            # For demonstration, limit to processing just 5 files
            # if files_processed >= 5:
            #     break

# Define paths to your ZIP file and the output directory
zip_file_path = r'C:\\Users\\kapoo\\Desktop\\IIIT DELHI\\IR Assignment\\irassignment.zip'
output_dir = r'C:\\Users\\kapoo\\Desktop\\IIIT DELHI\\IR Assignment\\outputq1'

process_and_save_files(zip_file_path, output_dir)