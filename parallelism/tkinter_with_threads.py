
import tkinter as tk
from tkinter import ttk
import time 
import threading

flag = False

def runwhile():
	k = 1
	global flag
	flag = True
	while flag:
		print(f'running thread \"{threading.current_thread().name}\"')
		k += 1
		time.sleep(1)

	print(f'While loop from thread \"{threading.current_thread().name}\" is over')

def runthread():
	thread = threading.Thread(target=runwhile)
	thread.start()

def printHello():
	print(f"Hello from \"{threading.current_thread().name}\"")


def stoploop():
	global flag
	flag = False
	print(f"changing flag from \"{threading.current_thread().name}\" ...")
	time.sleep(1.01)
	print(f"threads left: {list(thread.name for thread in threading.enumerate())}")
	

win =  tk.Tk()

butt = ttk.Button(text='start', command=runthread).pack()
butt2 = ttk.Button(text='stop', command=stoploop).pack()

butt3 = ttk.Button(text='printHello', command=printHello).pack()
butt4 = ttk.Button(text='quit', command=win.destroy).pack()



print(f"threads: {threading.enumerate()}")
win.mainloop()
