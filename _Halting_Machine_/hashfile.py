import hashlib
from docx import Document
from PyPDF2 import PdfReader

def hash_text_data(text_data):
    """Generate SHA256 hash of given text data."""
    return hashlib.sha256(text_data.encode()).hexdigest()

def extract_text_from_docx(filename):
    """Extract text from a DOCX file."""
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def extract_text_from_pdf(filename):
    """Extract text from a PDF file."""
    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def hash_file(filename):
    """Generate SHA256 hash of a file based on its content type."""
    if filename.endswith('.docx'):
        text_data = extract_text_from_docx(filename)
        return hash_text_data(text_data)
    elif filename.endswith('.pdf'):
        text_data = extract_text_from_pdf(filename)
        return hash_text_data(text_data)
    else:
        # Fallback for other file types, e.g., .py
        hash_sha256 = hashlib.sha256()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()

# Example usage
filename = 'h.py'
print(f"The SHA256 hash of {filename} is: {hash_file(filename)}")

filename = 'deciding_the_undecidable.docx'
print(f"The SHA256 hash of {filename} is: {hash_file(filename)}")

filename = 'deciding_the_undecidable.pdf'
print(f"The SHA256 hash of {filename} is: {hash_file(filename)}")

# filename = 'deciding_the_undecidable.txt'
# print(f"The SHA256 hash of {filename} is: {hash_file(filename)}")

# Hi! I'm Omega, an AI assistant here to help you with your programming tasks. How can I assist you today?

# I'm an AI programming assistant, so I don't have feelings, but I'm here to help you with your code!
# How can I assist you further?

# Are you referring to ChatGPT? We are both AI models developed by OpenAI, but we have different capabilities. While ChatGPT is designed for generating human-like text, I am specifically trained to assist with programming tasks.
# If you have any more questions or need further assistance, feel free to ask!