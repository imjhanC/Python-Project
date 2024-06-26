from pdfminer.high_level import extract_text
from docx import Document

def pdf_to_docx(pdf_path, docx_path):
    # Extract text from PDF
    text = extract_text(pdf_path)
    
    # Create a new Document
    doc = Document()
    
    # Add extracted text to the document
    for line in text.split('\n'):
        doc.add_paragraph(line)
    
    # Save the document
    doc.save(docx_path)
    print(f"PDF has been converted to DOCX and saved as {docx_path}")

# Example usage:
pdf_path = 'MPU33213_Topic_8_Failures_and_Erros_in_Computer_Systems.pdf'
docx_path = 'new.docx'

pdf_to_docx(pdf_path, docx_path)