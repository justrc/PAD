from tkinter import * #import all of tkinter tools


        
def import_topic():
        global topic_name #this will make the topic_name variable accessable outside the def.
        global question_file #this makes the question_file variable accessable outside the def
        global dict_name  #this makes the dict_name variable accessable outside the def.
        global questions
        question_file="questions.txt"  #will change the question_file to movie_quiz.txt to open the movie quiz file
        question_file=questions
        dict_name=movie_questions #this will change the dict_name variable into the movie_questions dict variable to append the questions and answers to later.
        open_quiz() #this will move to the open_quiz file def. 
        
        
class Start:
        
        def __init__(self,parent):
       
                # formatting variables
                background_color = "purple"
                font_colour = "white"
        
                # main frame
                self.start_frame = Frame (width=300, bg=background_color,
                                        pady=10)
                self.start_frame.grid()
       
                # heading
                self.start_heading_label = Label(self.start_frame,
                                                text="Razza's Quiz",
                                                font="Arial 16 bold",
                                                fg=font_colour,
                                                bg=background_color,
                                                padx=10, pady=10)
                self.start_heading_label.grid(row=0)
       
                # name entry
  
                self.start_instructions_label = Label(self.start_frame,
                                                text="Type in your name for the leaderboard "
                                                        "Click start to begin the quiz",
                                                font="Arial 10 italic", wrap=250,
                                                fg=font_colour,
                                                justify=LEFT, bg=background_color,
                                                padx=10, pady=10)
                self.start_instructions_label.grid(row=1)
       
                # Weight entry box (row 2)
                self.to_start_entry = Entry(self.start_frame, width=20,
                                        font="Arial 14 bold")
                self.to_start_entry.grid(row=2)
       
                # Conversion buttons frame (row 3), orchid3 | khaki1
                self.start_buttons_frame = Frame(self.start_frame)
                self.start_buttons_frame.grid(row=3, pady=10)
       
                self.start_button = Button(self.start_buttons_frame,
                                        text="Start", font="Arial 10 bold",
                                        command=self.start,
                                        bg="lime green", fg="white", padx=10, pady=10)
                self.start_button.grid(row=3, column=0)
       
                self.start_button = Button(self.start_buttons_frame,
                                        text="Exit", font="Arial 10 bold",
                                        bg="red", fg="white", padx=10, pady=10)
                self.start_button.grid(row=3, column=1)
       
                # History / Help button frame (row 5)
                self.hist_help_frame = Frame(self.start_frame)
                self.hist_help_frame.grid(row=4, pady=10)
       
                self.leaderboard_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                        text="Leaderboard", bg="LightSkyBlue3", fg="white", width=15)
                self.leaderboard_button.grid(row=0, column=0)
               
                #self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                          #command=Help(partner),
                                          #text="Help",bg="medium slate blue",fg="white", width=5)
                self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                          command=Help(),
                                          text="Help",bg="medium slate blue",fg="white", width=5)                
                self.help_button.grid(row=0, column=1) 
                
                
        def start(self):
                start_questions=questions()
                self.start_frame.destroy()        
                        
class questions:
        global maincount
        maincount=0
        
        def __init__(self):
                background='purple'
                
                self.questions_box=Toplevel()
                
                self.questions_frame=Frame(self.questions_box, width=300, height=450, bg=background, padx=30)
                self.questions_frame.grid()
                
                # heading for questions
                self.q_heading=Label(self.questions_frame, text="Razza's Quiz", font='Arial 16 bold', bg= background, fg='white', padx=10, pady=10)
                self.q_heading.grid(row=6, columnspan=2)

class intro:
        def __init__(self,partner):

                background = "purple"
        
                # Disable submit button
                partner.submit_button.config(state = DISABLED)
        
                # Sets up child daughterdow (submit box)
                self.submit_box = Toplevel()
        
                # Set up Gui Frame
                self.intro_frame = Frame(self.submit_box, width = 300, bg = background)
                self.intro_frame.grid()
        
                # Set up submit heading (rov 0 )
                self.how_heading = Label (self.intro_frame, text = "***************",
                                          font = "Arial 20 bold", bg = background)
                self.how_heading.grid (row = 0)
        
                # submit text (label, rov 1)
                self.intro_text = Label(self.intro_frame, text = "",
                                        justify = LEFT, width = 40, bg = background, wrap = 250)
                #self.intro_text.grid (column = 0, row = 1)
                self.intro_text.grid (row = 1)
        
                # Dismiss button (row 2)
                self.dis_btn = Button(self.intro_frame, text = "Back",
                                      width = 10, bg = "yellow", font = "Arial 10 bold",
                                       padx = 10, pady = 10,
                                       command = partial(self.close_submit, partner))      
                self.dis_btn.grid(row = 2, pady = 10)

def close_submit(self,partner):
        # Puts the submit button back to normal
        partner.submit_button.config(state = NORMAL)
        self.submit_box.destroy()
           
class Help:
        def __init__(partner):
                print ("You asked for help.")
                get_help = Help()
                get_help.help_text.configure(text="Help text goes here.")
                
                print("ffffffffffff")
                background_color = "orange"
               
                # disable help button
                partner.help_button.config(state=DISABLED)
               
                # Sets up child window (ie: help box)
                self.help_box = Toplevel()
                self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))
           
                # Set up GUI Frame
                self.help_frame = Frame(self.help_box, bg=background_color)
                self.help_frame.grid()
               
               
                # Set up help heading (row 0)
                self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                         font="arial 10 bold", bg=background_color)
                self.how_heading.grid(row=0)
               
                # Help text (label,row 1)
                self.help_text = Label(self.help_frame, text="Help / Instructions",
                                       justify=LEFT, width=40, bg=background_color, wrap=250)
                self.help_text.grid(column=0, row=1)
               
                # Dismiss button (row 2)
                self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                          width=10, bg="orange", font="arial 10 bold",
                                          command=partial(self.close_help, partner))
                self.dismiss_btn.grid(row=2, pady=10)
               
        def close_help(partner):
                print("sssssssss")
                # Put help button back to normal...
                partner.help_button.config(state=NORMAL)
                self.help_box.destroy()
                
               
# Main Routine
if __name__ =="__main__":
        root =Tk()
        root.title("Razza's Quiz")
        convert_it=Start(root)
        root.mainloop() 
        start()

                
                              


                                 
                

               
        