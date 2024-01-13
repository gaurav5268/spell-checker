from tkinter import *
from tkinter import filedialog
from reportlab.pdfgen import canvas
from main import SpellChecker  # Assuming main1.py is the correct file name

# Initializing tkinter here
root = Tk()
root.geometry("900x600")  # width and height of GUI
root.title(" Spell Checker ")

def openFile():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            inputText.delete("1.0", "end")
            inputText.insert("1.0", file.read())

def saveFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(Output.get("1.0", "end-1c"))

def savePDF():
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if file_path:
        corrected_text = Output.get("1.0", "end-1c")
        generate_pdf(file_path, corrected_text)

def generate_pdf(file_path, corrected_text):
    c = canvas.Canvas(file_path)
    c.setFont("Helvetica", 12)
    lines = corrected_text.split('\n')
    y_position = 750  # Initial y position for text

    for line in lines:
        c.drawString(50, y_position, line)
        y_position -= 15  # Adjust the vertical position for the next line

    c.save()

def takeInput():
    Output.delete("1.0", "end")
    Input = inputText.get("1.0", "end-1c")
    spell_checker = SpellChecker("C:\\Users\\Gravity\\Desktop\\project spell-checker\\corpus.txt")

    wrong_words = spell_checker.find_wrong_word(Input)
    Output.insert(END, 'Wrong words: ' + ', '.join(wrong_words) + '\n')

    if wrong_words:
        corrected_sentence = spell_checker.autocorrect_sentence(Input)
        Output.insert(END, 'Corrected sentence: ' + corrected_sentence + '\n')
    else:
        Output.insert(END, 'Correct!\n')

# Label is a widget provided by tkinter to display text/image on screen
l = Label(text="Type the word here: ", bg='#759D98',
          bd='4', font=("Times", "23", "bold"), width='40')

# Here, Text widget is initialized and assigned to the variable inputText.
inputText = Text(root, height=2, width=40, bd='3', font=("Times", "18", "bold"))

# The button widget is initialized here, this will add a button with the name Check
Check = Button(root, height=2, width=20, text="Check",
               command=lambda: takeInput(), bg='#375F5A', fg='white', font=("Times", "14"))

# Here, the text box is initialized, where the final result after checking spelling will be displayed
Output = Text(root, height=5, width=40, bd='3', bg='#8C9F9D', font=("Times", "18", "bold"))

# Buttons for opening and saving files
OpenButton = Button(root, text="Open File", command=openFile)
SaveButton = Button(root, text="Save Corrected Text", command=saveFile)
SavePDFButton = Button(root, text="Save Corrected PDF", command=savePDF)

# the pack() method declares the position of widgets in relation to each other
l.pack(padx=2, pady=2)
inputText.pack(padx=5, pady=5)
Check.pack(padx=2, pady=2)
Output.pack(pady=5)
OpenButton.pack(pady=5)
SaveButton.pack(pady=5)
SavePDFButton.pack(pady=5)

# This is to call an endless loop so that the GUI window stays open until the user closes it
mainloop()
