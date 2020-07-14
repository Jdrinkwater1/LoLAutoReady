#Jacob Drinkwater
#AutoReady app
#7/13/20

from tkinter import *
import pyautogui, time,threading
root = Tk()
root.title("LoLAutoReady v1.5")
def readySearch():

    done = False
    count = 0

    #look for the accept button on screen, click it if it is 50% accurate
    while not done:
        acceptLocation=pyautogui.locateCenterOnScreen(accept, minSearchTime=9999, confidence=.5)
        pyautogui.click(acceptLocation)
        readyString.set("Pressed the accept button")
        done = True
    #increment the count
    count += 1
    #if the count is not zero start the thread
    if (count < 1):
        t1.start()
    #run the thread if already started
    t1.run()

#if it finds the search denied picture restart the readysearch
def denied():
        pyautogui.locateOnScreen(denied,minSearchTime=12,confidence=.7)
        readySearch()

#close the program
def exitHit():
    exit()







t1 = threading.Thread(target=denied)
readyString = StringVar()
denied = "denied.png"
accept = "Ready.png"

#Setting up the labels/buttons
titleLabel= Label(root,text="AutoReady v1.5")
readyButton= Button(root,text="Ready",padx=40,command=readySearch)
exitButton= Button(root,text="Exit",padx=40,command=exitHit)
readyLabel= Label(root,textvariable=readyString)
#Placing the labels and buttons onto the app
titleLabel.grid(row=0,column=1)
readyButton.grid(row=1,column=0)
exitButton.grid(row=1,column=2)
readyLabel.grid(row=2,column=1)






root.mainloop()



