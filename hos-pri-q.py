from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.geometry("920x650")
window.title("Hospital Queue")

buttonFrame = LabelFrame(window)
buttonFrame.place(x=150, y=350)

canvas = Canvas(window, width=890, height=200, bg='lightblue')
canvas.place(x=15, y=100)

door = ImageTk.PhotoImage(Image.open('door.jpeg').resize((75, 175)))
label = Label(window, image=door)
label.place(x=20, y=110)

desk = ImageTk.PhotoImage(Image.open("desk.png").resize((100,175)))
label = Label(window, image=desk)
label.place(x=800, y=110)

person1 = ImageTk.PhotoImage(Image.open("person.jpeg").resize((40,40)))

row = 2
column = 7
data = [[] *7 for i in range(row)]

def draw_person_canvas(i):
    key_input = input_key.get("1.0", "end-1c")
    value_input = input_value.get("1.0", "end-1c")
    x = 1
    while x <= i:
        canvas.create_oval(800-(i*50),30,810-(i*50),40)  # head
        canvas.create_line(805-(i*50),40, 805-(i*50), 45) # neck
        canvas.create_rectangle(798-(i*50),45, 812-(i*50), 65) # body
        canvas.create_line(798-(i*50), 45, 793-(i*50), 55) # left arm
        canvas.create_line(812-(i*50), 45, 817-(i*50), 55) # right arm
        canvas.create_line(802-(i*50), 65, 802-(i*50), 85) # left leg
        canvas.create_line(808-(i*50), 65, 808-(i*50), 85) # right leg
        canvas.create_line(798-(i*50), 85, 803-(i*50), 85) # left foot
        canvas.create_line(808-(i*50), 85, 813-(i*50), 85) # right foot
        x+=1
    text_x = 850 - (x*50)
    text_y = 150
    canvas.create_text(text_x, text_y, text=f"{value_input}:{key_input}", fill="black", font=('Helvetica 8 bold'))

def draw_person_canvas_after_remove_min(j):
    canvas.delete("all")
    x = 0
    while x < j:
        for i in range(0, j+1):
            canvas.create_oval(800-(i*50),30,810-(i*50),40)  # head
            canvas.create_line(805-(i*50),40, 805-(i*50), 45) # neck
            canvas.create_rectangle(798-(i*50),45, 812-(i*50), 65) # body
            canvas.create_line(798-(i*50), 45, 793-(i*50), 55) # left arm
            canvas.create_line(812-(i*50), 45, 817-(i*50), 55) # right arm
            canvas.create_line(802-(i*50), 65, 802-(i*50), 85) # left leg
            canvas.create_line(808-(i*50), 65, 808-(i*50), 85) # right leg
            canvas.create_line(798-(i*50), 85, 803-(i*50), 85) # left foot
            canvas.create_line(808-(i*50), 85, 813-(i*50), 85) # right foot
        text_x = 750 - (x*50)
        key = data[0][x]
        value = data[1][x]
        x+=1
        canvas.create_text(text_x, 150, text=f"{value}:{key}", fill="black", font=('Helvetica 8 bold'))

def insert(): 
    key_input = input_key.get("1.0", "end-1c")
    value_input = input_value.get("1.0", "end-1c")

    length = len(data[0])
    if length < 14:
        data[0].append(key_input)
        data[1].append(value_input)
        draw_person_canvas(len(data[0])) #, key_input, value_input)           
    else:
        messagebox.showwarning("Wait", "Queue is currently full")
    print(data)
    print(f"length of queue: {len(data[0])}\n")

def get_min():
    length = len(data[0])
    if length == 0:
        messagebox.showerror("Error","Nobody is in the queue currently")
    else:
        min_key = min(data[0])
        index_of_min = data[0].index(min_key)
        min_value = data[1][index_of_min]
        messagebox.showinfo("Success", f"Highest priority is {min_value} with priority {min_key}")
        return f"Min priority: {min_value}: {min_key}"

def remove_min():
    if len(data[0]) == 0:
        messagebox.showerror("Error", "No one in the queue")
    else:
        min_key = min(data[0])
        index_of_min = data[0].index(min_key)
        removed_key = data[0].pop(index_of_min)
        removed_value = data[1].pop(index_of_min)
        print(f'After removing min: {data}')
        draw_person_canvas_after_remove_min(len(data[0]))
        messagebox.showinfo("Success", f"Removed {removed_value}: {removed_key}")
        return f'Removed {removed_value} with key {removed_key}'

def replace_key():
    key_input = input_key.get("1.0", "end-1c")
    replace_key = input_value.get("1.0", "end-1c")

    if key_input not in data[0]:
        messagebox.showerror("Error", f"Key {key_input} not found")
    else:
        index_of_key = data[0].index(key_input)
        data[0][index_of_key] = replace_key
        print(f"After changing key {key_input} to {replace_key} -> {data}")
        draw_person_canvas_after_remove_min(len(data[0]))
        messagebox.showinfo("Success", f"Key {key_input} changed to {replace_key}")
        return key_input

