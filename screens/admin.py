from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<AdminAccountScreen>:
    MDLabel:
        text: "Manage Administration Profile Here"
        halign: "center"

'''
Builder.load_string(d_kv)

class AdminAccountScreen(MDScreen):
    pass  