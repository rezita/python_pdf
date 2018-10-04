# -*- coding: utf-8 -*-

## pdfSplitter is a simple script which splits the pages
## of a given pdf file in verticaly / horisontaly.
## The output file will appear in the given directory under 
## the name 'output.pdf'. 
## The script requires a path (of the directory) 
##  and a name of a odf file.
## The script does not check the authority of the given directory, 
## so the user need to have the authority to read and write 
## the given path directory.
##
## Author: Zita Reiner

import PyPDF2
import copy
import os, sys, math

path = ""
input_file = ""
vertical = False
#vertical = True

def is_valid_path(path):
    return os.path.exists(path)

def make_pdf(input, output):
    pdf_output = PyPDF2.PdfFileWriter()
    pdf_reader = PyPDF2.PdfFileReader(input)
    for page_number in range(pdf_reader.numPages):
        #get the current page
        page_1 = pdf_reader.getPage(page_number)
        #make a copy of the current page
        page_2 = copy.copy(page_1)

        box = page_1.mediaBox
        #lower left coordinates of the actual page
        x1, y1 = box.lowerLeft
        #upper right coordinates of actual page
        x2, y2 = box.upperRight
        #middle point of the page
        x3, y3 = math.floor(x2/2), math.floor(y2/2)

        if vertical:
            page_1.mediaBox.lowerleft = (x1, y1)
            page_1.mediaBox.upperRight = (x3, y2)
            page_2.mediaBox.lowerLeft = (x3, y1)
            page_2.mediaBox.upperRight = (x2, y2)

        else:
            page_1.mediaBox.lowerLeft = (x1, y3)
            page_1.mediaBox.upperRight = (x2, y2)
            page_2.mediaBox.lowerLeft = (x1, y1)
            page_2.mediaBox.upperRight = (x2, y3)            

        pdf_output.addPage(page_1)
        pdf_output.addPage(page_2)
    try:
        pdf_output_file = open(output, 'wb')
        pdf_output.write(pdf_output_file)
        pdf_output_file.close()
        print "Done."
    except IOError:
        print "PDF writting failed. Check if output.pdf is closed."
    
def main():
    if is_valid_path(path):    
        file_path = os.path.join(path, "output.pdf")
        input_path = os.path.join(path, input_file)
        make_pdf(input_path, file_path)
    else:
        print "invalid path"

if __name__ == "__main__":
    if len(sys.argv[1:]) >0:
        if sys.argv[1:][0]:
            path = sys.argv[1:][0]
    if sys.argv[1:][1]:
        input_file = sys.argv[1:][1]
    if path and input_file:
        main()
    else:
        print("It seems, somethin is missing (path or filename).")
        
        

        
        
