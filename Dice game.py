from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("!Endless Dice Game!")
root.geometry("600x400")

root.configure(background="Black")
img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

P1=Label(root,text="Player 1",bg="Black",fg="White",font=("Arial",18))
P1.place(relx=0.2,rely=0.3,anchor=CENTER)

P2=Label(root,text="Player 2",bg="Black",fg="White",font=("Arial",18))
P2.place(relx=0.8,rely=0.3,anchor=CENTER)

P1_score=Label(root,bg="Black",fg="White",font=("Arial",18))
P1_score.place(relx=0.2,rely=0.4,anchor=CENTER)

P2_score=Label(root,bg="Black",fg="White",font=("Arial",18))
P2_score.place(relx=0.8,rely=0.4,anchor=CENTER)

dice=Label(root,bg="Blue",fg="White",font=("Arial",18))
dice.place(relx=0.5,rely=0.5,anchor=CENTER)

def play_game():
    print("This is a function")
    
btn_1=Button(root,text="Player 1",command=play_game)
btn_1.place(relx=0.2,rely=0.6,anchor=CENTER)

btn_2=Button(root,text="Player 2",command=play_game)
btn_2.place(relx=0.8,rely=0.6,anchor=CENTER)


root.mainloop()

