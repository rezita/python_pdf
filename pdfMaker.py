# -*- coding: utf-8 -*-

## pdfMaker is a simple script which creates a pdf file 
## from the given image files using FPDF library.
## It copies the images into a pdf file in lexicographic order.
## The output file will appear in the directory of the images
## under the name 'output.pdf'. 
## The script requires a path (of the directory) 
## where the images can be found.
## The script does not check the authority of the given directory, 
## so the user need to have the authority to read and write 
## the given path directory.
##
## Author: Zita Reiner

from fpdf import FPDF
import glob, os, sys
from PIL import Image

#margin in pixels
PAGE_MARGIN = 20
#FPDF supported formats are 'jpg', 'gif' and 'png'
APPROVED_EXTENSIONS = 'jpg', 'gif', 'png'
path = ""

def is_valid_path(path):
    """Checks if the given path exists ot not"""
    return os.path.exists(path)

def get_images(path):
    """Collects the images files from the given path"""
    images = []
    #for fileName.lower() in glob.glob(path + "\*.gif"):
    for file_name in os.listdir(path):
        if file_name.lower().endswith(APPROVED_EXTENSIONS):
            images.append(os.path.join(path, file_name))
    return images

def get_page_size(images):
    """Calculates the dimensions of pages by finding the 
        largest dimensions of images and set margins all sides"""
    sizes = [Image.open(f, 'r').size for f in images]
    max_width =  max(sizes, key = lambda x: x[0])[0]
    max_height = max(sizes, key = lambda x: x[1])[1]
    return (max_width + 2 * PAGE_MARGIN, max_height + 2 * PAGE_MARGIN)

def create_pdf(path, output_file):
    """Collects the images from the given path, 
        sets the page size and writes the output pdf file """
    images = get_images(path)
    page_size = get_page_size(images)
    pdf = FPDF(unit = 'pt', format = page_size)
    for imgage in images:
        pdf.add_page()
        pdf.image(imgage, x = PAGE_MARGIN, y = PAGE_MARGIN)
    try:
        pdf.output(output_file, "F")
        print "Done."
    except IOError:
        print "PDF writting failed. Check if output.pdf is closed."

def main():
    if is_valid_path(path):
        file_path = os.path.join(path, "output.pdf")
        create_pdf(path, file_path)
    else:
        print "Invalid path"

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0:
        if sys.argv[1:][0]:
            path = sys.argv[1:][0]
    else:
        path = os.getcwd()
    main()
