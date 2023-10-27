import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def NewFile():
    text = tk.Text(tab_control)
    tab_control.add(text, text="Untitled")
    tab_control.select(tab_control.index(tk.END))

def savefile():
    current_tab = tab_control.select()
    text_widget = tab_control.nametowidget(current_tab)
    t = text_widget.get("1.0", tk.END)
    filename = tab_control.tab(tab_control.select(), "text")
    
    if filename == "Untitled":
        saveAs()
    else:
        with open(filename, 'w') as f:
            f.write(t)

def saveAs():
    current_tab = tab_control.select()
    text_widget = tab_control.nametowidget(current_tab)
    t = text_widget.get("1.0", tk.END)
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if f is not None:
        try:
            f.write(t.rstrip())
            tab_control.tab(current_tab, text=f.name)
        except:
            tk.showerror(title="Oops!", message="Unable to save file...")

def openFile():
    f = filedialog.askopenfile(mode='r')
    if f is not None:
        text = tk.Text(tab_control)
        t = f.read()
        text.insert("1.0", t)
        tab_control.add(text, text=f.name)
        tab_control.select(tab_control.index(tk.END))

root = tk.Tk()
root.title("Text Editor")
root.minsize(width=400, height=400)

tab_control = ttk.Notebook(root)

# Initial Tab
text = tk.Text(tab_control)
tab_control.add(text, text="Untitled")

tab_control.pack(expand=1, fill="both")

menubar = tk.Menu(root)

filemenu = tk.Menu(menubar)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
