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
        MDBoxLayout:
            orientation: "vertical"
            size_hint: 1, .07
            md_bg_color: "#00BFFF"
            MDBoxLayout:
                adaptive_height: True
                padding: "10dp", "1dp"
                MDIconButton:
                    icon: "logo.png"
                    adaptive_size: True
                    icon_size: "24dp"
                    
                MDLabel:
                    text: "Real Estate Management System"
                    halign: "center"   
                    
                MDBoxLayout:
                    orientation: "horizontal"
                    adaptive_size: True
                    TooltipMDIconButton:
                        icon: "message"
                        icon_size: "24sp"
                        tooltip_text: "Messages"
                    TooltipMDIconButton:
                        icon: "account-circle"
                        icon_size: "24sp"
                        tooltip_text: "Admin"         
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
                MDNavigationRail:
                    md_bg_color: "#00BFFF"
                    selected_color_background: "#e7e4c0"
                    ripple_color_item: "#e7e4c0"
                    MDNavigationRailItem:
                        icon: "view-dashboard"
                        on_release: app.change_screen('dashboard')
                    MDNavigationRailItem:
                        icon: "city"
                        on_release: app.change_screen('properties')
                    MDNavigationRailItem:
                        icon: "home-account"
                        on_release: app.change_screen('accounts')
                    MDNavigationRailItem:
                        icon: "account-key"
                        on_release: app.change_screen('accounts')
                    MDNavigationRailItem:
                        icon: "cash"
                        on_release: app.change_screen('finance')
            
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