from tkinter import *
import random

def next_turn(row,col):
    global player
    if buttons[row][col]['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons[row][col]['text'] = player
            if check_winner() == False:
                player = players[1]
                lable.config(text = players[1]+'turn')
            elif check_winner() == True:
                lable.config(text=players[0] + 'wins')
            elif check_winner()=='Tie':
                lable.config(text='its a draw')
        else:
            buttons[row][col]['text'] = player
            if check_winner() == False:
                player = players[0]
                lable.config(text=players[0] + 'turn')
            elif check_winner()==True:
                lable.config(text=players[1] + 'wins')
            else:
                lable.config(text='its a draw')



    # pass

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text']==buttons[i][2]['text']!='':
            buttons[i][0].config(bg="green")
            buttons[i][1].config(bg="green")
            buttons[i][2].config(bg="green")
            return True
    for j in range(3):
        if buttons[0][j]['text'] == buttons[1][j]['text']==buttons[2][j]['text']!='':
            buttons[0][j].config(bg='green')
            buttons[1][j].config(bg='green')
            buttons[2][j].config(bg='green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        buttons[0][2].config(bg='black')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    if empty_spaces():
        return False
    else:
        return 'Tie'
    # return False
    # pass

def empty_spaces():
    spaces = 9
    for i in range(3):
        for j in range(3):
            if buttons[i][j]['text'] != '':
                spaces-=1
    if spaces==0:
        return False
    else:
        return True
    # pass

def new_game():
    global player
    player = random.choice(players)
    lable.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#F0F0F0')

window = Tk()
window.title("Tic-Tac-Toe")
players = ["$","%"]
player =random.choice(players)

buttons = [[None, None, None], [None, None, None], [None, None, None]]

lable = Label(text = player+'Turn',font = ('consolas',40))
lable.pack(side = 'top')
reset_button = Button(text='restart', font=('consola', 20), command=new_game)
reset_button.pack(side='top')


frame = Frame(window)
frame.pack()
for i in range(3):
    for j in range(3):
        buttons[i][j]= Button(frame,text = '',font = ('consolas',40),width=3,height=2,command = lambda row = i,column = j: next_turn(row,column))
        buttons[i][j].grid(row=i,column=j)


window.mainloop()
