from tkinter import *
from tkinter.ttk import *
import requests
from tkinter import messagebox
root=Tk()
root.title('News Checker App')
root.geometry("500x300")

def getCode():
    pass
country_label=Label(root,text="Enter Country Name:",font=('bold',10)).place(x=620,y=80)
countryText=StringVar()
countryInput=Entry(root,textvariable=countryText)
countryInput.place(x=750,y=79)

goButton=Button(root,text="Go",width=12,command=getCode)
goButton.place(x=715,y=100)

newsLabel=Label(root,text='',font=('bold',10))
newsLabel.place(x=615,y=200)
root.mainloop()