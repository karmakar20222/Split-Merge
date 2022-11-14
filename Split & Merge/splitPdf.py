# from builtins import open, range
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = '/home/sltech/Documents/Python/split/output/T38_TEST_PAGES.pdf'

file = path.replace('.pdf','')

op_folder = os.path.join(os.getcwd(),'output')

pdf = PdfFileReader(path)
for page_num in range(pdf.numPages):

    pdfWritter = PdfFileWriter()
    pdfWritter.addPage(pdf.getPage(page_num))

    with open(os.path.join(op_folder,'{0}_page{1}.pdf'.format(file,page_num+1)), 'wb')as f:
        pdfWritter.write(f)
        f.close()
        

