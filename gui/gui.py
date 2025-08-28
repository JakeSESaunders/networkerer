from enum import Enum
from tkinter import Tk, ttk, Label, Menu, LabelFrame, Canvas, NS, filedialog, StringVar, IntVar, END
from networkerdata import NetworkerData, FriendCondition
from gui.panels.required import get_required_panel
from gui.panels.friends import get_friend_panel
from gui.panels.friend_conditions import get_friend_conditions_panel
from gui.panels.mails import get_mails_panel
from gui.panels.page.page import get_page_panel
import json

networker_data = NetworkerData()

window = Tk()
window.title("Networkerer")
# window.iconbitmap("networkerer.ico")

get_required_panel(window, networker_data)
get_friend_panel(window, networker_data)
get_friend_conditions_panel(window, networker_data)

# notebook (tabs)
notebook = ttk.Notebook(window)
notebook.grid(column=1, row=0, rowspan=3, sticky=NS)

# page
notebook.add(get_page_panel(window, networker_data), text="Page")

# mail
mail_frame = LabelFrame(notebook)
notebook.add(mail_frame, text="Mails")
get_mails_panel(mail_frame, networker_data)

def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".json")
    if f is None: # cancel selected in save dialog
        return
    with f as write_file:
        json.dump(networker_data.to_json(), write_file)

# menu
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As...", command=file_save)
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)

def show_gui():
    window.mainloop()