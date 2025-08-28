import json
from data import MailTriggerType

class NetworkerData:
    def __init__(self, name="", rank=0, hidden=False, accurate=False, pg_col_bg=0, pg_col_sidebar=0,  pg_theme=0):
        self.name = name # Networker username
        self.rank = rank # Networker rank
        self.hidden = hidden # Should the networker be hidden on friend lists?
        self.pfp = ""
        self.accurate = accurate # Was the networker's page designed randomly or by referencing e.g. the wiki?
        self.friends = [] # A list of the usernames of the networker's friends
        self.friend_conditions = [] # A list of requirements for a networker to accept a friend request
        self.pg_col_bg = pg_col_bg
        self.pg_col_sidebar = pg_col_sidebar
        self.pg_theme = pg_theme
        self.modules = {} # The modules present on the networker's page. Dict of form {(x, y): Module}, where x=0 is at the top of the page
        self.mails = [] # A list of the mails a networker sends

    def set_module(self, x, y, module):
        self.modules[(x, y)] = module

    # remove the module with top-left corner at the given position
    def remove_module(self, x, y):
        del self.modules[(x, y)]

    def get_or_create_module_at(self, x, y):
        if (x, y) not in self.modules:
            self.modules[(x, y)] = Module()
        return self.modules[(x, y)]
            
    def add_friend(self, name):
        self.friends.append(name)

    def remove_friend(self, name):
        self.friends.remove(name)

    def add_mail(self, mail):
        self.mails.append(mail)

    def remove_mails_with_ids(self, mail_ids):
        mails_to_remove = []
        for mail in self.mails:
            if mail.id in mail_ids:
                mails_to_remove.append(mail)
        for mail in mails_to_remove:
            self.mails.remove(mail)

    def page_to_json(self):
        page_json = []
        for module in self.modules:
            try:
                page_json.append(self.modules[module].to_json(module[0], module[1]))
            except AttributeError as e:
                print(f'Page has no module at position {module}')
        return page_json

    def to_json(self):
        return {
            'name': self.name,
            'avatar': self.pfp,
            'rank': self.rank,
            'hidden': self.hidden,
            'accurate': self.accurate,
            'friends': self.friends,
            'friend_conditions': [friend_condition.to_json() for friend_condition in self.friend_conditions],
            'page_color_bg': self.pg_col_bg,
            'page_color_sidebar': self.pg_col_sidebar,
            'page_theme': self.pg_theme,
            'modules': self.page_to_json(),
            'mails': [mail.to_json() for mail in self.mails]
        }

class FriendCondition:
    def __init__(self, type, data):
        self.type = type # the type of trigger
        self.data = data # a dictionary containing the data associated to the condition (i.e. the id of item required to be owned)

    def to_json(self):
        return {'type': self.type, 'data': self.data}


# data is a dictionary containing things like input item id, qty, output item id.
class Module:
    def __init__(self):
        self.data = {}

    def to_json(self, x, y):
        return {
            'x': x,
            'y': y,
            'skin': self.skin.value,
            'color': self.color,
            'module_id': self.module_id,
            'data': self.data
        }

class Mail:
    def __init__(self):
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def remove_attachment(self, attachment):
        self.attachments.remove(attachment)

    def remove_attachments_with_ids(self, item_ids):
        attachments_to_remove = []
        for attachment in self.attachments:
            if attachment.item_id in item_ids:
                attachments_to_remove.append(attachment)
        for attachment in attachments_to_remove:
            self.attachments.remove(attachment)

    def to_json(self):
        mail_json = {
                'id': self.id,
                'trigger': self.trigger.to_json(),
                }
        attachments_json = [attachment.to_json() for attachment in self.attachments]
        if len(attachments_json) > 0:
            mail_json['attachments'] = attachments_json
        return mail_json

class MailTrigger:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def to_json(self):
        trigger_type = MailTriggerType[self.type]
        trigger_json = {'type': self.type}
        if trigger_type in [MailTriggerType.SENT_ITEM, MailTriggerType.FIRST_OBTAINED_ITEM, MailTriggerType.REPEAT_OBTAINED_ITEM, MailTriggerType.SENT_MESSAGE]:
            trigger_json['data'] = self.data
        return trigger_json

class Attachment:
    def __init__(self, item_id, qty):
        self.item_id = item_id
        self.qty = qty

    def to_json(self):
        return {'id': self.item_id, 'qty': self.qty}