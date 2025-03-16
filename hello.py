import pyttsx3
import PyPDF2

# Open the PDF file
with open('note.pdf', 'rb') as pdf_file:
    pdfreader = PyPDF2.PdfReader(pdf_file)

    speaker = pyttsx3.init()
    full_text = ""

    # Iterate through each page
    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        if text:  # Ensure text is extracted
            clean_text = text.strip().replace('\n', ' ')
            full_text += clean_text + " "  # Append text for later audio conversion
            print(clean_text)  # Print the extracted text for debugging

    # Convert the entire extracted text to speech
    if full_text:
        speaker.save_to_file(full_text, 'resume_audio.mp3')
        speaker.runAndWait()

    speaker.stop()
