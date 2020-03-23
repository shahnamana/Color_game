import tkinter as tk
import random
import os


def word_color_game_function():
	os.system('python words_game.py')


def shape_color_game_function():
	os.system('python shape_game.py')


main = tk.Tk()

main.title("Choice Window")


word_choice = tk.Button(main, text="Word Game", command = word_color_game_function).pack()
shape_choice = tk.Button(main, text="Shape Game", command = shape_color_game_function).pack()
main.geometry("375x200")

if word_choice or shape_choice:
	main.destroy()

main.mainloop()

# print(type(highscore_words_game))
