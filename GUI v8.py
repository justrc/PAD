from tkinter import Tk, Frame, Label, Button # this imports parts of tk in order to create a label, window and buttons
from time import sleep
import random # this imports the random function in order for the program to choose questions at random from the text file
used =[]
class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        self.true_button.config(state="disabled") # disables the true button once the user has answered the question so they cannot click a button once they have clicked once
        self.false_button.config(state="disabled") # disables the false button once the user has answered the question so they cannot click a button once they have clicked once
        if(letter == self.correctLetter):
            label = Label(view, text="Correct!",fg="green") # tells the user they answered the question correctly
            right += 1 # adds one point to the users score
        else:
            label = Label(view, text="Incorrect!",fg="red") # tells the user they answered the question incorrectly
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):

        view = Frame(window, bg="purple") # to create a window for the questions and answers for the quiz
        Label(view, text=self.question).pack() # to present the question in the window
        self.true_button = Button(view, text=self.answers[0], command=lambda *args: self.check("A", view,))
        self.true_button.pack() # to check if the answer to the question is true
        self.false_button = Button(view, text=self.answers[1], command=lambda *args: self.check("B", view,))
        self.false_button.pack() # to check if the answer to the question is false

        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, Button, right, number_of_questions
    print(len(used),"len)") # this is to show the number of questions being asked in Debug window
    if(len(used) >9): # to only ask the user 10 of the 30 questions from the text file
        print(len(used))
        # to show the user their score and the final part of the program
        Label(window,bg="purple", fg="white", text="Thank you for taking the quiz. " + str(right) + " of " + "10" + " questions were answered correctly.").pack()

    else:
        index=random.choice(range(30)) # for the program to randomly choose one of the 30 questions at random so there isnt a fixed order or the same questions every attempt
        if index not in used:
            used.append(index) # to add questions aready asked to a list in order for the program to avoid asking the same question twice
            questions[index].getView(window).pack()
        else:
            askQuestion()
    button.pack_forget()


questions = []
file = open("QuizQuestions.txt", "r")
line = file.readline() # to read the questions in the text file and integrate them into the quiz
while(line != ""):
    questionString = line
    answers = []
    for i in range (2):
        answers.append(file.readline()) # to obtain the answers for each question

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]

    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)


window = Tk()
window.geometry="102400x800"
button = Button(window, text="Start", bg="Lime Green",command=askQuestion)
button.pack()
window.mainloop()
# this starts the program once the user runs it