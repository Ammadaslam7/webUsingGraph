import os
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
from docx import Document  

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load DOCX file
docx_path = r'd:\Work\Semester 6\GT\Project 1\webUsingGraph\scrapping\Marketing and Sales\Document 15.docx'
doc = Document(docx_path)

# Extract text from DOCX
text_list = []
for paragraph in doc.paragraphs:
    text_list.append(paragraph.text)

# Convert list of paragraphs into a single string
doc_text = ' '.join(text_list)

# Tokenize text
tokenized_text = word_tokenize(doc_text)

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords and perform stemming
porter = PorterStemmer()
final_paragraph = []
for word in tokenized_text:
    if word.lower() not in stop_words:
        stemmed_word = porter.stem(word)
        final_paragraph.append(stemmed_word)

# Join the final paragraph into a single string
final_paragraph_str = ' '.join(final_paragraph)

# Get the name of the input document
doc_name = os.path.basename(docx_path)
doc_name_without_ext = os.path.splitext(doc_name)[0]

# Save final paragraph to a text file with the same name as the input document
output_path = os.path.join(os.path.dirname(__file__), f"{doc_name_without_ext}_final.txt")
with open(output_path, "w", encoding="utf-8") as final_file:
    final_file.write(final_paragraph_str)

print(f"Final paragraph saved successfully as {doc_name_without_ext}_final.txt.")
