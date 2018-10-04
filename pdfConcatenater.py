# -*- coding: utf-8 -*-

## pdfConcatener is a simple script which concatenates pdf files 
## from the given directory usinf PyFPDF2 library.
## The output file will appear in the given directory under 
## the name 'output.pdf'. 
## The script requires a path (of the directory) 
## where the pdf files can be found.
## The script does not check the authority of the given directory, 
## so the user need to have the authority to read and write 
## the given path directory.
##
## Author: Zita Reiner

import PyPDF2
import glob, os, sys

path = ""

def is_valid_path(path):
    """Checks if the given path exists ot not"""
    return os.path.exists(path)

def get_files(path):
    """Collects the pdf files from the given path"""
    pdf_files = []
    for file_name in glob.glob(path + "\*.pdf"):
        pdf_files.append(file_name)
    return pdf_files

def concatenate_pdfs(path, output):
    pdf_output = PyPDF2.PdfFileWriter()    
    sources = get_files(path)
    for act_file in sources:
        pdf_reader = PyPDF2.PdfFileReader(act_file)
        for page_num in range(pdf_reader.numPages):
            pdf_output.addPage(pdf_reader.getPage(page_num))
    try:
        pdf_output_file = open(output, 'wb')
        pdf_output.write(pdf_output_file)
        pdf_output_file.close()
        print "Done."
    except IOError:
        print "PDF writting failed. Check if output.pdf is closed."

def main():
    if is_valid_path(path):    
        output_path = os.path.join(path, "output.pdf")
        concatenate_pdfs(path, output_path)
    else:
        print "Invalid path"

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        if sys.argv[1:][0]:
            path = sys.argv[1:][0]
            main()
    else:
        print "Missing argument."
        
        

        
        
