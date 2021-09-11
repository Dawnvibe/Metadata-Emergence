from tkinter import *

root = Tk()
root.title("MetaData Emergence")
root.configure(background="black")
img = PhotoImage(file='metadata.gif')
root.tk.call('wm', 'iconphoto', root._w, img)
#root.geometry("853x479")
root.attributes('-zoomed', True)

# Creating the Basic Menu Bar Up-Top
my_menu = Menu(root, background="black", foreground="green",
               activebackground="green", activeforeground="black",
               bd="0")
root.config(menu=my_menu)

# Menu Buttons & Commands
def my_command_1():
    pass

# Menu Adding Items
file_menu = Menu(my_menu, tearoff="off", background="black", foreground="green",
                 activebackground="green", activeforeground="black")
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=my_command_1)
file_menu.add_command(label="New Tab", command=my_command_1)
file_menu.add_command(label="New Window", command=my_command_1)
file_menu.add_command(label="Print", command=my_command_1)
file_menu.add_separator()
file_menu.add_command(label="Quit The Emergence", command=root.quit)
#--------------------------------------------------------------------
edit_menu = Menu(my_menu, tearoff="off", background="black", foreground="green",
                 activebackground="green", activeforeground="black")
my_menu.add_cascade(label="Edit", menu=edit_menu)
#--------------------------------------------------------------------
help_menu = Menu(my_menu, tearoff="off", background="black", foreground="green",
                 activebackground="green", activeforeground="black")
my_menu.add_cascade(label="Help", menu=help_menu)
root.mainloop()