def replace_value():
    value_input = input_key.get("1.0", "end-1c")
    replace_value = input_value.get("1.0", "end-1c")

    if value_input not in data[1]:
        messagebox.showerror("Error", f"Value {value_input} not found")
    else:
        index_of_value = data[1].index(value_input)
        data[1][index_of_value] = replace_value
        print(f"After changing value {value_input} to {replace_value} -> {data}")
        draw_person_canvas_after_remove_min(len(data[0]))
        messagebox.showinfo("Success", f"Value {value_input} changed to {replace_value}")
        return value_input

def remove():
    key_input = input_key.get("1.0", "end-1c")

    if key_input not in data[0]:
        messagebox.showerror("Error", f"Key {key_input} not found")
    else:
        index_of_key_to_remove = data[0].index(key_input)
        removed_key = data[0].pop(index_of_key_to_remove)
        removed_value = data[1].pop(index_of_key_to_remove)
        print(f"After removing {removed_value}:{removed_key} -> {data}")
        draw_person_canvas_after_remove_min(len(data[0]))
        messagebox.showinfo("Success", f"Removed {removed_value}:{removed_key}")
        return f'Removed {removed_value} with key{removed_key}'
        
def size():
    length = len(data[0])
    messagebox.showinfo("Success", f"Number of people in queue is {length}")

def is_empty():
    length = len(data[0])
    value = ''
    if length == 0:
        value = 'True'
        messagebox.showinfo("Success", "Queue is empty")
    else:
        value = 'False'
        messagebox.showwarning("Error", "Queue is not empty")

QuitButton = Button(buttonFrame, text="QUIT", command=window.destroy )
QuitButton.grid(row=3, column=0, padx=20, pady=20)

InsertButton = Button(buttonFrame, text="INSERT", command=insert )
InsertButton.grid(row=1, column=1, padx=20, pady=20)

GetMinButton = Button(buttonFrame, text="GET MIN", command=get_min)
GetMinButton.grid(row=1, column=2, padx=20, pady=20)

RemoveMinButton = Button(buttonFrame, text="REMOVE MIN", command=remove_min)
RemoveMinButton.grid(row=1, column=3, padx=20, pady=20)

ReplaceKeyButton = Button(buttonFrame, text="REPLACE KEY", command=replace_key)
ReplaceKeyButton.grid(row=2, column=0, padx=20, pady=20)

ReplaceValueButton = Button(buttonFrame, text="REPLACE VALUE", command=replace_value )
ReplaceValueButton.grid(row=2, column=1, padx=20, pady=20)

RemoveButton = Button(buttonFrame, text="REMOVE", command=remove)
RemoveButton.grid(row=2, column=2, padx=20, pady=20)

SizeButton = Button(buttonFrame, text="SIZE", command=size)
SizeButton.grid(row=2, column=3, padx=20, pady=20)

IsEmptyButton = Button(buttonFrame, text="IS EMPTY", command=is_empty )
IsEmptyButton.grid(row=1, column=0, padx=20, pady=20)

text_label = Label(buttonFrame, text='', fg='black', font=('Helvetica 15 bold'))
text_label.grid(row=3, column=1, padx=20, pady=20)

input_text = Label(buttonFrame, text="Enter key:")
input_text.grid(row=3, column=2, padx=20, pady=20)

input_text = Label(buttonFrame, text="Enter value:")
input_text.grid(row=4, column=2, padx=20, pady=20)

input_key = Text(buttonFrame, height=1, width=15)
input_key.grid(row=3, column=3, padx=20, pady=20)

input_value = Text(buttonFrame, height=1, width=15)
input_value.grid(row=4, column=3, padx=20, pady=20)

window.mainloop()



# def draw_person(i, input_key, input_value):
# def draw_person(i):
#     key_input = input_key.get("1.0", "end-1c")
#     value_input = input_value.get("1.0", "end-1c")
#     x = 1
#     while x <= i:
#         label = Label(window, image=person1)
#         l = 800 - (x*50)
#         label.place(x=l, y=170) 
#         x+=1

#     text_x = 850 - (x*50)
#     text_y = 150

#     canvas.create_text(text_x, text_y, text=f"{value_input}:{key_input}", fill="black", font=('Helvetica 8 bold'))


# def draw_person_after_remove_min(i):
#     canvas.delete("all")
#     person1 = ImageTk.PhotoImage(Image.open("./person.jpeg").resize((40,40)))
#     # key_input = input_key.get("1.0", "end-1c")
#     # value_input = input_value.get("1.0", "end-1c")

#     x = 0
#     while x < i:
#         label = Label(window, image=person1)
#         l = 700 - ((x)*50)
#         label.place(x=l, y=170) 

#         text_x = 750 - (x*50)
#         key = data[0][x]
#         value = data[1][x]
#         x+=1

#     # text_x = 850 - (x*50)
#         canvas.create_text(text_x, 150, text=f"{value}:{key}", fill="black", font=('Helvetica 8 bold'))

