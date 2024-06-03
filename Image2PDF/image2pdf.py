from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def image_to_pdf(image_path, pdf_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Create a new PDF file
    c = canvas.Canvas(pdf_path, pagesize=img.size)
    
    # Draw the image onto the PDF
    c.drawImage(image_path, 0, 0)
    
    # Save the PDF file
    c.save()

# Example usage:
image_path = '283210.jpg'  # Path to your image file
pdf_path = 'output.pdf'      # Output PDF file path

image_to_pdf(image_path, pdf_path)
print(f"PDF file saved at {pdf_path}")
