from cgitb import reset
from tkinter import *
from classes import *
import numpy as np

stg = Settings()
p1 = Player("Red","x")
p2 = Player("Blue","o")
game =Game(p1.char,p1.color)

board = np.chararray((3,3),unicode=True)


window = Tk()
window.geometry(stg.screen_size)
window.config(bg=stg.bgcolor)
window.title(stg.title)


def game_layout():

    
    p1_leaderboard = Label(window, text=f"Player x\nWin={p1.win}\ntied={p1.tied}",bg=stg.bgcolor,font=stg.text_font )
    p1_leaderboard.place(x=0,y=0)    

    turn_title= Label(window, text=f"Turn {game.turn}",bg=game.turn_color,font=stg.text_font,  width=5 ) 
    turn_title.place(x=200,y=25)

    p2_leaderboard = Label(window, text=f"Player o\nWin={p2.win}\ntied={p2.tied}",bg=stg.bgcolor,font=stg.text_font )
    p2_leaderboard.place(x=380,y=0)


    def change_turn():
        
        if game.turn == p1.char:
            game.turn = p2.char
            game.turn_color=p2.color
            turn_title.config(bg=game.turn_color,text=f"Turn {game.turn}")
            return

        if game.turn == p2.char:
            game.turn=p1.char
            game.turn_color=p1.color
            turn_title.config(bg=game.turn_color,text=f"Turn {game.turn}")
            return
            
        

            

        

    def check_win():

        print(game.count)
        if board[0][0]==game.turn and  board[0][1]==game.turn  and board[0][2]==game.turn :
            win()
        elif board[1][0]==game.turn and  board[1][1]==game.turn  and board[1][2]==game.turn :
            win()
        elif board[2][0]==game.turn and  board[2][1]==game.turn  and board[2][2]==game.turn :
            win()
        
        elif board[0][0]==game.turn and  board[1][0]==game.turn  and board[2][0]==game.turn :
            win()
        elif board[0][1]==game.turn and  board[1][1]==game.turn  and board[2][1]==game.turn :
            win()
        elif board[0][2]==game.turn and  board[1][2]==game.turn  and board[2][2]==game.turn :
            win()


        elif board[0][0]==game.turn and  board[1][1]==game.turn  and board[2][2]==game.turn :
            win()
        elif board[0][2]==game.turn and  board[1][1]==game.turn  and board[2][0]==game.turn :
            win()

        
        elif game.count ==9:
            tied()

    def tied():
        def reset():
            board[:,:]=""
            game.count=0
            reset_window.grab_release()
            reset_window.destroy()
            game_layout()
        p1.tied+=1
        p2.tied+=1

        reset_window = Toplevel()
        reset_text = Label(reset_window,text=f"Tied {game.turn}" , font=stg.text_font)
        reset_text.pack()
        reset_button = Button(reset_window,text="Continue",font=stg.text_font,command=reset)
        reset_button.pack()
        print("tied")
        reset_window.grab_set()

    def win():

        def reset():
            board[:,:]=""
            game.count=0
            reset_window.grab_release()
            reset_window.destroy()
            game_layout()
            

        if game.turn == p1.char:
            p1.win+=1

        else:
            p2.win+=1
        reset_window = Toplevel()
        reset_text = Label(reset_window,text=f"congratulations {game.turn}" , font=stg.text_font)
        reset_text.pack()
        reset_button = Button(reset_window,text="Continue",font=stg.text_font,command=reset)
        reset_button.pack()
        reset_window.grab_set()
    
    def bttn_press(position):
        game.count+=1

        if position ==[[0],[0]]:
            top_left.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[0][0]=game.turn
       
        if position == [[0],[1]]:
            top.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[0][1]=game.turn

        if position == [[0],[2]]:
            top_right.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[0][2]=game.turn
         
        if position ==[[1],[0]]:
            mid_left.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[1][0]=game.turn
           

        if position == [[1],[1]]:
            mid.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[1][1]=game.turn
       
        if position == [[1],[2]]:
            mid_right.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[1][2]=game.turn
        
        if position ==[[2],[0]]:
            btm_left.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[2][0]=game.turn

        if position == [[2],[1]]:
            btm.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[2][1]=game.turn

        if position == [[2],[2]]:
            btm_right.config(text=game.turn,bg=game.turn_color,state=DISABLED)
            board[2][2]=game.turn
            
        check_win()
        change_turn()
   
    top_left =Button(window,font=stg.text_font,command= lambda:bttn_press([[0],[0]]))
    top =Button(window,font=stg.text_font,command= lambda:bttn_press([[0],[1]]))
    top_right =Button(window,font=stg.text_font,command= lambda:bttn_press([[0],[2]]))
    mid_left =Button(window,font=stg.text_font,command= lambda:bttn_press([[1],[0]]))
    mid =Button(window,font=stg.text_font,command= lambda:bttn_press([[1],[1]]))
    mid_right =Button(window,font=stg.text_font,command= lambda:bttn_press([[1],[2]]))
    btm_left =Button(window,font=stg.text_font,command= lambda:bttn_press([[2],[0]]))
    btm =Button(window,font=stg.text_font,command= lambda:bttn_press([[2],[1]]))
    btm_right =Button(window,font=stg.text_font,command= lambda:bttn_press([[2],[2]]))


    ttt_grid = [[top_left,top,top_right],[mid_left,mid,mid_right],[btm_left,btm,btm_right]]
        
    x_position=160
    y_position=160

    for row in range(3):

        for column in range(3):
            ttt_grid[row][column].place (x=x_position,y=y_position, height=70, width=70)
            x_position+=70
        y_position+=70
        x_position=160


def show_menu():

    def start():
        menu_title.destroy()
        menu_start.destroy()
        game_layout()


    menu_title =Label(window, text=f"Tic Tac Toe ",bg=stg.bgcolor,font=stg.title_font)
    menu_title.pack(pady=50)

    menu_start= Button(window, text= f"start", bg=stg.bgcolor,font=(stg.text_font), command=start)
    menu_start.pack(pady=30)

show_menu()
window.mainloop()