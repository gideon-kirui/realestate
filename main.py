from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from kivymd.uix.dialog import MDDialog
# from screens.dialogs import MultiStepAddpForm
# from screens.dialogs import MultiStepForm
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty
from kivymd.uix.button import MDRaisedButton

from screens.dashbord import DashboardScreen
from screens.properties import PropertiesScreen
from screens.tenants import TenantsScreen
from screens.finance import FinanceScreen
from screens.settings import SettingsScreen
from screens.chats import ChatScreen
from screens.admin import AdminAccountScreen
from screens.landlords import LandLordScreen
from screens.landloardprofile import LandloardProfileScreen
from screens.tenatntprofile import TenatntProfileScreen
from screens.adminlogin import AdminLoginPage
from screens.schedler import PlanSchedlerScreen


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
                icon: "asset/images/icons/logo.png"
                adaptive_size: True
                icon_size: "40dp"
                on_release: app.change_screen('dashboard')
                pos_hint: {"top": 1, "right": 0.05}

            
            MDLabel:
                text: "Real Estate Management System"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "H6"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

           
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
                        on_release: app.change_screen('tenants')

                    MDIconButton:
                        icon: "wallet"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .65, "right": .7}
                        on_release: app.change_screen('finance')

                    MDIconButton:
                        icon: "home-account"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .55, "right": .7}
                        on_release: app.change_screen('landloards')

                    MDIconButton:
                        icon: "alarm"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .45, "right": .7}
                        on_release: app.change_screen('scheddler')
                    
                    MDSeparator:
                        height: "1dp"
                        color: 1, 1, 1, 1
                        pos_hint: {"center_x": 0.5, "center_y": .37}

                    MDIconButton:
                        icon: "cog"
                        adaptive_size: True
                        icon_size: "24dp"
                        pos_hint: {"top": .35, "right": .7}
                        on_release: app.change_screen('settings')

                    MDIconButton:
                        icon: "information"
                        adaptive_size: True
                        icon_size: "30dp"
                        pos_hint: {"top": .28, "right": .7}
                        
                    
                    MDIconButton:
                        icon: "help-circle"
                        adaptive_size: True
                        icon_size: "30dp"
                        pos_hint: {"top": .2, "right": .7}
                       

                    MDBoxLayout:
                        orientation: 'vertical'
                        size_hint: None, None
                        size: self.minimum_size
                        spacing: "10dp"
                        pos_hint: {"top": .27, "right": .7}

                        MDIconButton:
                            id: voucher_btn
                            icon: "account"
                            icon_size: "14sp"
                            md_bg_color: 0, 0.5, 1, 1
                            theme_icon_color: "Custom"
                            icon_color: 1, 1, 1, 1
                            opacity: 0
                            disabled: True
                            on_release: app.open_registration_form()

                        MDIconButton:
                            id: cash_btn
                            icon: "home-city"
                            icon_size: "14sp"
                            md_bg_color: 0, 0.7, 0.3, 1
                            theme_icon_color: "Custom"
                            icon_color: 1, 1, 1, 1
                            opacity: 0
                            disabled: True
                            on_release: app.open_addproperty_form()

                        MDCard:
                            size_hint: None, None
                            size: "48dp", "48dp"
                            radius: [50,]
                            md_bg_color: 0.6, 0.5, 1, 1
                            pos_hint: {"center_x": 0.5}

                            MDIconButton:
                                id: fab_toggle
                                icon: "plus"
                                icon_size: "24sp"
                                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                                on_release: app.toggle_fab_menu()



            ScreenManager:
                id: screen_manager
                DashboardScreen:
                    name: 'dashboard'
                PropertiesScreen:   
                    name: 'properties'
                TenantsScreen:
                    name: 'tenants'
                FinanceScreen:
                    name: 'finance'
                LandLordScreen:
                    name: 'landloards'
                LandloardProfileScreen:
                    name: 'landloardprofile'
                TenatntProfileScreen:
                    name: 'tenantprofile'
                PlanSchedlerScreen:
                    name: 'scheddler'
                ChatScreen:
                    name: 'chats'
                AdminAccountScreen:
                    name: 'admin'
                SettingsScreen:
                    name: 'settings'

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .05
            padding: "12dp"
            md_bg_color: "red"
            MDRelativeLayout:

                MDIcon
                    icon: "asset/images/icons/phone.png"
                    pos_hint: {"center_x": 0.05, "center_y": 0.5}
                
                MDLabel:
                    text: "+254759348884"
                    adptive_size: True
                    pos_hint: {"center_x": .565}
                    bold: True
                    color: 1,1,1,1
                
                MDIcon
                    icon: "asset/images/icons/email.png"
                    pos_hint: {"center_x": 0.25, "center_y": 0.5}

                MDLabel:
                    text: "support@thegiks.co.ke"
                    adptive_size: True
                    pos_hint: {"center_x": .765}
                    bold: True
                    color: 1,1,1,1

                MDCard:
                    size_hint: None, None
                    size: "22dp", "22dp"
                    radius: [50,]
                    md_bg_color: 1, 1, 1, 1
                    pos_hint: {"center_x": 0.469, "center_y": 0.5}

                MDIcon
                    icon: "asset/images/icons/logo.png"
                    pos_hint: {"center_x": 0.47, "center_y": 0.5}

                MDLabel:
                    text: "Thegiks Softwares"
                    adptive_size: True
                    pos_hint: {"center_x": .98}
                    bold: True
                    color: 1,1,1,1

                MDIcon
                    icon: "asset/images/icons/web.png"
                    pos_hint: {"center_x": .815, "center_y": 0.5}

                MDLabel:
                    text: "www.thegiks.co.ke"
                    adptive_size: True
                    pos_hint: {"center_x": 1.33}
                    bold: True
                    color: 1,1,1,1

'''

class RMS(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = screen_name

    def toggle_fab_menu(self):
        fab = self.root.ids.fab_toggle
        btns = [self.root.ids.voucher_btn, self.root.ids.cash_btn]

        is_open = btns[0].opacity == 1

        fab.icon = "plus" if is_open else "close"

        for btn in btns:
            btn.opacity = 0 if is_open else 1
            btn.disabled = is_open

RMS().run()