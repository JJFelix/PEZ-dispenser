from tkinter import *
# from turtle import color

root = Tk()

root.title('Candy Dispenser')

canvas = Canvas(root, width = 700, height = 700, bg='orange')
canvas.grid(column=0, row=0, pady=20, padx=20)

actionsFrame = LabelFrame(root)
actionsFrame.grid(row=0, column=1)

canvas.create_line(120, 650, 480, 650, width=10)
canvas.create_line(120, 650, 120, 30, width=5)
canvas.create_line(480, 650, 480, 30, width=5)

k = 50
candy_h = 30

start_point_x = 120
start_point_y = 650

def draw_spring(start_point_x, start_point_y, k):
    i = 0
    level = 7
    while i <= level:
        canvas.create_line(start_point_x, start_point_y, 480, start_point_y - k, width=5)
        canvas.create_line(480, start_point_y-k, 120, start_point_y - k - k/2, width=5)
        if i == level:
            canvas.create_line(120, start_point_y - k - k/2, 480, start_point_y - k - k/2, width=5)

        i = i+1
        start_point_y = start_point_y - k - k/2
    return start_point_y

def draw_candy(start_point_x, start_point_y, h, number_of_candies):
    i = 0
    while i < number_of_candies:
        canvas.create_oval(start_point_x, start_point_y-(h*(i+1)), 480, start_point_y-(h*i), width=4, outline='black', fill='purple')
        text_x = (start_point_x + 480)/2
        text_y = ((start_point_y-(h*(i+1))) + (start_point_y-(h*i))) / 2

        canvas.create_text(text_x, text_y, text=f"Candy {i+1}", fill="black", font=('Helvetica 15 bold'))
        i= i+1

draw_spring(start_point_x, start_point_y, k)

candy_stack = []

def push():
    canvas.delete('all')
    canvas.create_line(120, 650, 480, 650, width=10)
    canvas.create_line(120, 650, 120, 30, width=5)
    canvas.create_line(480, 650, 480, 30, width=5)
    candy_stack.insert(0, 1)
    print(len(candy_stack))
    k = 50
    k = k - len(candy_stack)*2.5
    candy_start_point_y = draw_spring(start_point_x, start_point_y, k)
    draw_candy(start_point_x, candy_start_point_y, candy_h, len(candy_stack))

    # if size_label['text'] != '':
    #     size()

    # if top_label['text'] != '':
    #     top()

    # if size_label['text'] != '':
    #     size()
    


buttonPush = Button(actionsFrame, text='Push', command=push)
buttonPush.grid(row=1, column=0, padx=20, pady=20)

print(candy_stack)

def pop():
    if(len(candy_stack) > 0):
        canvas.delete('all')
        candy_stack.pop(len(candy_stack)-1)
    canvas.create_line(120, 650, 480, 650, width=10)
    canvas.create_line(120, 650, 120, 30, width=5)
    canvas.create_line(480, 650, 480, 30, width=5)
    print(len(candy_stack))
    k = 50
    k = k - len(candy_stack)*2.5
    candy_start_point_y = draw_spring(start_point_x, start_point_y, k)
    draw_candy(start_point_x, candy_start_point_y, candy_h, len(candy_stack))

buttonPop = Button(actionsFrame, text='Pop', command=pop)
buttonPop.grid(row=1, column=1, padx=20, pady=20)

isEmpty_label = Label(actionsFrame, text='', fg='black', font=('Helvetica 15 bold'))
isEmpty_label.grid(row=2, column=0, padx=20, pady=20)

def isEmpty():
    l = len(candy_stack)
    value = ''
    if l == 0:
        value = 'True'
    else:
        value = 'False'
        isEmpty_label.config(text= f'Is Empty: {value}')

buttonIsEmpty = Button(actionsFrame, text='Is Empty', command=isEmpty)
buttonIsEmpty.grid(row=3, column=0,padx=20, pady=20)

size_label = Label(actionsFrame, text='', fg='black', font=('Helvetica 15 bold'))
size_label.grid(row=4, column=0, padx=20, pady=20)

def size():
    l = len(candy_stack)
    size_label.config(text = f'Size: {str(l)}')

buttonSize = Button(actionsFrame, text='Size', command=size)
buttonSize.grid(row=5, column=0, padx=20, pady=20)

root.mainloop()