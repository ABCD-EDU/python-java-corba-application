import Tkinter as tk
# import ORBConnector as oc

# create orb connection
# con = oc.ORBConnector()

window = tk.Tk()
window.configure(bg="#F2F5EA")

def createRobotoFont(text="", color="", size=12, style="", height=0):
    label = tk.Label(
        text=text,
        fg=color,
        font="Roboto {0} {1}".format(size,style),
        height=height
    )

    return label

def loginClick(name):
    print(name)
    if name:
        pass
        # con.eo.logIn(name)

    # change window

def createSignInScreen():
    # creates the word scrambler label
    gameLabel = createRobotoFont(
        text="WORD SCRAMBLER",
        size=30, 
        color="#2C363F",
        style="bold",
    )

    gameLabel.pack(pady=(100,30), padx=(60,60))

    # Input user name prompt label
    inputNameLabel = tk.Label()

    #creates the login textfield
    userEntry = tk.Entry(bg="@", width=50)
    userEntry.pack(pady=(20,20))

    #creates the login button
    playButton = tk.Button(
        command=loginClick(userEntry.get()),
        text="PLAY!",
        width=42,
        heigh=2,
        bg="#E75A7C",
        fg="#fff"
    )
    playButton.pack(pady=(0,100))

def run():
    createSignInScreen()
    window.mainloop()    

run()