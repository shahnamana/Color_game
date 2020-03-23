import tkinter as tk
import random


colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

with open("shape_score.txt","r+") as f:
    high_score_shape_game = int(f.read())


def startGame():
    pass

main = tk.Tk()
main.title("Shape Game")
timeleft = 0
main.geometry("500x500")

instructions = tk.Label(main, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12)).pack()

scoreLabel = tk.Label(main, text="Press enter to start", font=('Helvetica', 12)).pack()

highscore_label = tk.Label(main, text="Previous High score was "+str(high_score_shape_game), font=('Helvetica', 12)).pack()

timeLabel = tk.Label(main, text="Time left: " +str(timeleft), font=('Helvetica', 12)).pack()


# add a label for displaying the colours
label = tk.Label(main, font=('Helvetica', 60)).pack()

e = tk.Entry(main)

# run the 'startGame' function
# when the enter key is pressed
main.bind('<Return>', startGame)
e.pack(side=tk.BOTTOM)

# set focus on the entry box
e.focus_set()

# start the GUI
main.mainloop()
