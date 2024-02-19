from tk import *
import random
import sys


def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")
def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg='#39ff14', foreground='black')
            buttons[row][1].config(bg='#39ff14', foreground='black')
            buttons[row][2].config(bg='#39ff14', foreground='black')
            return buttons[row][0]

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg='#39ff14', foreground='black')
            buttons[1][column].config(bg='#39ff14', foreground='black')
            buttons[2][column].config(bg='#39ff14', foreground='black')
            return buttons[0][column]

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='#39ff14', foreground='black')
        buttons[1][1].config(bg='#39ff14', foreground='black')
        buttons[2][2].config(bg='#39ff14', foreground='black')
        return buttons[0][0]

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='#39ff14', foreground='black')
        buttons[1][1].config(bg='#39ff14', foreground='black')
        buttons[2][0].config(bg='#39ff14', foreground='black')
        return buttons[0][2]

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="grey")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    label.config(text="x" + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", foreground='white', background='black')


window = Tk()
window.title("Tic-Tac-Toe")
window.minsize(550, 635)
window.maxsize(550, 635)
players = ["x","o"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text="x" + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=new_game, background='black', foreground='#39ff14',
                      activebackground='#39ff14', activeforeground='black')
reset_button.pack(side="top")
frame = Frame(window)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, foreground='white', background='black', text="", font=('consolas', 40),
                                      width=6, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column),
                                      activebackground='#39ff14')
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
