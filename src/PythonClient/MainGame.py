
import Tkinter as tk


mainGameWindow = tk.Tk()
mainGameWindow.title('GAME WINDOW')
mainGameWindow.geometry('500x600')

frame = tk.Frame(mainGameWindow)

# Create roboto formatted label


def createRobotoFont(_frame, text="", color="", size=12, style="", height=0):
    label = tk.Label(
        _frame,
        text=text,
        fg=color,
        font="Roboto {0} {1}".format(size, style),
        height=height
    )
    return label


# Initialize tries
triesCount = 0

# Create method for making 'XXXX' String


def formatTriesInText(_triesCount):
    triesInText = ""
    for i in range(_triesCount):
        triesInText += "X"
    return triesInText


triesCountLabel = createRobotoFont(
    frame,
    text=formatTriesInText(triesCount),
    size=15,
    style="bold",
    color="#E75A7C"
)

triesCountLabel.grid(row=0, column=2)
triesCountLabel.pack()

menuButton = tk.Button(
    text="menu",
    width=22,
    height=2,
    bg="#F2F5EA"
)

frame.place(anchor=tk.CENTER)
frame.pack()
mainGameWindow.mainloop()
