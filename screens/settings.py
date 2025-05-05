from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<SettingsScreen>:
    MDLabel:
        text: "Make Changes to your system Here"
        halign: "center"

'''
Builder.load_string(d_kv)

class SettingsScreen(MDScreen):
    pass 