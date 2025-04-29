from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<AccountsScreen>:
    MDLabel:
        text: "Account Screen"
        halign: "center"

'''
Builder.load_string(d_kv)

class AccountsScreen(MDScreen):
    pass  
