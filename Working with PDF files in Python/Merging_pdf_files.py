import PyPDF2


def PDFmerge(pdfs, output):

    # Step_1: creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # Step_2: appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)

    # Step_3: writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)

def main():

    # pdf files to merge
    pdfs = ['Globbing.pdf', 'rotated_globbing.pdf']

    # output pdf file name
    output = 'combined_globbings.pdf'

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)

if __name__ == "__main__":
    # calling the main function
    main()
