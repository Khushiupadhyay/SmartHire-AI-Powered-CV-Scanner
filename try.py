import pdfplumber
pdf = pdfplumber.open('../CV/C1061.pdf')
text = ''.join(page.extract_text() for page in pdf.pages)
print(text[:500])
