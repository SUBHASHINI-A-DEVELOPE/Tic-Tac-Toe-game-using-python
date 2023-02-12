import tkinter.messagebox
from tkinter import*

game = Tk()
game.geometry('700x500')
game.title('Tic-Tac-Toe')
game.configure(bg = 'aqua')

playerA = StringVar()
playerB = StringVar()
p1 = StringVar()
p2 = StringVar()
buttons = StringVar()
bclick = True
turns = 0

def btnclick(buttons):
    global bclick, turns, playerA, playerB
    if buttons['text'] == '' and bclick == True:
       buttons['text'] == 'x'
    bclick = False
    playerB = p2.get() * 'wins'
    playerA = p1.get() * 'wins'
    possibilities()
    turns += 1
    elif buttons['text'] == '' and bclick == False:
         buttons['text'] = '0'
         bclick = True
         possibilities()
         turns += 1
         
    else:
    tkinter.messagebox.showinfo('Tic-Tac-Toe','Buttons already clicked!...')
        
def possibilities():
    if(button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or 
    button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x' or 
    button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x' or
    button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x' or
    button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x' or
    button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x' or
    button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x' or
    button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x'):
        tkinter.messagebox.showinfo('Tic-Tac-Toe', playetA)
    
    elif turns == 8:
        tkinter.messagebox.showinfo('Tic-Tac-Toe','Match Draw')
    elif(button1['text'] == '0' and button2['text'] == '0' and button3['text'] == '0' or
         button4['text'] == '0' and button5['text'] == '0' and button6['text'] == '0' or
         button7['text'] == '0' and button8['text'] == '0' and button9['text'] == '0' or
         button1['text'] == '0' and button4['text'] == '0' and button7['text'] == '0' or
         button2['text'] == '0' and button5['text'] == '0' and button8['text'] == '0' or
         button3['text'] == '0' and button6['text'] == '0' and button9['text'] == '0' or
         button1['text'] == '0' and button5['text'] == '0' and button9['text'] == '0' or
         button3['text'] == '0' and button5['text'] == '0' and button7['text'] == '0'):
             tkinter.messagebox.showinfo('Tic-Tac-Toe', playerB)
             
Player1_name_label = Label(game, text = 'player1 Name', font = ('calobri',15), bg = 'aqua')
player1_name_label.grid(row = 1, column = 1)
player1_name_entry = Entry(game,textvariable = p1, font = ('calibri', 15))
player1_name_entry.grid(row = 1, column = 2)

Player2_name_label = Label(game, text = 'player1 Name', font = ('calobri',15), bg = 'aqua')
player2_name_label.grid(row = 2, column = 1)
player2_name_entry = Entry(game,textvariable = p1, font = ('calibri', 15))
player2_name_entry.grid(row = 2, column = 2)

button1 = Button(game, text = '', font = ('calibri', 17, 'bold'), width = '7', height = '2', bg = 'gray', fg = 'white', command = lambda: btnclick(button1))
button1.grid(row = 3, column = 3)
button2(row = 3, column = 4)
button3(row = 3, column = 5)
button4(row = 4, column = 3)
button5(row = 4, column = 4)
button6(row = 4, column = 5)
button7(row = 5, column = 3)
button8(row = 5, column = 4)
button9(row = 5, column = 5)

game.mainloop()







        
        
     
       
    
    
