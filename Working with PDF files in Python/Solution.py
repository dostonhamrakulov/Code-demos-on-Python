import PyPDF2

# Step_1: creating a pdf file object
pdfFileObj = open('Globbing.pdf', 'rb')

# Step_2: creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Step_3: printing number of pages in pdf file
print(pdfReader.numPages)

# Step_4: creating a page object
pageObj = pdfReader.getPage(0)

# Step_5: extracting text from page
print(pageObj.extractText())

# Step_6: closing the pdf file object
pdfFileObj.close()
