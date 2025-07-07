from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.fitimage import FitImage

# --- KV Layout ---
d_kv = '''
<PropertiesScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDGridLayout:
            cols: 2
            spacing: "10dp"
            padding: "10dp"
            adaptive_height: True
            adaptive_width: True
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            MDCard:
                size_hint: None, None
                size: "760dp", "580dp"
                md_bg_color: (0,0,100/255,1)
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: "20dp"
                    MDCard:
                        size_hint: None, None
                        size: "600dp", "60dp"
                        pos_hint: {"center_x": 0.39}
                        md_bg_color: 1,1,1,1
                        spacing: "20dp"
                        radius: [0,10,10,0]
                        MDRelativeLayout:
                            MDTextField:
                                id: search_field
                                hint_text: "Search"
                                mode: "round"
                                size_hint: None, None
                                size: "380dp", "40dp"
                                line_color_focus: 0, 0, 0, 0  
                                text_color: 0, 0, 0, 1       
                                hint_text_color_normal: 0.4, 0.4, 0.4, 1  
                                md_bg_color: 1, 1, 1, 1  
                                pos_hint: {"center_x": .5, "center_y": .6}
                                icon_right: "magnify"
                                icon_right_color: 0.3, 0.3, 0.3, 1 
                                on_text: root.on_search(self.text)

                            MDIconButton:
                                id: filter_button
                                icon: "filter-variant"
                                adaptive_size: True
                                icon_size: "24dp"
                                pos_hint: {"center_x": .95, "center_y": .6}
                                on_release: root.open_filter_menu()
                            
                            MDIconButton:
                                icon: "plus"
                                adaptive_size: True
                                pos_hint: {"center_x": .05, "center_y": .6}
                                user_font_size: "48sp"
                                theme_text_color: "Custom"
                                md_bg_color: 0,1,100/255,1

                    MDTabs:
                        id: tabs
                        tab_bar_height: "30dp"
                        on_tab_switch: root.on_tab_switch(*args)
                        background_color: 1, 1, 1, 0
                        text_color_normal: 0, 1, 0, 1
                        text_color_active: 0, .9, 0, .9
                        indicator_color: 1, 0, 0, 1
                        elevation: 0
                        Tab:
                            title: "Rentals"

                        Tab:
                            title: "Sale"

                        Tab:
                            title: "Lease"

            MDCard:
                id: details_card
                size_hint: None, None
                size: "460dp", "585dp"
                md_bg_color: 1,0,100/255,1
                orientation: 'vertical'
                padding: "10dp"
                spacing: "10dp"

                MDRelativeLayout:
                    MDLabel:
                        text: "Past Occupants"
                        adaptive_size: True
                        color: (0,0,100/255,1)
                        font_size: "14dp"
                        bold: True
                        pos_hint: {"top": 1, "center_x": 0.5}

                    MDBoxLayout:
                        id: history_table
                        size_hint: None, None
                        size: "455dp", "270dp"
                        orientation: 'vertical'
                        padding: "10dp"
                        pos_hint: {"top": .98, "center_x": 0.5}
                        elevation: 0

                    MDGridLayout:
                        cols: 2
                        adaptive_size: True
                        spacing: "10dp"
                        pos_hint: {"top": 0.5, "center_x": 0.5}
                        MDCard:
                            size_hint: None, None
                            size: "210dp", "280dp"
                            md_bg_color: 1, 1, 1, 1
                            MDRelativeLayout:
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .97, "center_x": 0.45}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Care Taker:"
                                        adaptive_size: True
                                        color: (0,0,100/255,1)
                                        bold: True
                                    MDLabel:
                                        text: "Fred Mwahi"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDSeparator:
                                    height: "1dp"
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": 0.5, "center_y": .88}

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .84, "center_x": 0.44}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Category:"
                                        adaptive_size: True
                                        color: (0,0,100/255,1)
                                        bold: True
                                    MDLabel:
                                        text: "Appartment"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDRaisedButton:
                                    text: "Download Agreement Form"
                                    on_release: app.open_file_chooser()
                                    adaptive_size: True
                                    font_size: "10sp"
                                    pos_hint: {"center_x": .4, "center_y": .67}
                                    elevation: 0
                                
                                MDRaisedButton:
                                    text: "Download Terms and Conditions"
                                    on_release: app.open_file_chooser()
                                    adaptive_size: True
                                    font_size: "10sp"
                                    pos_hint: {"center_x": .45, "center_y": .5}
                                    elevation: 0

                                MDRaisedButton:
                                    text: "Download Application Form"
                                    on_release: app.open_file_chooser()
                                    adaptive_size: True
                                    font_size: "10sp"
                                    pos_hint: {"center_x": .4, "center_y": .33}
                                    elevation: 0
                                
                                MDSeparator:
                                    height: "1dp"
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": 0.5, "center_y": .2}
                                
                                MDTextButton:
                                    text: "See more"
                                    pos_hint: {"center_x": 0.8, "center_y": .12}
                                    theme_text_color: "Custom"
                                    text_color: "#00BFFF"

                        MDCard:
                            size_hint: None, None
                            size: "210dp", "280dp"
                            padding: "10dp"
                            md_bg_color: 1, 1, 1, 1
                            MDRelativeLayout:
                                MDLabel:
                                    text: "Amenities"
                                    halign: "left"  
                                    theme_text_color: "Custom"
                                    text_color: (0,0,100/255,1)
                                    size_hint_x: 0.7
                                    pos_hint: {"top": .95, "center_x": 0.35}
                                    text_size: self.width, None
                                    adaptive_height: True
                                    font_size: "16sp"
                                    bold:True
                                
                                MDSeparator:
                                    height: "1dp"
                                    size_hint_x: None
                                    width: "120dp"  
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": .735, "center_y": .91}

                                MDLabel:
                                    text: "4 Bedroom\
                                            2 Kichen\
                                            Next to a river\
                                            20min Walk From town\
                                            Electricity available\
                                            Security asured\
                                            Cabroed Compound\
                                            Electric Fence\
                                            Perimiter wall\
                                            Titled floors and gipsome seiling\
                                            Parcking Lounge\
                                            Children play ground"

                                    halign: "left"  
                                    theme_text_color: "Primary"
                                    size_hint_x: 0.7
                                    pos_hint: {"top": .85, "center_x": 0.5}
                                    size_hint: None, None
                                    size: "200dp", "220dp"
                                    font_size: "14sp"


<Tab>:
    name: ''
    MDBoxLayout:
        id: table_box
        orientation: 'vertical'
        padding: "10dp"
'''

