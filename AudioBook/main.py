import pyttsx3
import PyPDF2
book = open('python.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Total no of Pages in the PDF: ",+ pages)
speaker = pyttsx3.init()
for num in range(7,pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say('hey Boss, ready to read the pdf  ')
    speaker.say(text)
    speaker.runAndWait()
