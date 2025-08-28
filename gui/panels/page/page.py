from tkinter import *
from gui.panels.page.colors import get_page_colours_panel
from gui.panels.page.module_info import get_page_module_info_panel
from data import module_widths
from networkerdata import Module

def get_page_panel(window, networker_data):
    frame = LabelFrame(window)
    frame.grid(column=0, row=0)

    module_x = IntVar(frame, value=-1)
    module_y = IntVar(frame, value=-1)

    def set_module_pos(x, y):
        module_x.set(x)
        module_y.set(y)

    page_frame = LabelFrame(frame)
    page_frame.grid(column=1, row=0, rowspan=2)
    module_btns = {}
    for x in range(3):
        for y in range(4):
            btn = Button(page_frame, text=f'Module ({x}, {y})', width=10, height=4, command=(lambda i = x, j = y: set_module_pos(i, j)))
            networker_data.set_module(x, y, Module())
            btn.grid(column=x, row=y, padx=2, pady=2)
            module_btns[(x, y)] = btn

    get_page_colours_panel(frame, networker_data)

    get_page_module_info_panel(frame, networker_data, module_x, module_y, module_btns)

    return frame