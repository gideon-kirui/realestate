from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

d_kv = '''
<PlanSchedlerScreen>:
    MDLabel:
        text: "Update all your plannings here"
        halign: "center"

'''
Builder.load_string(d_kv)

class PlanSchedlerScreen(MDScreen):
    pass  