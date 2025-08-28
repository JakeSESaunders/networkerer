from tkinter import *

def get_friend_panel(window, networker_data):
    # friendlist labelframe
    frame = LabelFrame(window, text="Friends")

    # friend name
    friend_name_var = StringVar(window)
    friend_name_lb = Label(frame, text="Name: ")
    friend_name_entry = Entry(frame, textvariable=friend_name_var)

    # friend_list
    friend_list = Listbox(frame)
    
    # commands for when buttons pressed
    def friend_add_btn_pressed(var=None):
        name = friend_name_var.get()
        friend_list.insert(0, name)
        friend_name_entry.delete(0, END)
        networker_data.add_friend(name)

    def friend_remove_btn_pressed(var=None):
        for index in friend_list.curselection():
            name = friend_list.get(index)
            networker_data.remove_friend(name)
            friend_list.delete(index)

    # add btn
    friend_add_btn = Button(frame, text="+",  command=friend_add_btn_pressed)
    friend_name_entry.bind('<Return>', friend_add_btn_pressed)

    # remove btn
    friend_remove_btn = Button(frame, text="−", command=friend_remove_btn_pressed)
    friend_list.bind('<Delete>', friend_remove_btn_pressed)

    frame.grid(column=0, row=1, sticky=N)

    friend_name_lb.grid(column=0, row=0)
    friend_name_entry.grid(column=1, row=0)
    friend_add_btn.grid(column=3, row=0)

    friend_list.grid(column=0, row = 1, columnspan=2, sticky=EW)
    friend_remove_btn.grid(column=3, row=1, sticky=NS)

    return friend_list
    