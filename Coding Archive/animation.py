from tkinter import *
import time

root_width = 500
root_height = 500

ball_move_x = 10
ball_move_y = 5

time_difference = 0.01

root = Tk()
root.geometry("500x500")
root.resizable(0,0)

canvas = Canvas(root,width=root_width,height=root_height,bg='black')
canvas.place(relx=0.5,rely=0.5,anchor=CENTER)

ball = canvas.create_oval(0,0,100,100,fill='green',outline="white",width=3)

while True:
    ball_coords = canvas.coords(ball)
    x0,y0,x1,y1 = ball_coords
    
    if x1 > root_width or x0 < 0:
        ball_move_x = -ball_move_x
    if y1 > root_height or y0 < 0:
        ball_move_y = -ball_move_y
    
    canvas.move(ball,ball_move_x,ball_move_y)
    time.sleep(time_difference)
    root.update()

