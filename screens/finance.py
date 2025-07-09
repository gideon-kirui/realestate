from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
import matplotlib.pyplot as plt
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ListProperty, NumericProperty, StringProperty

Builder.load_file("kv/finance.kv")

class FinanceScreen(MDScreen):
    active_category = StringProperty("rentals")
    def on_kv_post(self, base_widget):  # Automatically called after KV is loaded
        self.switch_table("rentals")  # Show rentals by default

    def switch_table(self, category):
        self.active_category = category
        self.update_button_colors()
        self.ids.table_container.clear_widgets()
        self.add_table_section(category)

    def update_button_colors(self):
        colors = {
            "rentals": (0,0,100/255,1),       
            "leased": (0,0,100/255,1),        
            "sold": (0,0,100/255,1),          
            "others": (0,0,100/255,1), 
        }

        selected_color = (1,0,100/255,1)  # Highlighted green

        self.ids.rentals_btn.md_bg_color = selected_color if self.active_category == "rentals" else colors["rentals"]
        self.ids.leased_btn.md_bg_color = selected_color if self.active_category == "leased" else colors["leased"]
        self.ids.sold_btn.md_bg_color = selected_color if self.active_category == "sold" else colors["sold"]
        self.ids.others_btn.md_bg_color = selected_color if self.active_category == "others" else colors["others"]

    def add_table_section(self, category):
        table_box = self.ids.table_container

        if category == "rentals":
            # title = "Rental Properties"
            row_data = [("Unit A", "10,000", "20,000"), ("Unit B", "12,000", "20,000"), ("Unit B", "12,000", "20,000")]
        elif category == "leased":
            # title = "Leased Properties"
            row_data = [("Office 1", "50,000", "")]
        elif category == "sold":
            # title = "Sold Properties"
            row_data = [("House X", "2,000,000", "")]
        elif category == "others":
            # title = "Other Revenues"
            row_data = [("Parking", "3,000", ""), ("Penalty", "1,000", "")]
        else:
            # title = "Unknown"
            row_data = []

        section = MDBoxLayout(orientation="vertical", spacing="10dp", size_hint_y=None)
        section.bind(minimum_height=section.setter("height"))

        section.add_widget(MDLabel(bold=True, font_style="H6", halign="left"))

        table = MDDataTable(
            size_hint=(None, None),
            height=dp(430),
            width=dp(480),
            use_pagination=True,
            rows_num=7,
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            column_data=[("Property", dp(30)), ("Expected Amount", dp(30)), ("Collected Amount", dp(30))],
            row_data=row_data
        )
        section.add_widget(table)
        table_box.add_widget(section)

class FinanceColProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    bar_color = ListProperty([1,0,100/255])
    bar_width = NumericProperty(10)
    value = NumericProperty(80)
    duration = NumericProperty(1.5)
    parcentage = StringProperty("0%")
    amount = StringProperty("KSH 0")
    counter = 0
    acounter = 100000000
    amnt_color = ListProperty([0,1,100/255])

    def __init__(self, **kwargs):
        super(FinanceColProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.duration/self.value)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counter < self.value and self.acounter >= 0:
            self.counter += 1
            self.parcentage = f"{self.counter}%"
            self.set_value = self.counter
            self.amount = f"KSH {self.acounter}"
        else:
            Clock.unschedule(self.percent_counter)