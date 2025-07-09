from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivymd.uix.snackbar import Snackbar

Builder.load_file("kv/adminlogin.kv")

class AdminLoginPage(MDScreen):
    def authenticate(self, username, password):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if username == "admin" and password == "1234":
            self.manager.current = "main"
        else:
            snackbar = Snackbar()
            snackbar.text = "Invalid credentials"
            snackbar.open()