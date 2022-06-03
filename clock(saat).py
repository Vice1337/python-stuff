import tkinter
from time import strftime
top = tkinter.Tk()
top.title('Saat (Clock)')
top.resizable(0,0)

def time(): 
    string = strftime('%H:%M:%S %p') 
    clockTime.config(text = string) 
    clockTime.after(1000, time)


clockTime = tkinter.Label(top, font = ('calibri', 45, 'bold'), background = 'white', foreground = 'red')

clockTime.pack(anchor = 'center')
time() 


top.mainloop()
