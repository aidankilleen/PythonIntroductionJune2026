# tk_investigation.py

from tkinter import Tk, messagebox
import tkinter as tk

from userdao import UserDao

# PyQt is a more-modern alternative to tk

root = Tk()
root.geometry("600x400")

# on_click is an event handler that gets called when the "command" in the button is 
# activated
def on_click():
    messagebox.showinfo("Clicked", "You clicked the button")
    print ("clicked")
    pass

# widgets - controls that go on the screen
btn = tk.Button(root, text="Press Me", command=on_click)
btn.pack(pady=20)

def on_item_selected(event):
    index = listbox.curselection()[0]
    user = users[index]
    messagebox.showinfo("clicked", user)

listbox = tk.Listbox(root)
listbox.bind("<<ListboxSelect>>", on_item_selected)
listbox.pack(pady=20)

dao = UserDao()

users = dao.get_users()

for user in users:
    listbox.insert(tk.END, user.name)

def on_delete():
    # delete the currently selected user
    index = listbox.curselection()[0]
    user = users[index]
    if messagebox.askyesno("Delete", user):
        # delete the item from the database
        dao.delete_user(user.id)

        # delete the item from the listbox
        listbox.delete(index)

        # there are some bugs in this code!
        

btn_delete = tk.Button(root, text="Delete", command=on_delete)
btn_delete.pack(pady=20)


root.mainloop()