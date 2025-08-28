from tkinter import *
from tkinter import ttk
from networkerdata import Mail, MailTrigger, Attachment
from data import MailTriggerType

# TODO I don't see how I can get around using this global variable to keep track of the data of the current mail
current_mail = Mail()

def get_mails_panel(window, networker_data):
     # mail frame
    mail_frame = LabelFrame(window, text="Mail")
    mail_frame.grid(column=0, row=0, columnspan=2, sticky=EW)

    # attachments frame
    attachments_frame = LabelFrame(mail_frame, text="Attachments")
    attachments_frame.grid(column=0, row=2, columnspan=5, sticky=EW)

    # set up variables
    id_var = StringVar(window)
    trigger_var = StringVar(window)
    trigger_data_var = StringVar(window)

    attachment_id_var = StringVar(window)
    attachment_qty_var = StringVar(window)
    attachments_listbox = Listbox(attachments_frame)
    mail_list = Listbox(window)

    current_mail = Mail()

    # set up callbacks for adding attachment and adding mail
    def add_attachment(var=None):
        global current_mail
        attachment_id = attachment_id_var.get()
        attachment = Attachment(attachment_id, attachment_qty_var.get())
        current_mail.add_attachment(attachment)
        attachments_listbox.insert(0, attachment_id)
        # reset form to default state
        attachment_id_var.set("")
        attachment_qty_var.set("")

    def remove_attachment(var=None):
        global current_mail
        # remove from mail
        current_mail.remove_attachments_with_ids(attachments_listbox.curselection())
        # remove from listbox
        # NOTE fix to remove every mail with an id selected, currently only deletes selection
        for index in attachments_listbox.curselection():
            attachments_listbox.delete(index)
    attachments_listbox.bind('<Delete>', remove_attachment)

    def add_mail():
        global current_mail
        current_mail.id = id_var.get()
        current_mail.trigger = MailTrigger(trigger_var.get(), trigger_data_var.get())
        # attachments are added on-the-fly
        networker_data.add_mail(current_mail)
        # add to mail list
        mail_list.insert(0, id_var.get())
        # now reset to default state
        current_mail = Mail()
        id_var.set("")
        trigger_var.set(MailTriggerType.HELP_REQUEST.name)
        trigger_data_var.set("")
        attachments_listbox.delete(0, END)

    def remove_mail(var=None):
        global current_mail
        # remove from networker mails
        networker_data.remove_mails_with_ids(mail_list.curselection())
        # remove from list
        # NOTE fix to remove every mail with an id selected, currently only deletes selection
        for index in mail_list.curselection():
            mail_list.delete(index)
    mail_list.bind('<Delete>', remove_mail)

    mail_id_lbl = Label(mail_frame, text="Mail ID: ")
    mail_id_entry = Entry(mail_frame, textvariable=id_var)
    mail_trigger_type_lbl = Label(mail_frame, text="Trigger: ")
    mail_trigger_type_entry = ttk.Combobox(mail_frame, textvariable=trigger_var, values=[type.name for type in MailTriggerType])
    mail_trigger_type_entry.set(MailTriggerType.HELP_REQUEST.name)

    mail_id_lbl.grid(column=0, row=0)
    mail_id_entry.grid(column=1, row=0)
    mail_trigger_type_lbl.grid(column=2, row=0)
    mail_trigger_type_entry.grid(column=3, row=0)

    # trigger data frame
    trigger_data_id_lbl = Label(mail_frame, text="Item ID: ")
    trigger_data_id_entry = Entry(mail_frame, textvariable=trigger_data_var)

    trigger_data_id_lbl.grid(column=4, row=0)
    trigger_data_id_lbl.grid_remove()
    trigger_data_id_entry.grid(column=5, row=0)
    trigger_data_id_entry.grid_remove()

    def trigger_data_visible(var, index, mode):
        trigger_type = MailTriggerType[trigger_var.get()]
        if trigger_type in [MailTriggerType.SENT_ITEM, MailTriggerType.FIRST_OBTAINED_ITEM, MailTriggerType.REPEAT_OBTAINED_ITEM, MailTriggerType.SENT_MESSAGE]:
            trigger_data_id_lbl.grid()
            trigger_data_id_entry.grid()
        else:
            trigger_data_id_lbl.grid_remove()
            trigger_data_id_entry.grid_remove()
    trigger_var.trace_add("write", trigger_data_visible)

    attachment_id_lbl = Label(attachments_frame, text="ID: ")
    attachment_id_entry = Entry(attachments_frame, textvariable=attachment_id_var)
    attachment_qty_lbl = Label(attachments_frame, text="Qty: ")
    attachment_qty_entry = Entry(attachments_frame, textvariable=attachment_qty_var)

    attachment_add_btn = Button(attachments_frame, text="+", command=add_attachment)
    attachment_remove_btn = Button(attachments_frame, text="−", command=remove_attachment)

    attachment_id_lbl.grid(column=0, row=0)
    attachment_id_entry.grid(column=1, row=0)
    attachment_qty_lbl.grid(column=0, row=1)
    attachment_qty_entry.grid(column=1, row=1)
    attachment_add_btn.grid(column=0, row=2, columnspan=2, sticky=EW)
    attachment_remove_btn.grid(column=2, row=2, sticky=EW)
    attachments_listbox.grid(column=2, row=0, rowspan=2, padx=10)

    attachment_qty_entry.bind('<Return>', add_attachment)

    # add and remove mail buttons
    add_mail_btn = Button(window, text="Add Mail", command=add_mail)
    remove_mail_btn = Button(window, text="Remove Mail", command=remove_mail)

    add_mail_btn.grid(column=0, row=1, sticky=EW)
    remove_mail_btn.grid(column=1, row=1, sticky=EW)

    mail_list.grid(column=0, row=2, columnspan=2, sticky=EW)