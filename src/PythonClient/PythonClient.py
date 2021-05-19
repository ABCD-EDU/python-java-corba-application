import Tkinter as tk
from Tkinter import *
import ORBConnector as oc

# create orb connection
con = oc.ORBConnector()

currName = ""
currScore = 0

class ScreenController(Tk):
    def __init__(self):
        Tk.__init__(self)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInScreen, GameScreen, ResultScreen):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SignInScreen.__name__)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()        

class GameScreen(Frame):
    def __init__(self, master=None, controller=None):
        Frame.__init__(self, master)
        self.controller = controller
        self.configure(bg="#F2F5EA")
        self.pack()
        self.createGameScreen()

    def submitWordPress(self):
        global con
        global currName
        isCorrect = con.checkAnswer(currName, self.guessEntry.get())
        if

    def menuButtonPress(self):
        print('test')
        self.controller.show_frame(SignInScreen.__name__)

    def rerollButtonPress(self):
        pass

    def createGameScreen(self):
        # Tries label
        triesCountLabel = tk.Label(
            self,
            text="X",
            font="Roboto 30 bold",
            fg="#E75A7C",
            bg="#F2F5EA"
        )

        triesCountLabel.grid(row=0, column=2, pady=(30,0), padx=(10,10))
        # End of tries label...

        # Score label
        userScoreLabel = tk.Label(
            self,
            text="Score: ",
            font="Roboto 12 bold",
            fg="#000000",
            bg="#F2F5EA"
        )
        userScoreLabel.grid(row=1, column=2, pady=(5, 10), padx=(10,10))

        menuButton = tk.Button(
            self,
            command=self.menuButtonPress,
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
            self,
            command=self.rerollButtonPress,
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
            self,
            text="Scrambled Word:",
            font="Roboto 15 normal",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        scrambleLabel.grid(row=3, column=0, columnspan=8, pady=(0, 2),  padx=(10,10))
        # End of scramble label

        # Scramble word to guess label
        scrambledWordLabel = tk.Label(
            self,
            text="none",
            font="Roboto 25 bold",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        scrambledWordLabel.grid(row=4, column=0, columnspan=8, pady=(2,0), padx=(10,10))
        # End scrambled word to guess label

        # Input Guess Prompt Label
        guessPromptLabel = tk.Label(
            self,
            text="Enter your Answer:",
            font="Roboto 15 normal",
            width=0,
            fg="#000000",
            bg="#F2F5EA"
        )
        guessPromptLabel.grid(row=6, column=0, columnspan=6, pady=(30, 2), padx=(10,10))
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

        submitButton = tk.Button(
            self,
            # command=onSubmit(),
            text="SUBMIT!",
            width=30,
            heigh=1,
            font=('Roboto', 12, 'bold'),
            bg="#E75A7C",
            fg="#fff"
        )

        submitButton.grid(row=8, column=0, columnspan=6, pady=(5, 10), padx=(10,10))
        # End

        # result message label
        resultMessageLabel = tk.Label(
            self,
            text= "Wrong answer. Try again!",
            font="Roboto 12 bold",
            fg="#E75A7C",
            bg="#F2F5EA"
        )
        resultMessageLabel.grid(row=9, column=0, columnspan=8, pady=(20,20), padx=(10,10))
        # End result

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
            con.eo.logIn(name)

            # change window
            self.controller.show_frame(ResultScreen.__name__)

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

    def menuButtonPress():
        self.controller.show_frame(GameScreen.__name__)

    def createResultScreen(self):
         # creates the score label
        scoreLabel = Label(
            self,
            text="Final Score: 0",
            fg="#2C363F",
            font="Roboto 15 bold",
        )

        scoreLabel.pack(pady=(70,15), padx=(100,100))

         # creates the score label
        endLabel = Label(
            self,
            text="GAME OVER!",
            fg="#E75A7C",
            font="Roboto 30 bold",
        )

        endLabel.pack(pady=(0,15), padx=(100,100))

        menuButton = tk.Button(
            self,
            command=self.menuButtonPress,
            text="menu",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )
        menuButton.pack(padx=(100,100))

        exitButton = tk.Button(
            self,
            command=self.menuButtonPress,
            text="exit",
            font="Roboto 12 bold",
            bg="#F2F5EA",
            fg="#000000",
            width=20,
            borderwidth=0
        )

        exitButton.pack(pady=(10,30), padx=(100,100))

if __name__ == "__main__":
    root = ScreenController()
    root.configure(bg="#F2F5EA")
    root.resizable(False, False)
    root.geometry("580x540")
    root.mainloop()
    root.destroy()
