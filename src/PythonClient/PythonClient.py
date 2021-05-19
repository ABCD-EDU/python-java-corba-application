import Tkinter as tk
from Tkinter import *
# import ORBConnector as oc

# create orb connection
# con = oc.ORBConnector()

class SignInScreen(Frame):
    def loginClick(self, name):
        if name:
            pass
            # con.eo.logIn(name)

        # change window

    def createSignInScreen(self):
        # creates the word scrambler label
        gameLabel = Label(
            text="WORD SCRAMBLER",
            fg="#2C363F",
            font="Roboto 30 bold",
        )

        gameLabel.pack(pady=(100,30), padx=(60,60))

        #creates the login textfield
        userEntry = tk.Entry(bg="#F2F5EA", width=50)
        userEntry.pack(pady=(20,20))

        #creates the login button
        playButton = tk.Button(
            command=self.loginClick(userEntry.get()),
            text="PLAY!",
            width=42,
            heigh=2,
            bg="#E75A7C",
            fg="#fff"
        )
        playButton.pack(pady=(0,100))   

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createSignInScreen()

if __name__ == "__main__":
    root = Tk()
    app = SignInScreen(master=root)
    app.mainloop()
    root.destroy()