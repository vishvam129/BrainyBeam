import pypandoc
import os

def convert_docx_to_pdf(docx_file_path):
    """Converts .docx to .pdf"""
    output_pdf_path = os.path.splitext(docx_file_path)[0] + '.pdf'
    try:
        print(f"Converting {docx_file_path} to PDF...")
        pypandoc.convert_file(docx_file_path, 'pdf', outputfile=output_pdf_path)
        print(f"Conversion successful! PDF saved at {output_pdf_path}")
        return output_pdf_path
    except Exception as e:
        print(f"Error converting file: {e}")
        return None