Builder.load_string(d_kv)

# --- Tab class ---
class Tab(MDBoxLayout, MDTabsBase):
    pass

# --- Main Screen class ---
class PropertiesScreen(MDScreen):
    
    table_cache = {}

    def on_kv_post(self, base_widget):
        first_tab = self.ids.tabs.get_slides()[0]
        self.load_table("Rentals", first_tab.ids.table_box)

        self.menu_items = [
            {"text": "Available", "on_release": lambda x="Available": self.filter_table(x)},
            {"text": "Occupied", "on_release": lambda x="Occupied": self.filter_table(x)},
            {"text": "Sold", "on_release": lambda x="Sold": self.filter_table(x)},
            {"text": "Leased", "on_release": lambda x="Leased": self.filter_table(x)},
            {"text": "Empty", "on_release": lambda x="Empty": self.filter_table(x)},
            {"text": "On Renovation", "on_release": lambda x="Renovation": self.filter_table(x)},
            {"text": "Available for sale", "on_release": lambda x="For Sale": self.filter_table(x)},
            {"text": "Available for lease", "on_release": lambda x="For Lease": self.filter_table(x)},
        ]
        self.filter_menu = MDDropdownMenu(
            caller=self.ids.filter_button,
            items=self.menu_items,
            width_mult=3,
        )

        tcont = self.ids.history_table
        history_table = MDDataTable(
            size_hint=(1, 0.6),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            rows_num=4,
            column_data=[
                ("ID", dp(20)),
                ("F Name", dp(20)),
                ("Status", dp(20)),
                ("Approval", dp(20)),
            ],
            row_data=[
                ("GU-10025E", "Alice", "Active", "In Debt"),
                ("GU-10025E", "Bob", "Acitve-A", "Cleared"),
                ("GU-10025E", "Charlie", "Active-A", "Cleard"),
                ("GU-10025E", "Diana", "N-Active", "In Debt"),
                ("GU-10025E", "Eve", "N-Active", "Cleared"),
            ]
        )
        tcont.add_widget(history_table)
        tcont.row_height = dp(20)

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        self.load_table(tab_text, instance_tab.ids.table_box)

    def load_table(self, category, container):
        container.clear_widgets()
        if category in self.table_cache:
            container.add_widget(self.table_cache[category])
            return

        if category == "Rentals":
            row_data = [
                ("00123", "Sunset Villas", "Downtown", "Occupied"),
                ("00234", "Green Acres", "Uptown", "Empty"),
                ("00564", "Blue Horizon", "Riverside", "On Renovation"),
                ("00873", "Palm Heights", "Midtown", "Occupied"),
                ("00890", "By Grace homes", "Rvist", "For Lease"),
                ("00750", "Kiamunyi Phase II", "Kiamunyi", "For Sale"),
                ("00750", "Blessed Hostels", "Kabarak", "For rent"),
                ("00750", "Sweet Banana", "Freehold", "Occupied"),
            ]
        elif category == "Sale":
            row_data = [
                ("00873", "Maple Estate", "Lakeside", "Available"),
                ("000865", "Stone Ridge", "Hills", "Sold"),
            ]
        elif category == "Lease":
            row_data = [
                ("89965", "Ocean Breeze", "Coastal", "Leased"),
                ("76854", "Forest View", "Suburbs", "Available"),
            ]
        else:
            row_data = []

        table = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Property ID", dp(25)),
                ("Owners Name", dp(40)),
                ("Location", dp(50)),
                ("Status", dp(30)),
            ],
            row_data=row_data,
        )

        self.table_cache[category] = table
        container.add_widget(table)


    def open_filter_menu(self):
        self.filter_menu.caller = self.ids.filter_button
        self.filter_menu.open()

    def filter_table(self, status):
        self.filter_menu.dismiss()
        current_tab = self.ids.tabs.get_current_tab()
        category = current_tab.title
        container = current_tab.ids.table_box

        if category not in self.table_cache:
            return

        # Filter data from cache
        original_table = self.table_cache[category]
        filtered_data = [row for row in original_table.row_data if status.lower() in row[3].lower()]
        
        # Create and show filtered table
        container.clear_widgets()
        table = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            column_data=original_table.column_data,
            row_data=filtered_data,
        )
        container.add_widget(table)

    def on_search(self, query):
        query = query.lower()
        current_tab = self.ids.tabs.get_current_tab().title
        original_rows = self.get_original_rows(current_tab)

        if not query:
            filtered_rows = original_rows
        else:
            filtered_rows = [
                row for row in original_rows
                if any(query in str(cell).lower() for cell in row)
            ]

        container = self.ids.tabs.get_current_tab().ids.table_box
        container.clear_widgets()

        table = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Property ID", dp(25)),
                ("Owners Name", dp(40)),
                ("Location", dp(50)),
                ("Status", dp(30)),
            ],
            row_data=filtered_rows,
        )
        container.add_widget(table)

    def get_original_rows(self, category):
        data = {
            "Rentals": [
                ("00123", "Sunset Villas", "Downtown", "Occupied"),
                ("00234", "Green Acres", "Uptown", "Empty"),
                ("00564", "Blue Horizon", "Riverside", "On Renovation"),
                ("00873", "Palm Heights", "Midtown", "Occupied"),
                ("00890", "By Grace homes", "Rvist", "For Lease"),
                ("00750", "Kiamunyi Phase II", "Kiamunyi", "For Sale"),
                ("00750", "Blessed Hostels", "Kabarak", "For rent"),
                ("00750", "Sweet Banana", "Freehold", "Occupied"),
            ],
            "Sale": [
                ("00873", "Maple Estate", "Lakeside", "Available"),
                ("000865", "Stone Ridge", "Hills", "Sold"),
            ],
            "Lease": [
                ("89965", "Ocean Breeze", "Coastal", "Leased"),
                ("76854", "Forest View", "Suburbs", "Available"),
            ]
        }
        return data.get(category, [])