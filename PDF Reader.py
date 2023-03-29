import PyPDF2  # python pdf module
import pyttsx3  # python text to speech version 3 module

book = open('name.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
speaker=pyttsx3.init()
i=int(input('Enter from where you want me to read'))
for num in range(i,pages):
  page=pdfReader.pages[num]
  text=page.extract_text()
  speaker.say(text)
  speaker.runAndWait()
  speaker.say("Page completed, moving to page number"+ str(i+1))
  i+=1
