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
		windowExit.resizable(False, False) # window'll not size now'
		exitButton = Button(windowExit) # create button
		#button arguments
		exitButton["text"] = "shutdown"
		exitButton["command"] = exit
		exitButton.pack() # start button 
		windowExit.mainloop() # start window
	
	def exit():
		sys.exit(0) #exit from programm

if __name__ == "__main__": # starts rogramm
	root = Tk()
	root.title("mytest") # title window
	root.attributes("-fullscreen", True) # window now fullscreen
	button1 = Button(root) # creating button
	# button arguments
	button1["text"] = "exit"
	button1["command"] = functions.exitMenu # if click on button window'll open'
	button1["bg"] = "red"
	button1["fg"] ="white"
	button1.pack()
	
	root.mainloop()
