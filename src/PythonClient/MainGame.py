
# import Tkinter as tk
# from tkinter import ttk
import Tkinter as tk


mainGameWindow = tk.Tk()
mainGameWindow.title('GAME WINDOW')
mainGameWindow.geometry('500x600')
mainGameWindow.resizable(0, 0)

frame = tk.Frame(mainGameWindow, bg="#F2F5EA")

# Initialize Global Variables
triesCount = 2
userScore = 300
scrabledWord = "COEFR"


# Create method for making 'XXXX' String
def formatTriesInText(_triesCount):
    triesInText = ""
    for i in range(_triesCount):
        triesInText += "X"
    return triesInText


# Tries label
triesCountLabel = tk.Label(
    frame,
    text=formatTriesInText(triesCount),
    font="Roboto 30 bold",
    fg="#E75A7C",
    bg="#F2F5EA"
)

triesCountLabel.grid(row=0, column=2, pady=(30, 10), padx=(20, 0))
# End of tries label...

# Score label
formattedScore = 'Score: %s' % userScore
userScoreLabel = tk.Label(
    frame,
    text=formattedScore,
    font="Roboto 12 bold",
    fg="#000000",
    bg="#F2F5EA"
)
userScoreLabel.grid(row=1, column=2, pady=(10, 10), padx=(20, 0))

# End of score label

# # Menu button


def goToMenu():
    pass


menuButton = tk.Button(
    frame,
    command=goToMenu(),
    text="menu",
    font="Roboto 12 bold",
    bg="#F2F5EA",
    fg="#000000",
    width=20,
    borderwidth=0
)
menuButton.grid(row=2, column=0, columnspan=1, pady=(10, 10))
# # End of menu button

# Reroll
rerollButton = tk.Button(
    frame,
    command=goToMenu(),
    text="reroll",
    font="Roboto 12 bold",
    bg="#F2F5EA",
    fg="#000000",
    width=20,
    borderwidth=0
)
rerollButton.grid(row=2, column=5, columnspan=1, pady=(10, 10))
# end of reroll

# Scramble Label
scrambleLabel = tk.Label(
    frame,
    text="Scrambled Word:",
    font="Roboto 15 normal",
    width=0,
    fg="#000000",
    bg="#F2F5EA"
)
scrambleLabel.grid(row=3, column=0, columnspan=8, pady=(30, 2),  padx=(20, 0))
# End of scramble label

# Scramble word to guess label
scrambledWordLabel = tk.Label(
    frame,
    text=scrabledWord,
    font="Roboto 25 bold",
    width=0,
    fg="#000000",
    bg="#F2F5EA"
)
scrambledWordLabel.grid(row=4, column=0, columnspan=8,
                        pady=(2, 10), padx=(20, 0))
# End scrambled word to guess label

# Horizontal line separator
# ttk.Separator(frame, orient=tk.HORIZONTAL).grid(
#     column=0, row=5, columnspan=3)
# End horizontal

# Input Guess Prompt Label
guessPromptLabel = tk.Label(
    frame,
    text="Enter your Answer:",
    font="Roboto 15 normal",
    width=0,
    fg="#000000",
    bg="#F2F5EA"
)
guessPromptLabel.grid(row=6, column=0, columnspan=6,
                      pady=(30, 2), padx=(20, 0))
# End prompt

# User guess entry
guessEntry = tk.Entry(
    frame, 
    font=('Roboto', 20, 'normal'),
    bg="#F2F5EA", 
    width=25
    )
guessEntry.grid(row=7, column=0, columnspan=6, pady=(2, 5), padx=(20, 0))
# End

# Submit Button
def onSubmit():
    pass

submitButton = tk.Button(
    frame,
    command=onSubmit(),
    text="SUBMIT!",
    width=30,
    heigh=1,
    font=('Roboto', 12, 'bold'),
    bg="#E75A7C",
    fg="#fff"
)

submitButton.grid(row=8, column=0, columnspan=6, pady=(5, 10), padx=(20, 0))
# End

# result message label 
resultMessage = "Wrong answer. Try again!"
resultMessageLabel = tk.Label(
    frame,
    text= resultMessage,
    font="Roboto 12 bold",
    fg="#E75A7C",
    bg="#F2F5EA"
)
resultMessageLabel.grid(row=9, column=0, columnspan=8, pady=(20,0), padx=(20,0))
# End result

# frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
frame.pack(expand=True, fill=tk.BOTH)
mainGameWindow.mainloop()
