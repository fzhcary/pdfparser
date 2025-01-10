import fitz  # PyMuPDF
import re
import json

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from each page of the PDF located at pdf_path.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as pdf_document:
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF file: {e}")
    return text

def parse_fields_from_text(text, fields):
    """
    Parses specified fields from the extracted text.
    """
    data = {}
    for field in fields:
        # Regular expression to find the field and its value
        pattern = rf"{field}:\s*(.*)"
        match = re.search(pattern, text)
        if match:
            data[field] = match.group(1).strip()
        else:
            data[field] = None  # Field not found
    return data

def convert_to_json(data):
    """
    Converts the dictionary to a JSON-formatted string.
    """
    try:
        return json.dumps(data, indent=4)
    except (TypeError, ValueError) as e:
        print(f"Error converting to JSON: {e}")
        return None
