import tkinter as tk
from tkinter import filedialog, messagebox
import os
import comtypes.client
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("DWG files", "*.dwg")])
    if file_path:
        convert_to_pdf(file_path)

def convert_to_pdf(dwg_path):
    try:
        # Create AutoCAD application object
        acad = comtypes.client.CreateObject("AutoCAD.Application")

        # Open the DWG file
        doc = acad.Documents.Open(dwg_path)

        # Get the modelspace
        msp = doc.ModelSpace

        # Create a PDF file
        pdf_path = dwg_path.replace('.dwg', '.pdf')
        c = canvas.Canvas(pdf_path, pagesize=letter)

        # Iterate through entities and add them to the PDF
        for entity in msp:
            # Add logic to handle different entity types
            # For example, you can handle LINE, CIRCLE, TEXT, etc.
            if entity.EntityName == 'AcDbLine':
                start_point = entity.StartPoint
                end_point = entity.EndPoint
                c.line(start_point[0], start_point[1], end_point[0], end_point[1])

        c.save()

        # Close the document
        doc.Close()

        # Close AutoCAD
        acad.Quit()

        messagebox.showinfo("Success", f"File converted successfully to {pdf_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("DWG to PDF Converter")

# Create and place the components
select_button = tk.Button(root, text="Select DWG File", command=select_file)
select_button.pack(pady=20)

# Run the application
root.mainloop()
