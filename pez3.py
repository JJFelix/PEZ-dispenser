from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x400")
window.title("PEZ Candy Dispenser")

canvas = Canvas(window)
canvas.pack()
candyStack = []

#draw candy dispenser
def drawCandyDispenser():
    canvas.create_rectangle(150,20,225,250, outline="black", width=3)
    # canvas.pack()
    drawSpring(x=180)


#draw spring
def drawSpring(x): # (x) ->parameter x for flexible height
    # canvas.create_rectangle(152,x,223,248, fill="blue")
    canvas.create_rectangle(152,x,223,248, fill="blue")
    # canvas.pack()

def drawCandy(y0, y1): #(x0, y0, x1, y1) --> y0 and y1 for dynamicity
    global candy
    candy = canvas.create_oval(152,y0,223,y1, fill="brown")
    canvas.pack()

def delete_candy():
    canvas.delete(candy)

# STACK OPERATIONS
def push(candy, y0, y1):
    messagebox.showinfo("Success", f"Pushed {candy} into Dispenser")
    drawCandy(y0, y1)

def pop():
    if isEmpty():
        # messagebox.showerror("Error", "Dispenser is Empty")
        pass
    else:
        popped_candy = candyStack.pop()
        length = len(candyStack)
        while length >= 0:
            if length == 7:
                # y0, y1 = 40, 60
                # drawCandy(y0, y1)
                delete_candy()
                break
            elif length == 6:
                # y0, y1 = 60, 80
                # drawCandy(y0, y1)
                delete_candy()
                break
            elif length == 5:
                # y0, y1 = 80, 100
                # drawCandy(y0, y1)
                delete_candy()
                break
            elif length == 4:
                y0, y1 = 100, 120
                drawCandy(y0, y1)
                break
            elif length == 3:
                # y0, y1 = 120, 140
                # drawCandy(y0, y1)
                delete_candy()
                break
            elif length == 2:
                # y0, y1 = 140, 160
                # drawCandy(y0, y1)
                delete_candy()
                break
            elif length == 1:
                # y0, y1 = 160, 180
                # drawCandy(y0, y1)
                delete_candy()
                break
            else:
                drawCandyDispenser()
                break

        messagebox.showinfo("Success", f"Popped {popped_candy}")
        
    print(candyStack)
    # messagebox.showinfo("Success", f"Popped {popped_candy} from Dispenser")

def isEmpty():
    candyStack_length =  len(candyStack)
    if candyStack_length == 0:
        messagebox.showerror("Error", "Dispenser is Empty")
    else:
        messagebox.showinfo("Success","Dispenser has Candy")
    return candyStack_length == 0

def top():
    if isEmpty():
        pass
    else:
        top_candy = candyStack[-1]
        messagebox.showinfo("Success", f"Topmost candy is {top_candy}")

def size():
    dispenser_size = len(candyStack)
    messagebox.showinfo("Success", f"Dispenser has {dispenser_size} candy(ies)")
    return dispenser_size


# LISTENERS
def push_listener():
    input = text_push.get("1.0", "end-1c")
    candyStack.append(input)

    length = len(candyStack)
    candy = candyStack.index(input)
    print(f'{input} --> ',length)
    while candy < length:
        if input == candyStack[candy] and candy == 0:
            y0, y1 = 160, 180
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 1:
            y0, y1 = 140, 160
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 2:
            y0, y1 = 120, 140
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 3:
            y0, y1 = 100, 120
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 4:
            y0, y1 = 80, 100
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 5:
            y0, y1 = 60, 80
            push(input, y0, y1)
            break
        elif input == candyStack[candy] and candy == 6:
            y0, y1 = 40, 60
            push(input, y0, y1)
            break  
        elif input == candyStack[candy] and candy == 7:
            y0, y1 = 20, 40
            push(input, y0, y1)
            break
        else:
            messagebox.showerror("Error", "Dispenser is full")
            candyStack.pop()
            break

    print(candyStack)


def pop_listener():
    input = text_pop.get("1.0", 'end-1c')
    if input == "pop":
        pop()
        


def top_listener():
    input = text_top.get("1.0", "end-1c")
    if input == "top":
        top()


def is_empty_listener():
    input = text_isempty.get("1.0", "end-1c")
    if input == "is empty":
        isEmpty()


def size_listener():
    input = text_size.get("1.0", "end-1c")
    if input == "size":
        size()


# TEXT_FIELDS
text_push = Text(window, height=1, width=15)
text_push.place(x=350, y=30)

text_pop = Text(window, height=1, width=15)
text_pop.place(x=350, y=70)

text_top = Text(window, height=1, width=15)
text_top.place(x=350, y=110)

text_isempty = Text(window, height=1, width=15)
text_isempty.place(x=350, y=150)

text_size = Text(window, height=1, width=15)
text_size.place(x=350, y=190)


drawCandyDispenser()
# drawSpring(x=180)
# drawSpring(180)

#BUTTONS
Button(window, text="PUSH", command=push_listener).place(x=170, y=30)
Button(window, text="POP", command=pop_listener).place(x=180, y=70)
Button(window, text="TOP", command=top_listener).place(x=180, y=110)
Button(window, text="ISEMPTY", command=is_empty_listener).place(x=150, y=150)
Button(window, text="SIZE", command=size_listener).place(x=180, y=190)

Button(window, text="QUIT", command=window.destroy, bg="red").pack(side="bottom", pady=30)

window.mainloop()