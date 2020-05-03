# import the modules
import tkinter
import random
import re

# list of possible colours
colours = ['Red','Blue','Green','Pink','Black',
		'Yellow','Orange','Purple','Brown','Gray']
score = 0
filepath = open(r"words_score.txt", "r+")

highscore = filepath.read()
highscore = highscore.strip()

highscore = int(highscore)

# the game time left, initially 30 seconds.
timeleft = 30

# function that will start the game.
def startGame(event):
	if timeleft == 30:
		# start the countdown timer.
		countdown()
	# run the function to
	# choose the next colour.
	if timeleft > 0:
		start_btn.config(state='disabled')
		nextColour()
		root.bind('<Return>', startGame)
	
#play again function
def play_again(event):
	global timeleft
	global score
	score=0
	timeleft=30
	startGame(entry.get())

# Function to choose and
# display the next colour.
def nextColour():

	# use the globally declared 'score'
	# and 'play' variables above.
	global score
	global timeleft

	# if a game is currently in play
	if timeleft > 0:

		# make the text entry box active.
		entry.focus_set()

		# if the colour typed is equal
		# to the colour of the text
		if entry.get().lower() == colours[1].lower():
			score += 1

		# clear the text entry box.
		entry.delete(0, tkinter.END)

		random.shuffle(colours)

		# change the colour to type, by changing the
		# text _and_ the colour to a random colour value
		label.config(fg = str(colours[1]), text = str(colours[0]))

		# update the score.
		scoreLabel.config(text = "Score: " + str(score))


# Countdown timer function
def countdown():

	global timeleft

	# if a game is in play
	if timeleft > 0:

		# decrement the timer.
		timeleft -= 1

		# update the time left label
		timeLabel.config(text = "Time left: "
							+ str(timeleft))

		# run the function again after 1 second.
		timeLabel.after(1000, countdown)
	elif timeleft == 0:
		start_btn.config(state='active', text='Play again', command=lambda: play_again(entry.get()))
		

# Driver Code

# create a GUI window
root = tkinter.Tk()

# set the title
root.title("COLOR GAME")
#set the geometry
root.geometry("600x600")

#set the frames
frame1=tkinter.Frame(root)
frame1.place(relheight=0.7,relwidth=1)

frame=tkinter.Frame(root)
frame.place(rely=0.7,relheight=0.3,relwidth=1)
# add an instructions label
instructions = tkinter.Label(frame1, text = "Type in the colour in which the words are written,\nand not the actual word text!",font = ('Helvetica', 12))
instructions.place(relx=0.2, rely=0.02, relwidth=0.6)

#previous highscore label
previous_highscore = tkinter.Label(frame1, text="Previous HighScore: "+str(highscore), font=('Helvetica', 12))
previous_highscore.place(relx=0.2, relwidth=0.6,rely=0.2)

# add a score label
scoreLabel = tkinter.Label(frame1,font = ('Helvetica', 12))
scoreLabel.place(relx=0.2,relwidth=0.6, rely=0.3)

# add a time left label
timeLabel = tkinter.Label(frame1, text = "Time left: " +str(timeleft), font = ('Helvetica', 12))

timeLabel.place(relx=0.2,relwidth=0.6, rely=0.4)

# add a label for displaying the colours
label = tkinter.Label(frame1, font = ('Helvetica', 60))
label.place(relx=0.2, relwidth=0.6, rely=0.5, relheight=0.2)

# add a text entry box for
# typing in colours
entry = tkinter.Entry(frame1)

# run the 'startGame' function
# when the enter key is pressed
entry.place(relx=0.2, relwidth=0.6, rely=0.75,relheight=0.05)

# set focus on the entry box
entry.focus_set()
if timeleft < 0:
	entry.config(state='disabled')
	

#start button
start_btn = tkinter.Button(frame, text="Start", state='active', command=lambda: startGame(entry.get()))
start_btn.place(relx=0.275,relwidth=0.2,relheight=0.2)

#close button
close_btn = tkinter.Button(frame, text="Close", command=root.destroy)
close_btn.place(relx=0.525,relwidth=0.2,relheight=0.2)
# start the GUI
root.mainloop()

if score > highscore:
	# str_score = str(score)
	# filepath.write(str_score)
	wr = open("words_score.txt", 'w')
	wr.write(str(score))
	# filepath.truncate()
	# file_path.write(str(score))
