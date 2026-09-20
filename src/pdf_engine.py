import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from a PDF file and returns it as a single cleaned string.
    """
    text_blocks = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_blocks.append(text)

        # Join pages and normalize whitespace
        full_text = "\n".join(text_blocks)
        return " ".join(full_text.split())
    except Exception as e:
        print(f"Error extracting PDF {pdf_path}: {e}")
        return ""
