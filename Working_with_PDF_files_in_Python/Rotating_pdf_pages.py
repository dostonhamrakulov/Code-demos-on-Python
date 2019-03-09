import PyPDF2


def PDFrotate(origFileName, newFileName, rotation):

    # step_1: creating a pdf File object of original pdf
    pdf_obj = open(origFileName, 'rb')

    # step_2: creating a pdf Reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_obj)

    # step_3: creating a pdf writer object for new pdf
    pdfWriter = PyPDF2.PdfFileWriter()

    # step_4: rotating each page
    for page in range(pdf_reader.numPages):
        # creating rotated page object
        pageObj = pdf_reader.getPage(page)
        pageObj.rotateClockwise(rotation)

        # adding rotated page object to pdf writer
        pdfWriter.addPage(pageObj)

    # step_5: new pdf file object
    newFile = open(newFileName, 'wb')

    # step_6: writing rotated pages to new file
    pdfWriter.write(newFile)

    # step_7: closing the original pdf file object
    pdf_obj.close()

    # step_7: closing the new pdf file object
    newFile.close()


def main():
    # original pdf file name
    origFileName = 'Globbing.pdf'

    # new pdf file name
    newFileName = 'rotated_globbing.pdf'

    # rotation angle
    rotation = 270

    # calling the PDFrotate function
    PDFrotate(origFileName, newFileName, rotation)


if __name__ == "__main__":
    # calling the main function
    main()
