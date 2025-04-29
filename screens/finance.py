from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<FinanceScreen>:
    MDLabel:
        text: "Finance Screen"
        halign: "center"

'''
Builder.load_string(d_kv)

class FinanceScreen(MDScreen):
    pass  