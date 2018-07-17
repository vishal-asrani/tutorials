import pdfkit

# covert content of url google.com to a pdf named out1.pdf
pdfkit.from_url('google.com', 'out1.pdf')

# covert content of below file to a pdf named fromfile.pdf
pdfkit.from_file('../collections/deque.py', 'fromfile.pdf')
