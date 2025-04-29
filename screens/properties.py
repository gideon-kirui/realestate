from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<PropertiesScreen>:
    MDLabel:
        text: "Properties Screen"
        halign: "center"

'''
Builder.load_string(d_kv)

class PropertiesScreen(MDScreen):
    pass  
