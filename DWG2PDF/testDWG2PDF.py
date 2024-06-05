# The following code sample demonstrates how to convert a DWG file to a PDF document using Python.
import aspose.cad as cad

# Load an existing DWG file
image = cad.Image.load("C:\Files\sample.dwg")

# Specify PDF Options
pdfOptions = cad.imageoptions.PdfOptions()

# Save as PDF
image.save("C:\Files\output.pdf", pdfOptions)