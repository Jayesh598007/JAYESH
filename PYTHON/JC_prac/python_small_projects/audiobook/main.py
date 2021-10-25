# this program is to convert pdf to audio books

# firstly install these below packages in terminal 

import pyttsx3       # for text to audio 
import PyPDF2       # for pdf to audio

book =open('oop.pdf', 'rb')       #open the pdf 
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()