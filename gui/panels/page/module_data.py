from tkinter import *
from data import ModuleType, module_widths

# Sets up the panels for each module data input.

grid_pos_col = 0,
grid_pos_row = 4

# Networker Trade Module
def get_module_data_panel(window, networker_data, module_x, module_y, type_var, buttons):
    frame = LabelFrame(window, text="Module Data")

    # sticker id input
    id_var = IntVar(window)
    id_lbl = Label(frame, text="Pic Sticker ID: ")
    id_entry = Entry(frame, textvariable=id_var)
    
    frame.grid(column=grid_pos_col, row=grid_pos_row, columnspan=2)
    frame.grid_remove()
    id_lbl.grid(column=0, row=0)
    id_lbl.grid_remove()
    id_entry.grid(column=1, row=0)
    id_entry.grid_remove()

    # Text input
    txt_lbl = Label(frame, text="Text:")
    txt_entry = Text(frame, width=20, height=4)

    txt_lbl.grid(column=0, row=1, columnspan=2)
    txt_lbl.grid_remove()
    txt_entry.grid(column=0, row=2, columnspan=2)
    txt_entry.grid_remove()

    # input item id
    in_id_var = IntVar(window)
    in_id_lbl = Label(frame, text="Input Item ID: ")
    in_id_entry = Entry(frame, textvariable=in_id_var)

    # input item qty
    in_qty_var = IntVar(window)
    in_qty_lbl = Label(frame, text="Input Quantity: ")
    in_qty_entry = Entry(frame, textvariable=in_qty_var)

    # output item id
    out_id_var = IntVar(window)
    out_id_lbl = Label(frame, text="Output Item ID: ")
    out_id_entry = Entry(frame, textvariable=out_id_var)

    # output item qty
    out_qty_var = IntVar(window)
    out_qty_lbl = Label(frame, text="Output Item Quantity: ")
    out_qty_entry = Entry(frame, textvariable=out_qty_var)
    
    in_id_lbl.grid(column=0, row=3)
    in_id_entry.grid(column=1, row=3)
    in_qty_lbl.grid(column=0, row=4)
    in_qty_entry.grid(column=1, row=4)
    out_id_lbl.grid(column=0, row=5)
    out_id_entry.grid(column=1, row=5)
    out_qty_lbl.grid(column=0, row=6)
    out_qty_entry.grid(column=1, row=6)

    in_id_lbl.grid_remove()
    in_id_entry.grid_remove()
    in_qty_lbl.grid_remove()
    in_qty_entry.grid_remove()
    out_id_lbl.grid_remove()
    out_id_entry.grid_remove()
    out_qty_lbl.grid_remove()
    out_qty_entry.grid_remove()

    def hide_unnecessary(var, index, mode):
        if type_var.get() not in [type.name for type in ModuleType]:
            return
        module_type = ModuleType[type_var.get()]
        frame.grid()
        # pic sticker id
        if module_type == ModuleType.PIC:
            id_lbl.grid()
            id_entry.grid()
        else:
            id_lbl.grid_remove()
            id_entry.grid_remove()
        # text id
        if module_type == ModuleType.TEXT:
            txt_lbl.grid()
            txt_entry.grid()
        else:
            txt_lbl.grid_remove()
            txt_entry.grid_remove()
        # trade
        if module_type in [ModuleType.TRADE, ModuleType.STICKER, ModuleType.LOOP]:
            in_id_lbl.grid()
            in_id_entry.grid()
            in_qty_lbl.grid()
            in_qty_entry.grid()
            out_id_lbl.grid()
            out_id_entry.grid()
        else:
            in_id_lbl.grid_remove()
            in_id_entry.grid_remove()
            in_qty_lbl.grid_remove()
            in_qty_entry.grid_remove()
            out_id_lbl.grid_remove()
            out_id_entry.grid_remove()
        if module_type == ModuleType.TRADE:
            out_qty_lbl.grid()
            out_qty_entry.grid()
        else:
            out_qty_lbl.grid_remove()
            out_qty_entry.grid_remove()

    type_var.trace_add("write", hide_unnecessary)

    def edit_module_data():
        pic_id = id_var.get()
        id_var.set(0)
        txt = txt_entry.get(1.0, END)
        txt_entry.delete(1.0, END)
        in_id = in_id_var.get()
        in_id_var.set(0)
        in_qty = in_qty_var.get()
        in_qty_var.set(0)
        out_id = out_id_var.get()
        out_id_var.set(0)
        out_qty = out_qty_var.get()
        out_qty_var.set(0)

        module_type = ModuleType[type_var.get()]
        x = module_x.get()
        y = module_y.get()
        module = networker_data.get_or_create_module_at(x, y)
        if module_type == ModuleType.PIC:
            module.data = {
                'pic-id': pic_id
            }
        elif module_type == ModuleType.TEXT:
            module.data = {
                'text': txt
            }
        elif module_type == ModuleType.TRADE:
            module.data = {
                'in-id': in_id,
                'in-qty': in_qty,
                'out-id': out_id,
                'out-qty': out_qty
            }
        elif module_type in [ModuleType.STICKER, ModuleType.LOOP]:
            module.data = {
                'in-id': in_id,
                'in-qty': in_qty,
                'out-id': out_id
            }
        width = module_widths[module_type]
        for i in range(width):
            buttons[(x + i, y)]["state"] = DISABLED

    save_data = Button(frame, text="Save Module Data", command=edit_module_data)
    save_data.grid(column=0, row=7,columnspan=2)

    

    return frame