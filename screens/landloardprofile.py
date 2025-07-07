from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<LandloardProfileScreen>:
    MDLabel:
        text: "Manage Landloard Profile Here"
        halign: "center"

'''
Builder.load_string(d_kv)

class LandloardProfileScreen(MDScreen):
    pass  