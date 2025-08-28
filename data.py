from enum import Enum

class ModuleSkin(Enum):
    DEFAULT = 18
    BUBBLES = 19
    LINES = 20
    CROSS = 21
    HEARTS = 22

class FriendConditionType(Enum):
    OWNS_ITEM = 0
    NONE = 1

class MailTriggerType(Enum):
    SENT_ITEM = 0
    FRIEND_REQUEST_ACCEPTED = 1
    FRIEND_REQUEST_DECLINED = 2
    HELP_REQUEST = 3
    STICKER_REQUEST = 4
    LOOP_REQUEST = 5
    FIRST_OBTAINED_ITEM = 6
    REPEAT_OBTAINED_ITEM = 7
    TRADE_REQUEST = 8
    SENT_MESSAGE = 9

class ModuleType(Enum):
    PIC = 0
    TEXT = 1
    TRADE = 2
    STICKER = 3
    LOOP = 4

class ModuleTheme(Enum):
    MLN = 0
    LEGO_UNIVERSE = 1
    BIONICLE = 2
    SPA = 3
    BETA = 4

# LU pic module ids
BRICKKEEPER = 0
NUMB_CHUCK = 1
FRIENDLY_FELIX = 2
OLD_CAPT_JOE = 3

# module ids
PIC = {
    ModuleTheme.MLN: 43889
}
TEXT = {
    ModuleTheme.MLN: 43890,
    ModuleTheme.LEGO_UNIVERSE: 78718,
    ModuleTheme.BIONICLE: 91153
}
TRADE = {
    ModuleTheme.MLN: 43884,
    ModuleTheme.LEGO_UNIVERSE: 78720,
    ModuleTheme.BIONICLE: 91152
}
STICKER = {
    ModuleTheme.MLN: 56868, # there is also an ID for a "friend version"? 69866
    ModuleTheme.LEGO_UNIVERSE: 78716,
    ModuleTheme.BIONICLE: 91156,
    ModuleTheme.SPA: 53743,
    ModuleTheme.BETA: 53012
}
LOOP = {
    ModuleTheme.MLN: 52701, # there is also an ID for a "friend version"? 69865
    ModuleTheme.LEGO_UNIVERSE: 78719,
    ModuleTheme.BIONICLE: 91154
}

module_type_to_theme_id_dict = {
    ModuleType.PIC: PIC,
    ModuleType.TEXT: TEXT,
    ModuleType.TRADE: TRADE,
    ModuleType.STICKER: STICKER,
    ModuleType.LOOP: LOOP
}

module_widths = {
    ModuleType.PIC: 3,
    ModuleType.TEXT: 1,
    ModuleType.TRADE: 2,
    ModuleType.STICKER: 1,
    ModuleType.LOOP: 1
}

# I am colourblind, so used an online tool to give names to each colour.
colors = {
    "red-orange": 1,
    "yellow-orange": 2,
    "canary-yellow": 3,
    "mustard-yellow": 4,
    "citrus-green": 5,
    "apple-green": 6,
    "neon-blue": 7,
    "cool-blue": 8,
    "clear-blue": 9,
    "cornflower-blue": 16,
    "purple-flower": 17,
    "neon-pink": 18,
    "strawberry-red": 19,
    "chalk-blue": 20,
    "copper": 21,
    "magenta-red": 22,
    "bright-gold": 23,
    "moss-green": 24,
    "ochre": 25,
    "avocado": 32,
    "indigo": 33,
    "blue-purple": 34,
    "cyan": 35,
    "purple": 36,
    "bright-blue": 37,
    "hot-pink": 38,
    "wood-brown": 39,
    "dark-grey": 40
}

colors_sidebar = {
    "camo": 0,
    "muted-blue": 1,
    "avocado": 2,
    "plum": 3,
    "dark-grey": 4
}

page_skins = {
    "default": -1,
    "lego-universe": 96450,
    "bionicle": 94622,
    "city": 103114
}