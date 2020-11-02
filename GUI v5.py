from tkinter import Tk, Frame, Label, Button
from time import sleep

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Correct!",fg="green")
            right += 1
        else:
            label = Label(view, text="Incorrect!",fg="red")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):

        view = Frame(window, bg="purple")
        Label(view, text=self.question).pack()
        Button(view, text=self.answers[0], command=lambda *args: self.check("A", view,)).pack()
        Button(view, text=self.answers[1], command=lambda *args: self.check("B", view,)).pack()

        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions
    if(len(questions) == index + 1):

        Button.self = tk.DISABLED

        Label(window,bg="purple", text="Thank you for answering the questions." + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("QuizQuestions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (2):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]

    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)


window = Tk()
window.geometry=bg="purple",("102400x800")
button = Button(window, text="Start", bg="Lime Green",command=askQuestion)
button.pack()
window.mainloop()