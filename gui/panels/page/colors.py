from tkinter import *
from tkinter import ttk
from data import colors, colors_sidebar, page_skins

def get_page_colours_panel(window, networker_data):
    col_bg_var = StringVar(window)
    col_sidebar_var = StringVar(window)
    theme_var = StringVar(window)

    # set up callbacks for when values edited
    def edit_col_bg_var(var, index, mode):
        networker_data.pg_col_bg = colors[col_bg_var.get()]
    col_bg_var.trace_add("write", edit_col_bg_var)

    def edit_col_sidebar_var(var, index, mode):
        networker_data.pg_col_sidebar = colors_sidebar[col_sidebar_var.get()]
    col_sidebar_var.trace_add("write", edit_col_sidebar_var)

    def edit_theme_var(var, index, mode):
        networker_data.pg_theme = page_skins[theme_var.get()]
    theme_var.trace_add("write", edit_theme_var)

    # visual components
    # colour editor
    colour_frame = LabelFrame(window, text="Page Colours")
    colour_frame.grid(column=0, row=0, sticky=N+EW)

    col_bg_lbl = Label(colour_frame, text="Background: ", width=10)
    col_bg_lbl.grid(column=0, row=0, sticky=E)

    col_bg_entry = ttk.Combobox(colour_frame, values=list(colors), textvariable=col_bg_var)
    col_bg_entry.set("red-orange")
    col_bg_entry.grid(column=1, row=0, sticky=W)
    
    col_bar_lbl = Label(colour_frame, text="Sidebar: ")
    col_bar_lbl.grid(column=0, row=1, sticky=E)

    col_bar_entry = ttk.Combobox(colour_frame, values=list(colors_sidebar), textvariable=col_sidebar_var)
    col_bar_entry.set("camo")
    col_bar_entry.grid(column=1, row=1, sticky=W)

    col_theme_lbl = Label(colour_frame, text="Theme: ")
    col_theme_lbl.grid(column=0, row=2, sticky=E)

    col_theme_entry = ttk.Combobox(colour_frame, values=list(page_skins), textvariable=theme_var)
    col_theme_entry.set("default")
    col_theme_entry.grid(column=1, row=2, sticky=W)