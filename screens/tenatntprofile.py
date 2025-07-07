from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<TenatntProfileScreen>:
    MDLabel:
        text: "Manage Tenant Profile Here"
        halign: "center"

'''
Builder.load_string(d_kv)

class TenatntProfileScreen(MDScreen):
    pass  