from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x400")
window.title("PEZ Candy Dispenser")

canvas = Canvas(window)

canvas.pack()

candyStack = []

canvas.create_rectangle(150,20,225,250, outline="black", width=3)

initial_spring_position = 20
candy_height = 20
candy_entry_point = 20

#draw spring
def drawSpring(initial_spring_position, shrink_spring_by): 
    i = 0
    length = len(candyStack)
    while i <= length:
        if i == length:
            canvas.create_rectangle(152,initial_spring_position + (shrink_spring_by * i) ,223,248, fill="blue")  
            # new_spring_position = initial_spring_position + (shrink_spring_by * i)  
        i += 1

    # return new_spring_position

drawSpring(initial_spring_position, candy_height)


def drawCandy(initial_spring_position, candy_height, no_of_candies):
    i = 0
    while i < no_of_candies:
        canvas.create_oval(152,initial_spring_position+(candy_height*i),223, initial_spring_position+(candy_height*(i+1)), fill="brown")     
        i += 1

# STACK OPERATIONS
def push(): 
    canvas.delete("all")
    canvas.create_rectangle(150,20,225,250, outline="black", width=3)
    length = len(candyStack)
    if length < 11:
        candyStack.append("candy")
        candy_height = 20
        drawSpring(initial_spring_position, candy_height )
        print(f'Pushed candy {len(candyStack)} into dispenser') 
        drawCandy(candy_entry_point,candy_height, len(candyStack))
        messagebox.showinfo("Success", f"Pushed candy {len(candyStack)} into Dispenser")
        print(candyStack)
    else:
        # messagebox.showerror("Error", "Dispenser is full")
        candy_height = 20
        drawSpring(initial_spring_position, candy_height )
        drawCandy(candy_entry_point,candy_height, len(candyStack))
        messagebox.showerror("Error", "Dispenser is full")
        print(candyStack)

    
def pop():
    if ( len(candyStack) == 0):
        messagebox.showerror("Error", "Dispenser is empty")
    else:
        canvas.delete("all")
        length_before_popping = len(candyStack)
        candyStack.pop()
    canvas.create_rectangle(150,20,225,250, outline="black", width=3)

    initial_spring_position = candy_entry_point
    candy_height = 20
    drawSpring(initial_spring_position,candy_height)
    print(f'Popped candy {length_before_popping} from dispenser')
    drawCandy(candy_entry_point, candy_height, len(candyStack) )
    messagebox.showinfo("Success", f"Popped candy {length_before_popping} from dispenser")
    print(candyStack)

    
def isEmpty():
    candyStack_length =  len(candyStack)
    if candyStack_length == 0:
        messagebox.showerror("Error", "Dispenser is Empty")
    else:
        messagebox.showinfo("Success","Dispenser is not Empty")
    return candyStack_length == 0

def top():
    if (len(candyStack) != 0):
        top_candy = candyStack[-1]
        messagebox.showinfo("Success", f"Topmost candy is candy {len(candyStack)}")
    else:
        messagebox.showerror("Error", "Dispenser is empty")
    return top_candy 

def size():
    dispenser_size = len(candyStack)
    messagebox.showinfo("Success", f"Dispenser has {dispenser_size} candy(ies)")
    return dispenser_size

#BUTTONS
Button(window, text="PUSH", command=push).place(x=170, y=30)
Button(window, text="POP", command=pop).place(x=180, y=70)
Button(window, text="TOP", command=top).place(x=180, y=110)
Button(window, text="ISEMPTY", command=isEmpty).place(x=150, y=150)
Button(window, text="SIZE", command=size).place(x=180, y=190)

Button(window, text="QUIT", command=window.destroy, bg="red").pack(side="bottom", pady=30)

window.mainloop()