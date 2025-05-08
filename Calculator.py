import tkinter as tk
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("310x380")  
root.resizable(0, 0)
result=StringVar()
display=Entry(root,textvariable=result,justify='right',bg='white',fg='black',font=('lucida',20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text='7',font=('lucida',12,'bold'),bg='white',fg='black',height=2,width=6)
btn7.grid(row=1,column=0)
btn8=Button(root,text='8',font=('lucida',12,'bold'),bg='white',fg='black',height=2,width=6)
btn8.grid(row=1,column=1)
btn9=Button(root,text='9',font=('lucida',12,'bold'),bg='white',fg='black',height=2,width=6)
btn9.grid(row=1,column=2)
btn_add=Button(root,text='+',font=('lucida',12,'bold'),bg='white',fg='black',height=2,width=6)
btn_add.grid(row=1,column=3)

root.mainloop()