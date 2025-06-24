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

d_kv = '''

<FinanceColProgressBar>
    canvas.before:
        Color:
            rgba: root.bar_color + [0.3]
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_color
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_value*3.6)
    MDRelativeLayout:
        MDLabel:
            text: root.parcentage
            color: root.bar_color
            adaptive_size: True
            font_size: "30dp"
            pos_hint: {"center_x":.5, "center_y":.6}
            value: 50

        MDLabel:
            text: root.amount
            color: root.bar_color
            adaptive_size: True
            font_size: "14dp"
            bold: True
            pos_hint: {"center_x":.5, "center_y":.4}
            value: 50

<FinanceScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDRelativeLayout:
            MDGridLayout:
                cols: 3
                adaptive_height: True
                adaptive_width: True
                spacing: "10dp"
                pos_hint: {"center_x": 0.5, "center_y": .5}
                MDCard:
                    size_hint: None, None
                    size: "230dp", "600dp"
                    md_bg_color: 1, 1, 1, 1
                    MDRelativeLayout:
                        MDLabel:
                            text: "Total Revenue Collected"
                            color: 0, 0, 0, 1
                            adaptive_size: True
                            font_size: "16dp"
                            pos_hint: {"center_x":.5, "center_y":.97}
                            
                        FinanceColProgressBar:
                            size_hint: None, None
                            size: 150, 150
                            pos_hint: {"center_x":.5, "center_y":.8}
                        
                        MDLabel:
                            text: "Total Expenditure"
                            color: 0, 0, 0, 1
                            adaptive_size: True
                            font_size: "16dp"
                            pos_hint: {"center_x":.5, "center_y":.63}
                        
                        FinanceColProgressBar:
                            size_hint: None, None
                            size: 150, 150
                            pos_hint: {"center_x":.5, "center_y":.46}

                        MDSeparator:
                            height: "1dp"
                            color: 0, 1, 0, 1
                            pos_hint: {"center_x": 0.5, "center_y": .3}

                        MDProgressBar:
                            orientation: "vertical"
                            value: 80
                            size_hint: None, None 
                            color: 0, 1, 0, 1
                            width: "50dp"          
                            height: "170dp"
                            pos_hint: {"center_x":.15}
                        
                        MDLabel:
                            text: "Rating Indicators"
                            color: 0, 0, 0, 1
                            adaptive_size: True
                            font_size: "16dp"
                            bold: True
                            pos_hint: {"center_x":.6, "center_y":.25}
                        
                        MDCard:
                            size_hint: None, None
                            size: "130dp", "100dp"
                            radius: [5, 5, 5, 5]
                            pos_hint: {"top": .2, "right": .9}
                            md_bg_color: 0, 0, 0, .1
                            MDRelativeLayout:
                                MDCard:
                                    size_hint: None, None
                                    size: "20dp", "20dp"
                                    radius: [50, 50, 50, 50]
                                    pos_hint: {"top": .9, "right": .2}
                                    md_bg_color: [0,1,0, 1]

                                MDLabel:
                                    text: "Excellent(80 - 100%)"
                                    adaptive_size: True
                                    color: (0, 0, 0, 1)
                                    bold: True
                                    font_size: "10dp"
                                    pos_hint: {"top": .87, "right": .95}

                                MDCard:
                                    size_hint: None, None
                                    size: "20dp", "20dp"
                                    radius: [50, 50, 50, 50]
                                    pos_hint: {"top": .6, "right": .2}
                                    md_bg_color: [0,0,1, 1]

                                MDLabel:
                                    text: "Average(50 - 79%)"
                                    adaptive_size: True
                                    color: (0, 0, 0, 1)
                                    bold: True
                                    font_size: "10dp"
                                    pos_hint: {"top": .6, "right": .9}

                                MDCard:
                                    size_hint: None, None
                                    size: "20dp", "20dp"
                                    radius: [50, 50, 50, 50]
                                    pos_hint: {"top": .3, "right": .2}
                                    md_bg_color: [1,0,0, 1]

                                MDLabel:
                                    text: "Critical (0 - 49%)"
                                    adaptive_size: True
                                    color: (0, 0, 0, 1)
                                    bold: True
                                    font_size: "10dp"
                                    pos_hint: {"top": .3, "right": .85}

                MDCard:
                    size_hint: None, None
                    size: "500dp", "600dp"
                    md_bg_color: .5, 0, 0, .1
                    MDRelativeLayout:
                        MDLabel:
                            text: "Revenue Collection"
                            color: 0, 0, 0, 1
                            adaptive_size: True
                            font_size: "24dp"
                            bold: True
                            pos_hint: {"center_x":.5, "center_y":.95}
                        
                        MDSeparator:
                            height: "1dp"
                            color: 0, 1, 0, 1
                            pos_hint: {"center_x": 0.5, "center_y": .9}

                        MDTextField:
                            pos_hint: {"center_x": 0.5, "center_y": .85}
                            hint_text: "Search"
                            mode: "round"
                            size_hint: None, None
                            size: "350dp", "40dp"
                            line_color_focus: 0, 0, 0, 0  
                            text_color: 0, 0, 0, 1       
                            hint_text_color_normal: 0.4, 0.4, 0.4, 1  
                            md_bg_color: 0.95, 0.95, 0.95, 1  
                            icon_right: "magnify"
                            icon_right_color: 0.3, 0.3, 0.3, 1 
                        
                        MDBoxLayout:
                            id: button_box
                            adaptive_size: True
                            spacing: "8dp"
                            pos_hint: {"center_x": 0.5, "center_y": .8}
                            MDFillRoundFlatButton:
                                id: rentals_btn
                                text: "Rentals"
                                text_color: "white"
                                md_bg_color: (1,0,100/255,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                font_size: "12dp"
                                elevation: 0
                                on_release: root.switch_table("rentals")
                                

                            MDFillRoundFlatButton:
                                id: leased_btn
                                text: "Leased properties"
                                md_bg_color: (0,0,100/255,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                font_size: "12dp"
                                elevation: 0
                                on_release: root.switch_table("leased")

                            MDFillRoundFlatButton:
                                id: sold_btn
                                text: "Sold Properties"
                                md_bg_color: (0,0,100/255,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                font_size: "12dp"
                                elevation: 0
                                on_release: root.switch_table("sold")

                            MDFillRoundFlatButton:
                                id: others_btn
                                text: "Other Revenues"
                                md_bg_color: (0,0,100/255,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                font_size: "12dp"
                                elevation: 0
                                on_release: root.switch_table("others")
                                
                        MDBoxLayout:
                            id: table_container
                            orientation: 'vertical'
                            

                MDCard:
                    size_hint: None, None
                    size: "500dp", "600dp"
                    md_bg_color: 0,0,100/255,1
                    MDRelativeLayout:
                        MDLabel:
                            text: "Expenditure"
                            color: 1, 1, 1, 1
                            adaptive_size: True
                            font_size: "24dp"
                            bold: True
                            pos_hint: {"center_x":.5, "center_y":.95}
                        
                        MDSeparator:
                            height: "1dp"
                            color: 1, 0, 0, 1
                            pos_hint: {"center_x": 0.5, "center_y": .9}

                        MDGridLayout:
                            cols: 3
                            adaptive_height: True
                            adaptive_width: True
                            spacing: "10dp"
                            pos_hint: {"center_x": 0.5, "center_y": .6}
                            MDCard:
                                size_hint: None, None
                                size: "155dp", "155dp"
                                md_bg_color: 1, 1, 1, 1
                                MDRelativeLayout:
                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        pos_hint: {"center_x": .8, "center_y": .8}
                                        user_font_size: "48sp"
                                        theme_text_color: "Custom"
                                        md_bg_color: 0,1,100/255,1

                                    MDLabel:
                                        text: "Bills"
                                        halign: "center"
                                        adaptive_size: True
                                        bold: True
                                        pos_hint: {"center_x": 0.2, "center_y": .8}

                                    MDLabel:
                                        text: "KSH 100,000"
                                        adaptive_size: True
                                        font_size: "20dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.5, "center_y": .5}

                                    MDFillRoundFlatButton:
                                        text: "Explore Expenditure"
                                        md_bg_color: (1,0,100/255,1)
                                        pos_hint: {"center_x": .5, "center_y": .2}
                                        font_size: "12dp"
                                        elevation: 0

                            MDCard:
                                size_hint: None, None
                                size: "155dp", "155dp"
                                md_bg_color: 1, 1, 1, 1
                                MDRelativeLayout:
                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        pos_hint: {"center_x": .8, "center_y": .8}
                                        user_font_size: "48sp"
                                        theme_text_color: "Custom"
                                        md_bg_color: 0,1,100/255,1

                                    MDLabel:
                                        text: "Sallaries"
                                        halign: "center"
                                        adaptive_size: True
                                        font_size: "12dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.2, "center_y": .8}

                                    MDLabel:
                                        text: "KSH 100,000"
                                        adaptive_size: True
                                        font_size: "20dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.5, "center_y": .5}

                                    MDFillRoundFlatButton:
                                        text: "Explore Expenditure"
                                        md_bg_color: (1,0,100/255,1)
                                        pos_hint: {"center_x": .5, "center_y": .2}
                                        font_size: "12dp"
                                        elevation: 0

                            MDCard:
                                size_hint: None, None
                                size: "155dp", "155dp"
                                md_bg_color: 1, 1, 1, 1
                                MDRelativeLayout:
                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        pos_hint: {"center_x": .8, "center_y": .8}
                                        user_font_size: "48sp"
                                        theme_text_color: "Custom"
                                        md_bg_color: 0,1,100/255,1

                                    MDLabel:
                                        text: "Vochures"
                                        halign: "center"
                                        adaptive_size: True
                                        font_size: "12dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.2, "center_y": .8}

                                    MDLabel:
                                        text: "KSH 100,000"
                                        adaptive_size: True
                                        font_size: "20dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.5, "center_y": .5}

                                    MDFillRoundFlatButton:
                                        text: "Explore Expenditure"
                                        md_bg_color: (1,0,100/255,1)
                                        pos_hint: {"center_x": .5, "center_y": .2}
                                        font_size: "12dp"
                                        elevation: 0

                            MDCard:
                                size_hint: None, None
                                size: "155dp", "155dp"
                                md_bg_color: 1, 1, 1, 1
                                MDRelativeLayout:
                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        pos_hint: {"center_x": .8, "center_y": .8}
                                        user_font_size: "48sp"
                                        theme_text_color: "Custom"
                                        md_bg_color: 0,1,100/255,1

                                    MDLabel:
                                        text: "Misleniuos"
                                        halign: "center"
                                        adaptive_size: True
                                        font_size: "12dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.25, "center_y": .8}

                                    MDLabel:
                                        text: "KSH 100,000"
                                        adaptive_size: True
                                        font_size: "20dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.5, "center_y": .5}

                                    MDFillRoundFlatButton:
                                        text: "Explore Expenditure"
                                        md_bg_color: (1,0,100/255,1)
                                        pos_hint: {"center_x": .5, "center_y": .2}
                                        font_size: "12dp"
                                        elevation: 0

                            MDCard:
                                size_hint: None, None
                                size: "155dp", "155dp"
                                md_bg_color: 1, 1, 1, 1
                                MDRelativeLayout:
                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        pos_hint: {"center_x": .8, "center_y": .8}
                                        user_font_size: "48sp"
                                        theme_text_color: "Custom"
                                        md_bg_color: 0,1,100/255,1

                                    MDLabel:
                                        text: "PC Vochures"
                                        halign: "center"
                                        adaptive_size: True
                                        font_size: "12dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.27, "center_y": .8}

                                    MDLabel:
                                        text: "KSH 100,000"
                                        adaptive_size: True
                                        font_size: "20dp"
                                        bold: True
                                        pos_hint: {"center_x": 0.5, "center_y": .5}

                                    MDFillRoundFlatButton:
                                        text: "Explore Expenditure"
                                        md_bg_color: (1,0,100/255,1)
                                        pos_hint: {"center_x": .5, "center_y": .2}
                                        font_size: "12dp"
                                        elevation: 0

                        MDSeparator:
                            height: "1dp"
                            color: 1, 0, 0, 1
                            pos_hint: {"center_x": 0.5, "center_y": .3}
                        
                        MDCard:
                            adaptive_size: True
                            md_bg_color: 0,0,100/255,1
                            padding: "10dp", "3dp"
                            pos_hint: {"center_x": 0.5, "center_y": .3}
                            MDLabel:
                                text: "Upcomming Expenditures"
                                color: "white"
                                halign: "center"
                                adaptive_size: True
                                font_size: "14dp"
                                bold: True

                        BoxLayout:
                            orientation: "vertical"
                            size_hint: None, None
                            size: "490dp", "180dp"
                            pos_hint: {"center_x": 0.5, "center_y": .15}
                            padding: "10dp"
                            MDScrollView:
                                MDList:
                                    spacing: "10dp"
                                    TwoLineListItem:
                                        text: "July Field Activations"
                                        secondary_text: "Deu: 05/06/2024"
                                        theme_text_color: "Custom"
                                        text_color: (1, 1, 1, 1)
                                        secondary_theme_text_color: "Custom"
                                        secondary_text_color: (1,1,1,1)
                                        bg_color: (1,0,100/255,1)
                                        radius: [20,20,20,20]
                                        bold: True
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 1, 1, 1, 1
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "KSH 30000"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "10dp", "5dp"
                                                    font_size: "12dp"
                                                    bold: True

                                    TwoLineListItem:
                                        text: "July Field Activations"
                                        secondary_text: "Deu: 05/06/2024"
                                        theme_text_color: "Custom"
                                        text_color: (1, 1, 1, 1)
                                        secondary_theme_text_color: "Custom"
                                        secondary_text_color: (1,1,1,1)
                                        bg_color: (1,0,100/255,1)
                                        radius: [20,20,20,20]
                                        bold: True
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 1, 1, 1, 1
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "KSH 30000"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "10dp", "5dp"
                                                    font_size: "12dp"
                                                    bold: True
                                    
                                    TwoLineListItem:
                                        text: "July Field Activations"
                                        secondary_text: "Deu: 05/06/2024"
                                        theme_text_color: "Custom"
                                        text_color: (1, 1, 1, 1)
                                        secondary_theme_text_color: "Custom"
                                        secondary_text_color: (1,1,1,1)
                                        bg_color: (1,0,100/255,1)
                                        radius: [20,20,20,20]
                                        bold: True
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 1, 1, 1, 1
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "KSH 30000"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "10dp", "5dp"
                                                    font_size: "12dp"
                                                    bold: True
'''
Builder.load_string(d_kv)

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
            row_data = [("Unit A", "10,000"), ("Unit B", "12,000"), ("Unit B", "12,000"), ("Unit B", "12,000"),("Unit B", "12,000"), ("Unit B", "12,000"),("Unit A", "10,000"), ("Unit B", "12,000"),("Unit A", "10,000"), ("Unit B", "12,000")]
        elif category == "leased":
            # title = "Leased Properties"
            row_data = [("Office 1", "50,000")]
        elif category == "sold":
            # title = "Sold Properties"
            row_data = [("House X", "2,000,000")]
        elif category == "others":
            # title = "Other Revenues"
            row_data = [("Parking", "3,000"), ("Penalty", "1,000")]
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
            column_data=[("Property", dp(40)), ("Amount", dp(40))],
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