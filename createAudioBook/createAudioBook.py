import pyttsx3
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('C:/Users/sshri/Downloads/PythonProjects/createAudioBook/Offer.pdf', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
engine.save_to_file(text, 'C:/Users/sshri/Downloads/PythonProjects/createAudioBook/audio.mp3')
engine.runAndWait()