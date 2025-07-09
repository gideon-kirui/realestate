from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

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
from screens.adminprofile import AdminAccountScreen
from screens.landlords import LandLordScreen
from screens.landloardprofile import LandloardProfileScreen
from screens.tenatntprofile import TenatntProfileScreen
from screens.adminlogin import AdminLoginPage
from screens.schedler import PlanSchedlerScreen
from screens.forms import MultiStepAddpForm


Builder.load_file("kv/mainapp.kv")

class MainAppScreen(MDScreen):
    pass
