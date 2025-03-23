from tkinter import *
import sys
import time

#def update_time(self):
#	# Получить текущее время
#	current_time = time.strftime("%H:%M:%S")
#	self.time_label.config(text=current_time)
#	# Обновить время каждые 1000 мс (1 секунда)
#	self.root.after(1000, self.update_time)

#создание класса функции
#тут будут приложения и функции
class functions: 
	def printer(event):
		newWindow = Toplevel()
		newWindow.title("hello, window")
		
		button2 = Button(newWindow, text="hello").pack()
		newWindow.mainloop()
	
	def exitMenu(event=None):
		windowExit = Toplevel() #create window
		# window arguments
		windowExit.title("exit from system") # name window
		windowExit.geometry("300x150") # size window
		windowExit.resizable(False, False) # window'll not size now
		#buttons
		exitButton = Button(windowExit) # create button
		#button arguments
		exitButton["text"] = "shutdown"
		exitButton["command"] = exit
		exitButton.pack() # start button 
		windowExit.mainloop() # start window
	def startMenu(event=None):
		windowStartMenu = Toplevel()
		#start menu arguments
		windowStartMenu.title("start") # name window 
		windowStartMenu.geometry("200x300") # size window
		windowStartMenu.resizable(False, False) # window'll not siz now
		
		#buttons
		button1 = Button(windowStartMenu) # creating button
		# button arguments
		button1["text"] = "shutdown"
		button1["command"] = functions.exitMenu # if click on button window'll open'
		button1["bg"] = "red" # background is red
		button1["fg"] ="white" # color text is white
		button1.place(y = 0, x = 0) # start button & place
		windowStartMenu.mainloop() # start window
	
	def exit():
		sys.exit(0) #exit from programm

if __name__ == "__main__": # starts rogramm
	root = Tk()
	root.title("mytest") # title window
	root.attributes("-fullscreen", True) # window now fullscreen
	#buttons
	
	
	buttonStart = Button(root) # create button
	buttonStart["text"] = "start" # button name is "start"
	buttonStart.bind("<Button-1>", functions.startMenu) # if click on button, window'll open
	buttonStart.place(y = 0, x = 0) # start button & place
	
	root.mainloop()
