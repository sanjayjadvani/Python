import PyPDF2
from PyPDF2 import *

def search_parameter(file_name,param):
    with open(file_name, 'rb') as report:
        ln_no=0
        for line in report:
            ln_no+=1
            if param in line:
                print(param, 'is in line ',ln_no)
                print(line)
                print(line.find(param))
                break


report=open('SamplePDF.pdf', 'rb')
pdfdata01=PyPDF2.PdfFileReader(report)
pdfpage01=pdfdata01.getPage(0)
print('Number of pages :', pdfdata01.numPages)
print(pdfpage01.extractText())
report.close()


#param1=input('Please enter the Parameter to search :')





