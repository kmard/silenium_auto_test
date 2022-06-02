from tkinter import *

start = True
lastcommand = '='
resul = 0

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("+{0}+{1}".format(x, y))

def click(text):
    global start
    global lastcommand
    global display
    if text.isdigit() or text == '.':
        if start:
            display.configure(text='')
            start=False
        if text != '.' or display.cget('text').find('.') == -1:
             display.configure(text=(display.cget('text')+text))
    else:
        if start:
            lastcommand = text
        else:
            calculate(float(display.cget('text')))
            lastcommand = text
            start=True

def calculate(x):
    global lastcommand
    global resul
    global display

    if lastcommand == '+':
        resul+=x
    elif lastcommand == '-':
        resul-=x
    elif lastcommand == '*':
        resul *= x
    elif lastcommand == '/':
        try:
            resul /= x
        except ZeroDivisionError:
            pass

    elif lastcommand == '=':
        resul = x
    display.configure(text=resul)



root = Tk()
setwindow(root)

buttons = (('7','8','9','/'),
           ('4','5','6','*'),
           ('1','2','3','-'),
           ('0','.','=','+'),
           )

display = Label(root, text='0', font="Tahoma 20", bd=10, foreground='white')
display.grid(column=0, row=0, columnspan=4)

for row in range(4):
    for column in range(4):
        button = Button(root,text=buttons[row][column],font="Tahoma 20",command= lambda text=buttons[row][column]:click(text))
        button.grid(row=row+1,column=column,padx=5, pady=5,ipady=20,ipadx=20,sticky='nsew')



root.mainloop()