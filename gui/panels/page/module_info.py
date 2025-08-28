from tkinter import *
from tkinter import ttk
from data import ModuleType, ModuleSkin, ModuleTheme, colors, module_type_to_theme_id_dict
from networkerdata import Module
from gui.panels.page.module_data import get_module_data_panel

var_list = {}

def get_page_module_info_panel(window, networker_data, module_x, module_y, buttons):
    # module info editor
    frame = LabelFrame(window, text=f'Module at ({module_x.get()}, {module_y.get()})')
    frame.grid(column=0, row=1, sticky=N+EW)
    frame.grid_remove()

    # variables
    type_var = StringVar(frame)
    theme_var = StringVar(frame, value=ModuleTheme.MLN.name)
    color_var = StringVar(frame, value="red-orange")
    skin_var = StringVar(frame, value=ModuleSkin.DEFAULT.name)
    global var_list
    var_list = [type_var, theme_var, color_var, skin_var]


    # module type
    type_lbl = Label(frame, text="Type: ")
    type_lbl.grid(column=0, row=0, sticky=E)
    
    type_entry = ttk.Combobox(frame, textvariable=type_var, values=[type.name for type in ModuleType])
    type_entry.grid(column=1, row=0, sticky=W)

    # module theme
    theme_lbl = Label(frame, text="Theme: ")
    theme_lbl.grid(column=0, row=1, sticky=E)

    theme_entry = ttk.Combobox(frame, values=[theme.name for theme in ModuleTheme], textvariable=theme_var)
    theme_entry.grid(column=1, row=1, sticky=W)

    # module colour
    colour_lbl = Label(frame, text="Colour: ")
    colour_lbl.grid(column=0, row=2, sticky=E)

    colour_entry = ttk.Combobox(frame, values=list(colors), textvariable=color_var)
    colour_entry.grid(column=1, row=2, sticky=W)

    # module skin
    skin_lbl = Label(frame, text="Skin: ")
    skin_lbl.grid(column=0, row=3, sticky=E)

    skin_entry = ttk.Combobox(frame, values=[skin.name for skin in ModuleSkin], textvariable=skin_var)
    skin_entry.grid(column=1, row=3, sticky=W)

    def change_module_pos(var, index, mode):
        frame.grid()
        frame['text'] = f'Module at ({module_x.get()}, {module_y.get()})'
        edit_module(var, index, mode)
    module_x.trace_add("write", change_module_pos)
    module_y.trace_add("write", change_module_pos)

    def edit_module(var, index, mode):
        if type_var.get() == '':
            return
        module_type = ModuleType[type_var.get()]
        module_theme = ModuleTheme[theme_var.get()]
        module_color = colors[color_var.get()]
        module_skin = ModuleSkin[skin_var.get()]

        module_id = module_type_to_theme_id_dict[module_type][module_theme]
        
        module = networker_data.get_or_create_module_at(module_x.get(), module_y.get())
        module.skin = module_skin
        module.color = module_color
        module.module_id = module_id

    type_var.trace_add("write", edit_module)
    theme_var.trace_add("write", edit_module)
    color_var.trace_add("write", edit_module)
    skin_var.trace_add("write", edit_module)

    get_module_data_panel(frame, networker_data, module_x, module_y, type_var, buttons)

    return frame