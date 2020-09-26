import sys
import os
from PyPDF2 import PdfFileMerger, PdfFileReader

script = sys.argv[0]
filenames = sys.argv[1:]

merged = PdfFileMerger()

for file in filenames:
  merged.append(PdfFileReader(os.path.realpath(file),'rb'))

merged.write("output.pdf")
