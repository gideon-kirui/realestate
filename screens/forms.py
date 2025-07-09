from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.label import MDLabel

Builder.load_file("kv/forms.kv")

class MultiStepAddpForm(MDBoxLayout):
    pass