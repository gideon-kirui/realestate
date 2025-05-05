from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from screens.dashbord import DashboardScreen
from screens.properties import PropertiesScreen
from screens.accounts import AccountsScreen
from screens.finance import FinanceScreen
from screens.settings import SettingsScreen
from screens.chats import ChatScreen
from screens.admin import AdminAccountScreen


KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
<TooltipMDIconButton@MDIconButton+MDTooltip>
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    unfocus_color: "#fffcf4"

MDScreen:
    md_bg_color: "darkgrey"
    MDBoxLayout:
        orientation: 'vertical'
        MDFloatLayout:
            size_hint: 1, .07
            md_bg_color: "#00BFFF"

            # Logo Button
            MDIconButton:
                icon: "logo.png"
                adaptive_size: True
                icon_size: "40dp"
                on_release: app.change_screen('dashboard')
                pos_hint: {"top": 1, "right": 0.05}

            # Title Label
            MDLabel:
                text: "Real Estate Management System"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H6"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

            # Icon Buttons on the right
            MDBoxLayout:
                orientation: "horizontal"
                size_hint: None, None
                height: self.minimum_height
                width: self.minimum_width
                pos_hint: {"top": 0.95, "right": 1}
                spacing: "12dp"

                TooltipMDIconButton:
                    icon: "message"
                    icon_size: "24sp"
                    tooltip_text: "Messages"
                    on_release: app.change_screen('chats')

                TooltipMDIconButton:
                    icon: "account-circle"
                    icon_size: "24sp"
                    tooltip_text: "Admin"
                    on_release: app.change_screen('admin')

                TooltipMDIconButton:
                    icon: "exit-to-app"
                    icon_size: "24sp"
                    tooltip_text: "Logout"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .88
            md_bg_color: "white"
            MDBoxLayout:
                adaptive_width: True
                md_bg_color: "#00BFFF"
                MDRelativeLayout:
                    MDIconButton:
                        icon: "view-dashboard"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .95, "right": .7}
                        on_release: app.change_screen('dashboard')

                    MDIconButton:
                        icon: "home-city"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .85, "right": .7}
                        on_release: app.change_screen('properties')

                    MDIconButton:
                        icon: "account-multiple"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .75, "right": .7}
                        on_release: app.change_screen('accounts')

                    MDIconButton:
                        icon: "wallet"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .65, "right": .7}
                        on_release: app.change_screen('finance')

                    MDIconButton:
                        icon: "cog"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .1, "right": .7}
                        on_release: app.change_screen('settings')

            ScreenManager:
                id: screen_manager
                DashboardScreen:
                    name: 'dashboard'
                PropertiesScreen:   
                    name: 'properties'
                AccountsScreen:
                    name: 'accounts'
                FinanceScreen:
                    name: 'finance'
                ChatScreen:
                    name: 'chats'
                AdminAccountScreen:
                    name: 'admin'
                SettingsScreen:
                    name: 'settings'

        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .05
            padding: "12dp"
            md_bg_color: "red"
            
            MDLabel:
                text: "Footer"

'''

class RMS(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def change_screen(self, screen_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name

RMS().run()