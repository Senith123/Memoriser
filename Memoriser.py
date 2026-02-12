from tkinter import*
from tkinter.filedialog import*
screen = Tk()
screen.geometry("500x500")
screen.title("Memoriser")
screen.config(background = 'dark olive green')

def add_item():
    item = entry.get()
    list.insert(END, item)
    entry.delete(0, END)
def delete_item():
    item = list.curselection()
    list.delete(item)
def save_item():
    file = asksaveasfile(defaultextension = ".txt")
    for item in list.get(0,END):
        print(item, file = file)
    list.delete(0, END)
def open_item():
    file = askopenfile(title = "open file")
    if file is not None:
        list.delete(0, END)
        items = file.readlines()
        for item in items:
            list.insert(END, item.strip())

open = Button (screen, text = "OPEN", bg = "olive drab", fg = "dark sea green", font = ("times", 20, "bold"), command = open_item)
open.place(x = 10, y = 10)
delete = Button (screen, text = "DELETE", bg = "olive drab", fg = "dark sea green", font = ("times", 20, "bold"), command = delete_item)
delete.place(x = 195, y = 10)
save = Button (screen, text = "SAVE", bg = "olive drab", fg = "dark sea green", font = ("times", 20, "bold"), command = save_item)
save.place(x = 395, y = 10)
entry = Entry(bd = 5, bg = "olive drab", fg = "dark sea green", width = 20, font = ("times", 26, "bold"))
entry.place(x = 10, y = 85)
add = Button (screen, text = " ADD ", bg = "olive drab", fg = "dark sea green", font = ("times", 20, "bold"), command = add_item)
add.place(x = 395, y = 85)
frame = Frame(screen)
scroll = Scrollbar(frame, orient = "vertical")
scroll.pack(side = RIGHT, fill = Y)
list = Listbox(frame, width = 76, height = 16, yscrollcommand = scroll.set, bg = "olive drab")
for i in range(1,100):
    list.insert(END, i)
list.pack(side = LEFT)
scroll.config(command = list.yview)
frame.place( x = 10, y = 200)
screen.mainloop()
