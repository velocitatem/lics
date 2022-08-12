from lics import *
import pyperclip as pc
from plyer import notification
import os
def copy(text):
    os.system(f"echo \"{text}\" | xclip -selection \"clipboard\"")
clip=pc.paste()
clip=modify_sentence(clip)
pc.copy(str(clip))
copy(str(clip))
notification.notify(
    title = "LICS IS DONE",
    message = str(clip),
    timeout = 10,
)
