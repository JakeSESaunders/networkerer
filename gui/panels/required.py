from tkinter import *
from networkerdata import NetworkerData

def get_required_panel(window, networker_data):
    name_var = StringVar(window)
    pfp_var = StringVar(window)
    rank_var = StringVar(window)
    hidden_var = IntVar(window)
    accurate_var = IntVar(window)

    # define and set callback functions to update networker data when these values are edited
    def edit_name(var, index, mode):
        networker_data.name = name_var.get()
    name_var.trace_add("write", edit_name)

    def edit_pfp(var, index, mode):
        networker_data.pfp = pfp_var.get()
    pfp_var.trace_add("write", edit_pfp)

    def edit_rank(var, index, mode):
        networker_data.rank = rank_var.get()
    rank_var.trace_add("write", edit_rank)

    def edit_hidden(var, index, mode):
        networker_data.hidden = (hidden_var.get() == 1)
    hidden_var.trace_add("write", edit_hidden)

    def edit_accurate(var, index, mode):
        networker_data.accurate = (accurate_var.get() == 1)
    accurate_var.trace_add("write", edit_accurate)

    # visual components
    # required labelframe
    required_frame = LabelFrame(window, text="Required")
    required_frame.grid(column=0, row=0, sticky=N + EW)

    # name
    name_label = Label(required_frame, text="Name: ")
    name_label.grid(column=0, row=0)
    name_entry = Entry(required_frame, bd=5, textvariable=name_var)
    name_entry.grid(column=1, columnspan=3, sticky=EW, row=0)
    #pfp
    pfp_lbl = Label(required_frame, text="Avatar: ")
    pfp_lbl.grid(column=0, row=1)
    pfp_entry = Entry(required_frame, bd=5, textvariable=pfp_var)
    pfp_entry.grid(column=1, columnspan=3, sticky=EW, row=1)
    # rank
    rank_label = Label(required_frame, text="Rank: ")
    rank_label.grid(column=0, row=2, rowspan=2)
    rank_entry = Spinbox(required_frame, from_=0, to=10, width=8, textvariable=rank_var)
    rank_entry.grid(column=1, row=2, rowspan=2)
    # hidden
    hidden_label = Label(required_frame, text="Hidden? ")
    hidden_label.grid(column=2, row=2),
    hidden_entry = Checkbutton(required_frame, variable=hidden_var)
    hidden_entry.grid(column=3, row=2, sticky=W)
    #accurate
    accurate_lbl = Label(required_frame, text="Accurate? ")
    accurate_lbl.grid(column=2, row=3),
    accurate_entry = Checkbutton(required_frame, variable=accurate_var)
    accurate_entry.grid(column=3, row=3, sticky=W)