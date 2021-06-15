from tkinter import *
import random
from tkinter import messagebox
from sklearn import preprocessing
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier

Dice1=[1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]
Dice2=[6,2,1,3,3,5,2,3,2,2,5,6,4,2,5,2,3,5,1,2,3,4,2,1,4,5,2,4,5,3]
#Dice3=[2,3,2,1,3,4,5,6,4,4,3,5,3,5,4,3,5,2,2,3,2,4,2,5,1,2,3,4,5,6]
Labels=['low','high','high','low','high','low',
       'high','high','high','low','low','low',
       'low','high','low','low','high','low',
       'high','high','low','high','high','high',
       'low','low','high','high','high','high']
features=list(zip(Dice1,Dice2))
le = preprocessing.LabelEncoder()

# Converting string labels into numbers.
labels=le.fit_transform(Labels)
# print('Prediction high or low', labels )
classifier =DecisionTreeClassifier()
classifier.fit(features,labels)


win = Tk()
can = Canvas(win,bg="white", width=900, height=600)
win.title("Dice Game")
win.configure(bg="white")
win.geometry("900x600")

Diceimg = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
num = random.randint(0,5)
num1 = random.randint(0,5)

DiceLabelRight = Label(win, bg="white", text=f'{Diceimg[num1]}', font=("Arial", 250))
DiceLabelRight.place(x = 660, y = 200)
point = 0


def Clicked(event):
    global DiceLabelRight
    global point
    X = event.x
    Y = event.y
    
    Predict=classifier.predict([[6,6]])
    print(Predict)

    # if X in range(425, 475) and Y in range(115, 335):
    if Predict[0] == 0:
        print("Up")
        indexr = Diceimg.index(DiceLabelRight.cget("text"))
        num1 = random.randint(0, 5)
        if indexr <= num1:
            D1.configure(text=f'{DiceLabelRight.cget("text")}')
            DiceLabelRight.configure(text=f'{Diceimg[num1]}')
            point = point + 1
            Point.configure(text="Streak: {}".format(point))
        else:
            point = 0
            D1.configure(text=f'{DiceLabelRight.cget("text")}')
            DiceLabelRight.configure(text=f'{Diceimg[num1]}')
            Point.configure(text="Streak: {}".format(point))
            

    # if X in range(425, 475) and Y in range(350, 575):
    if Predict[0] == 1:
        print("Down")
        index = Diceimg.index(DiceLabelRight.cget("text"))
        num1 = random.randint(0, 5)
        if index >= num1:
            D1.configure(text = f'{DiceLabelRight.cget("text")}')
            DiceLabelRight.configure(text=f'{Diceimg[num1]}')
            point = point + 1
            Point.configure(text="Streak: {}".format(point))
        else:
            point = 0
            D1.configure(text=f'{DiceLabelRight.cget("text")}')
            DiceLabelRight.configure(text=f'{Diceimg[num1]}')
            Point.configure(text = "Streak: {}".format(point))

    print(num1+1)
    if point == 0:
        messagebox.showinfo("model prediction", "Predicted wrong Lower")
    else:
        messagebox.showinfo("model prediction", "Success streak = " + str(point))


Title = Label(win, bg ="white", text = "Predict if it Will be Higher or Lower!", font = ("Arial", 40))
Title.place( x = 20, y= 20, anchor = NW)
Previous = Label(win, bg = "white", text = "Previous", font = ("Arial",40))
Previous.place(x= 20, y = 130)
D1 = Label(win, bg = "white", text = f'{Diceimg[num]}', font = ("Arial", 250))
D1.place(x = -10, y =200)
Next = Label(win, bg = "white", text = "Now", font = ("Arial", 40))
Next.place(x = 725, y = 130)
Point = Label(win, bg = "white", text = "Streak: {}".format(point) )
Point.place(x = 260, y = 120)

can.place(x=1,y=1)
can.create_line(0,110,900,110)
can.create_rectangle(0,110,250,600)
can.create_rectangle(900,110,650,600)
# can.create_line(450, , 450, 335, width = 50, arrow = FIRST, arrowshape = (50, 60, 40), fill = "red" )
can.create_text(20, 30, anchor=W, font="Purisa", text="predict")
can.create_line(350, 300, 550, 300,  width = 30, fill = "blue" )
can.bind("<Button-1>", Clicked)

win.mainloop()