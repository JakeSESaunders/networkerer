from tkinter import *
from tkinter import ttk
from networkerdata import FriendCondition
from data import FriendConditionType

def get_friend_conditions_panel(window, networker_data):
    # set up frame
    frame = LabelFrame(window, text="Friend Condition(s)")
    frame.grid(column=0, row=2, sticky=N)

    # set up variables
    type_var = StringVar(window)
    data_var = StringVar(window)

    # add callbacks to update friend condition when variables updated
    def set_friend_condition(var, index, mode):
        data = data_var.get()
        if not str.isdigit(data):
            return
        friend_condition = FriendCondition(type_var.get(), int(data_var.get()))
        networker_data.friend_conditions.clear()
        networker_data.friend_conditions.append(friend_condition)

    type_var.trace_add("write", set_friend_condition)
    data_var.trace_add("write", set_friend_condition)

    # visual components
    type_label = Label(frame, text="Type: ")
    type_entry = ttk.Combobox(frame, values=[type.name for type in FriendConditionType], textvariable=type_var)
    type_entry.set('OWNS_ITEM')

    data_label = Label(frame, text="ID: ")
    data_entry = Entry(frame, textvariable=data_var)

    type_label.grid(column=0, row=0, sticky=E)
    type_entry.grid(column=1, row=0, sticky=W)
    data_label.grid(column=0, row=1, sticky=E)
    data_entry.grid(column=1, row=1, sticky=EW)