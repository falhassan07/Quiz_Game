from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: 0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1, row=0)


        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.create_text(150, 125, text="Some dummy text", font=("arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)



        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)






        self.window.mainloop()



