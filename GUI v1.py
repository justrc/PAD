from tkinter import * #import all of tkinter tools

class Converter:#"Foo" and "bar" are just silly names  popularised by MIT about 1969
    def __init__(self):
       
        # Formatting variables
        background_color = "purple"
       
        # Converter Main SCreen GUI
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)  
        self.converter_frame.grid()
       
        # Weight Conversion Heading (row 0)
        self.weight_converter_label = Label(self.converter_frame, text="Weight converter",
                                            font=("Arial", "16", "bold"),
                                            bg=background_color,
                                            padx=10, pady=10)
        self.weight_converter_label.grid(row=0)
       
        # Help Button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial","14"),
                                  padx=10, pady=10,)
        self.help_button.grid(row=1)
       
def help(self):
    print ("You asked for help.")
    get_help = Help(self)
    get_help.help_text.configure(text="Help text goes here.")
   
class Help:
    def __init__(self,partner):
       
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
       
    def close_help(self,partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()
       
if __name__ == "__main__":
    root =Tk()
    root.title("Weight converter")
    something = Converter()
    root.mainloop()
   
def __init__(self):
   
    # Formatting variables
    background_color = "purple"
   
    # Converter frame
    self.converter_frame = Frame (width=300, bg=background_color,
                                  pady=10)
    self.converter_frame.grid()
   
    # Weight converter heading (row 0)
    self.weight_heading_label = Label(self.converter_frame,
                                      text="Weight Converter",
                                      font="Arial 16 bold",
                                      bg=background_color,
                                      padx=10, pady=10)
    self.weight_converter_label.grid(row=0)
   
    # User instructions (row 1)
    self.weight_instructions_label = Label(self.converter_frame,
                                           text="Type in the amount to be"
                                                "converted and then push"
                                                "one of the buttons below...",
                                           font="Arial 10 italic", wrap=250,
                                           justify=LEFT, bg=background_color,
                                           padx=10, pady=10)
    self.weight.instructions_label.grid(row=1)
   
    # Weight entry box (row 2)
    self.to_convert_entry = Entry(self.converter_frame, width=20,
                                  font="Arial 14 bold")
    self.to_convert_entry.grid(row=2)
   
    # Conversion buttons frame (row 3), orchid3 | khaki1
    self.conversion_buttons_frame = Frame(self.converter_frame)
    self.conversion_buttons_frame.grid(row=3, pady=10)
   
    self.to_p_button = Button(self.conversion_buttons_frame,
                              text="To Pounds", font="Arial 10 bold",
                              bg="red", padx=10, pady=10)
    self.to_p_button.grid(row=0, column=0)
   
    self.to_k_button = Button(self.conversion_buttons_frame,
                              text="To Kilograms", font="Arial 10 bold",
                              bg="blue", padx=10, pady=10)
    self.to_k_button.grid(row=0, column=1)
   
    # Answer label (row 4)
    self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                 fg="purple", bg=background_color,
                                 pady=10, text="Conversion goes here")
    self.converted_label.grid(row=4)
   
    # History / Help button frame (row 5)
    self.hist_help_frame = Frame(self.converter_frame)
    self.hist_help_frame.grid(row=5, pady=10)
   
    self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                   text="Calculation History", width=15)
    self.calc_hist_button.grid(row=0, column=0)
   
    self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                              text="Help", width=5)
    self.help_button.grid(row=0, column=1)
   
def to_p(from_k):
    pounds = (from_k * 2.205)
    return pounds

# Main Routine
weights = [20,40,85]
converted = []

for item in weights:
    answer= to_p(item)
    ans_statement = "{} Kilograms is {} Pounds".format(item.answer)
    converted.append(ans_statement)
   
print(converted)

