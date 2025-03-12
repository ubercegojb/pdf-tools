from PyPDF2 import PdfMerger, PdfReader, PdfWriter
import pdfplumber
from pdf2image import convert_from_path
import os

def convert_pdf_to_word(pdf_path):
    output_path = "converted.docx"
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    with open(output_path, "w") as f:
        f.write(text)
    return output_path

def merge_pdfs(pdf_paths):
    merger = PdfMerger()
    for path in pdf_paths:
        merger.append(path)
    output_path = "merged.pdf"
    merger.write(output_path)
    merger.close()
    return output_path

def compress_pdf(pdf_path):
    # Implemente a compressão de PDF
    pass

def protect_pdf(pdf_path, password):
    # Implemente a proteção de PDF com senha
    pass