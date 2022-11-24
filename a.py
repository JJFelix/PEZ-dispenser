from email import message
from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("700x600")
window.resizable(0,0)
window.configure(background="grey")
window.title("Candy Dispenser Project")
#image1
# icon1 = PhotoImage(file = "C:/Users/HP/Downloads/sweets.png")
# image1 = Label(window,bg="pink")
# image1.place( x=200,y=30,height=100,width=100)
#image2
# icon2 = PhotoImage(file = "C:/Users/HP/Downloads/sweets.png")
# image2 = Label(window,bg="pink")
# image2.place( x=800,y=30,height=100,width=100)

# m =Label(window,text="CANDY DISPENSER",font=("Arial",30),bg="white")
# m.pack()
# m.place(x=300,y=50,height=60,width=500)
# b =Label(window,text="PRESS A BUTTON",font=("Arial",14),bg="white")
# b.place(x=20,y=150)
#buttons
import turtle
x = turtle.Turtle()
#drawing container
x.color("blue")
x.up()
x.goto(-100,-90)
x.forward(200)
x.left(90)
x.forward(200)
x.pendown()
x.backward(370)
x.left(90)
x.forward(200)
x.right(90)
x.forward(370)
x.up()
x.home()

#drawing spring
def draw_rect(x,y,color,fd):
    z.up()
    z.goto(x,y)
    z.down()
    z.begin_fill()
    z.fillcolor(color)
    z.forward(50)
    z.right(90)
    z.forward(fd)
    z.right(90)
    z.forward(50)
    z.right(90)
    z.forward(fd)
    z.right(90)
    z.end_fill()
    z.up()
    z.home()

#drawing candy
def draw_circle(x,y,rad,color):
    c.goto(x,y)
    c.down()
    c.begin_fill()
    c.fillcolor(color)
    c.circle(rad)
    c.end_fill()
    c.up()
    c.home()

c = turtle.Turtle()
c.up()
z= turtle.Turtle()


#func for compressing spring lowering it
def compress_spring():
    current_rectsize = s.size()
    # return 350 - (40*current_rectsize)
    if current_rectsize == 1:
        bottom = 350 -(40*current_rectsize)+15
    elif current_rectsize == 2:
        bottom = 350 -(40*current_rectsize)+10
    elif current_rectsize == 3:
        bottom = 350 -(40*current_rectsize)+5
    elif current_rectsize == 4:
        bottom = 350 -(40*current_rectsize)
    elif current_rectsize == 5:
        bottom = 350 -(40*current_rectsize)-5
    elif current_rectsize == 6:
        bottom = 350 -(40*current_rectsize)-10
    elif current_rectsize == 7:
        bottom = 350 -(40*current_rectsize)-15
    elif current_rectsize == 8:
        bottom = 350 -(40*current_rectsize)-20
    return bottom

def lower_rectpos():
    current_pos =s.size()
    return 91 -(40*current_pos)
def clear_func():
    z.clear()
#func for compressing spring lowering it
def relax_spring():
    current_rectsize = s.size()
    # return 220 +(-20*current_rectsize)+150

    if current_rectsize == 0:
        bottom = 220 + (-20*current_rectsize)+150
    elif current_rectsize == 1:
        bottom = 220 + (-20*current_rectsize)+125
    elif current_rectsize == 2:
        bottom = 220 + (-20*current_rectsize)+100
    elif current_rectsize == 3:
        bottom = 220 + (-20*current_rectsize)+75
    elif current_rectsize == 4:
        bottom = 220 + (-20*current_rectsize)+50
    elif current_rectsize == 5:
        bottom = 220 + (-20*current_rectsize)+25
    elif current_rectsize == 6:
        bottom = 220 + (-20*current_rectsize)
    elif current_rectsize == 7:
        bottom = 220 + (-20*current_rectsize)-25
    
    return bottom 

def lift_rectpos():
    current_pos =s.size()
    return -40-(30*current_pos)
draw_rect(-30, 91, "blue", 350)

class Stack:
    def __init__(self):
     self.items =[]

    def is_empty(self):
        return self.items==[]

    def push(self,item):
        if s.size() ==8:
            # turtle.write("stack is full", align="center", font=("Cooper Black", 25, "italic"))
            messagebox.showerror("Error", "Stack is full")
        else:
            self.items.append(item) 
            z.clear()
            draw_circle(-5, change(), 15, "green")
            draw_rect(-30, change(), "blue", compress_spring())
           

    def pop(self):        
        if s.size() == 0:
            c.clear()
            messagebox.showerror("Error", "Stack is empty")            
        else:
            # popped = self.items.pop()
            erase()
            # c.clear()
            popped = self.items.pop()
            z.clear()
            # i = 0
            # if i < s.size():
            #     # erase()
            #     draw_rect(-30, change(), "blue", relax_spring())
            #     x1 = draw_circle(-5, (change()+(45*i)), 15, "green")  
            #     # x2 = draw_circle(-5, (change()+(45*i+1)), 15, "green")           
            #     # x1.undo()

            # else:
            #     # erase()
            #     draw_rect(-30, change(), "blue", relax_spring())
            #     draw_circle(-5, change(), 15, "green")
                # erase()
                
            draw_circle(-5, change(), 15, "green")
            draw_rect(-30, change(), "blue", relax_spring())
            
        return popped

    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

s = Stack()

def change():
    current_size = s.size()
    if current_size == 1:
        return 110 - (60 * current_size) +15
    else:
        return 110 - (45 * current_size)

q= s.size()

def erase():
    for i in range(7+q):
    # for i in s.items:
    #     if i == s.size():
        c.undo()
            # c.clear()
def finish():
    # res = txt.get()
    s.push("candy")
def do_pop():
    s.pop()

def do_top():
    p=s.peek()
    top_val= Label(window, text=p, bg="white")
    top_val.place(x=250, y=300,width=80, height=80)
def do_size():
    a = s.size()
    size_val = Label(window, text=a, bg="white")
    size_val.place(x=360, y=300, width=80, height=80)

def do_empty():
    b= s.is_empty()
    d= "Yes" if b else "No"
    size_val = Label(window, text=d, bg="white")
    size_val.place(x=470, y=300, width=80, height=80)

def clicked():
    prompt =Label(window,text="enter value to be pushed",bg="white")
    prompt.place(x=32,y=310)

def close_window():
    window.destroy()
    exit()

push=Button(window,text ="PUSH",bg="white",font=("Arial",8),command=finish)
push.place(x=30,y=220,width=70,height=30,)

func=Label(window,text="PUSH VALUE",bg="white")
func.place(x=30,y=280)

txt=Entry(window,width=15)
txt.place(x=32,y=320)

# finish=Button(window,text ="PUSH",bg="white",font=("Arial",8),command=finish)
# finish.place(x=32,y=370,width=70,height=30)

pop=Button(window,text ="POP",bg="white",font=("Arial",8),command=do_pop)
pop.place(x=160,y=220,width=70,height=30)

top=Button(window,text ="TOP",bg="white",font=("Arial",8),command=do_top)
top.place(x=250,y=220,width=70,height=30)

size=Button(window,text ="SIZE",bg="white",font=("Arial",8),command=do_size)
size.place(x=360,y=220,width=70,height=30)

isempty=Button(window,text ="IS EMPTY?",bg="white",font=("Arial",8),command=do_empty)
isempty.place(x=470,y=220,width=70,height=30)

close=Button(window,text ="QUIT",bg="white",font=("Arial",8),command=close_window)
close.place(x=580,y=220,width=70,height=30)

turtle.done()
window.mainloop()


