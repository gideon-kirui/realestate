from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<ChatScreen>:
    MDLabel:
        text: "Manage Messages Here"
        halign: "center"

'''
Builder.load_string(d_kv)

class ChatScreen(MDScreen):
    pass  
