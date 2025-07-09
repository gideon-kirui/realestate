from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar

from screens.adminlogin import AdminLoginPage
from screens.mainapp import MainAppScreen

class RMS(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AdminLoginPage(name="login"))
        sm.add_widget(MainAppScreen(name="main"))
        return sm

    def change_screen(self, screen_name):
        self.root.get_screen("main").ids.screen_manager.current = screen_name

    def toggle_fab_menu(self):
        screen = self.root.get_screen("main")
        fab = screen.ids.fab_toggle
        btns = [screen.ids.voucher_btn, screen.ids.cash_btn]
        is_open = btns[0].opacity == 1
        fab.icon = "plus" if is_open else "close"
        for btn in btns:
            btn.opacity = 0 if is_open else 1
            btn.disabled = is_open

    def reset_login(self):
        # Optional: clear username/password fields
        login_screen = self.root.get_screen("login")
        login_screen.ids.username.text = ""
        login_screen.ids.password.text = ""
        
if __name__ == '__main__':
    RMS().run()