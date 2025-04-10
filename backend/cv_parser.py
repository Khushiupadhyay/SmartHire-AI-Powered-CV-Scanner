import pdfplumber
import re

def extract_cv_data(path):
    with pdfplumber.open(path) as pdf:
        text = ''.join(page.extract_text() for page in pdf.pages if page.extract_text())

    if not text:
        print(f"❌ No extractable text in: {path}")

    name = re.search(r'Name:\s*(.*)', text)
    email = re.search(r'Email:\s*(.*)', text)

    return {
        'name': name.group(1).strip() if name else "Unknown",
        'email': email.group(1).strip() if email else "noemail@example.com",
        'text': text
    }
