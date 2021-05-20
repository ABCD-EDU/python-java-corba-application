import Tkinter as tk
from Tkinter import *
import ORBConnector as oc
import sys

# create orb connection
con = oc.ORBConnector(sys.argv)

currName = ""
currScore = 0
lives = 5
root = None
class ScreenController(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInScreen, GameScreen, ResultScreen):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SignInScreen.__name__)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        global root
        frame.tkraise()        
        return frame

class GameScreen(Frame):
    def __init__(self, master=None, controller=None):
        Frame.__init__(self, master)
        self.controller = controller
        self.configure(bg="#F2F5EA")
        self.gridsize = 30
        self.grid(padx=self.gridsize)
        self.pack()
        self.createGameScreen()

    def submitWordPress(self):
        global con
        global currName
        isCorrect = con.getEO().checkAnswer(currName, self.guessEntry.get())
        if isCorrect:
            self.guessEntry.delete(0,'end')
            self.requestWord()
            self.rerollWord()
            self.requestScore()
            self.guessEntry.configure(text="")
            self.resultMessageLabel['fg'] = "#F2F5EA"
        else:
            self.deductTries();
            self.resultMessageLabel['fg'] = "#E75A7C"

    def deductTries(self):
        global lives
        if (lives != 0):
            lives -= 1
            currLives = self.triesCountLabel.cget("text")
            if lives < 2:
                self.gridsize -= 10
                if lives < 1:
                    self.gridsize -= 3
                self.grid(padx=self.gridsize)
            self.triesCountLabel['text'] = currLives + 'X'
        else:
            lives = 5
            self.gridsize = 30
            self.resultMessageLabel['fg'] = "#F2F5EA"
            frame = self.controller.show_frame(ResultScreen.__name__)
            frame.initData(frame)

    def requestWord(self):
        global currName
        global con

        newWord = con.getEO().requestWord(currName)
        if newWord == "":
            frame = self.controller.show_frame(ResultScreen.__name__)
            frame.initData(frame)
        self.scrambledWordLabel.config(text=newWord)

    def rerollWord(self):
        global currName
        global con

        scrambledWord = con.getEO().requestRescramble(currName)
        self.scrambledWordLabel.config(text=scrambledWord)

    def requestScore(self):
        global currName
        global currScore
        global con

        currScore = con.getEO().requestScore(currName) 
        self.userScoreLabel.config(text="Score : {1}".format(1,currScore))

    def menuButtonPress(self):
        global currScore
        global currName
        global lives
        lives = 5
        currName = ""
        currScore = 0
        self.controller.show_frame(SignInScreen.__name__)

    def createGameScreen(self):
        # Tries label
        self.triesCountLabel = tk.Label(
            self,
            text="X",
            font="Roboto 30 bold",
            fg="#E75A7C",
            bg="#F2F5EA"
        )

        self.triesCountLabel.grid(row=0, column=2, pady=(30,0))
        # End of tries label...

        # Score label
        self.userScoreLabel = tk.Label(
            self,
            text="Score: ",
            font="Roboto 12 bold",
            fg="#000000",
            bg="#F2F5EA"
        )
        self.userScoreLabel.grid(row=1, column=2, pady=(5, 10), padx=(10,10))

        self.menuButton = tk.Button(
            self,
            command=self.menuButtonPress,
            text="menu",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )
        self.menuButton.grid(row=2, column=0, columnspan=1, pady=(10, 10))
        # # End of menu button

        # Reroll
        self.rerollButton = tk.Button(
            self,
            command=self.rerollWord,
            text="reroll",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )
        self.rerollButton.grid(row=2, column=5, columnspan=1, pady=(10, 10))
        # end of reroll

        # Scramble Label
        self.scrambleLabel = tk.Label(
            self,
            text="Scrambled Word:",
            font="Roboto 15 normal",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        self.scrambleLabel.grid(row=3, column=0, columnspan=8, pady=(0, 2),  padx=(10,10))
        # End of scramble label

        # Scramble word to guess label
        self.scrambledWordLabel = tk.Label(
            self,
            text="none",
            font="Roboto 25 bold",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        self.scrambledWordLabel.grid(row=4, column=0, columnspan=8, pady=(2,0), padx=(10,10))
        # End scrambled word to guess label

        # Input Guess Prompt Label
        self.guessPromptLabel = tk.Label(
            self,
            text="Enter your Answer:",
            font="Roboto 15 normal",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        self.guessPromptLabel.grid(row=6, column=0, columnspan=6, pady=(30, 2), padx=(10,10))
        # End prompt

        # User guess entry
        self.guessEntry = tk.Entry(
            self,
            font=('Roboto', 20, 'normal'),
            bg="#F2F5EA", 
            width=25
            )
        self.guessEntry.grid(row=7, column=0, columnspan=6, pady=(2, 5), padx=(10,10))
        # End

        self.submitButton = tk.Button(
            self,
            command=self.submitWordPress,
            text="SUBMIT!",
            width=30,
            heigh=1,
            font=('Roboto', 12, 'bold'),
            bg="#E75A7C",
            fg="#fff"
        )

        self.submitButton.grid(row=8, column=0, columnspan=6, pady=(5, 10), padx=(10,10))
        # End

        # result message label
        self.resultMessageLabel = tk.Label(
            self,
            text= "Wrong answer. Try again!",
            font="Roboto 12 bold",
            fg="#F2F5EA",
            bg="#F2F5EA"
        )
        self.resultMessageLabel.grid(row=9, column=0, columnspan=8, pady=(20,20), padx=(10,10))
        # End result

    @staticmethod
    def initData(self):
        global currName
        if currName is not "":
            self.requestWord()
            self.rerollWord()
            self.requestScore()

            self.grid(padx=self.gridsize)
            self.guessEntry.delete(0,'end')
            self.triesCountLabel.configure(text="")
            self.resultMessageLabel['fg'] = "#F2F5EA"

class SignInScreen(Frame):
    def __init__(self, master=None, controller=None):
        Frame.__init__(self, master)
        self.controller=controller
        self.configure(bg="#F2F5EA")
        self.pack()
        self.createSignInScreen()
    
    def loginClick(self):
        name = self.userEntry.get()
        if name: 
            global currName
            currName = name

            global con
            con.getEO().logIn(name)

            # change window
            frame = self.controller.show_frame(GameScreen.__name__)
            frame.initData(frame)

    def createSignInScreen(self):
        # creates the word scrambler label
        gameLabel = Label(
            self,
            text="WORD SCRAMBLER",
            fg="#2C363F",
            font="Roboto 30 bold",
        )

        gameLabel.pack(pady=(100,30), padx=(60,60))

        #creates the login textfield
        self.userEntry = tk.Entry(
            self,
            bg="#F2F5EA",
            width=50)
        self.userEntry.pack(pady=(20,20))

        #creates the login button
        playButton = tk.Button(
            self,
            command=self.loginClick,
            text="PLAY!",
            width=42,
            heigh=2,
            bg="#E75A7C",
            fg="#fff"
        )
        playButton.pack(pady=(0,50))   

class ResultScreen(Frame):
    def __init__(self, master=None, controller=None):
        Frame.__init__(self, master)
        self.controller = controller
        self.configure(bg="#F2F5EA")
        self.pack()
        self.createResultScreen()

    @staticmethod
    def initData(self):
        global currScore
        global currName

        global con
        currScore = con.getEO().requestScore(currName)
        self.scoreLabel['text'] = "Final Score: {1}".format(1, currScore)

    def exitButtonPress(self):
        global currName
        global currScore
        global lives

        lives = 5
        currName = ""
        currScore = 0

        self.controller.show_frame(SignInScreen.__name__)
    
    def playAgainPress(self):
        frame = self.controller.show_frame(GameScreen.__name__)
        frame.initData(frame)

    def createResultScreen(self):
         # creates the score label
        self.scoreLabel = Label(
            self,
            text="Final Score: 0",
            fg="#2C363F",
            bg="#F2F5EA",
            font="Roboto 15 bold",
        )

        self.scoreLabel.pack(pady=(70,15), padx=(100,100))

         # creates the score label
        self.endLabel = Label(
            self,
            text="GAME OVER!",
            fg="#E75A7C",
            bg="#F2F5EA",
            font="Roboto 30 bold",
        )

        self.endLabel.pack(pady=(0,15), padx=(100,100))

        self.playAgainButton = tk.Button(
            self,
            command=self.playAgainPress,
            text="play again",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )
        self.playAgainButton.pack(padx=(100,100))

        self.exitButton = tk.Button(
            self,
            command=self.exitButtonPress,
            text="exit",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )

        self.exitButton.pack(pady=(10,30), padx=(100,100))

if __name__ == "__main__":
    root = ScreenController()
    root.configure(bg="#F2F5EA")
    root.resizable(False, False)
    root.geometry("580x540")
    root.mainloop()
    root.destroy()
