from tkinter import *
root=Tk()
root.geometry('400x400')
root.title('INteger')
root.config(bg='WHite')


h=int(input('Enter a number: '))
h.pack()
h2=int
(input('Enter 2nd number: '))
h2.pack()

def c1():
    g=h+h2
    print("The sum of given number is: ", g)
    
b1=Button(root,text='Submit',command=c1)
b1.pack()

root.mainloop()