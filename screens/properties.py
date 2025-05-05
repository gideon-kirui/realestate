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
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: "20dp"
                    MDBoxLayout:
                        orientation: 'horizontal'
                        adaptive_size: True
                        pos_hint: {"center_x": 0.45}
                        spacing: "20dp"
                        MDTextField:
                            id: search_field
                            hint_text: "Search"
                            mode: "round"
                            size_hint: None, None
                            size: "380dp", "40dp"
                            line_color_focus: 0, 0, 0, 0  
                            text_color: 0, 0, 0, 1       
                            hint_text_color_normal: 0.4, 0.4, 0.4, 1  
                            md_bg_color: 0.95, 0.95, 0.95, 1  
                            icon_right: "magnify"
                            icon_right_color: 0.3, 0.3, 0.3, 1 
                            on_text: root.on_search(self.text)

                        MDRelativeLayout:
                            MDIconButton:
                                id: filter_button
                                icon: "filter-variant"
                                adaptive_size: True
                                icon_size: "24dp"
                                pos_hint: {"center_y": 0.5}
                                on_release: root.open_filter_menu()

                    MDTabs:
                        id: tabs
                        tab_bar_height: "30dp"
                        on_tab_switch: root.on_tab_switch(*args)
                        background_color: 1, 1, 1, 1
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
                md_bg_color: 0.95, 0.95, 0.95, 1
                orientation: 'vertical'
                padding: "10dp"
                spacing: "10dp"

                MDRelativeLayout:
                    size_hint_y: None
                    height: "200dp"  # Give it enough space for image + label

                    MDLabel:
                        text: "LandLords"
                        adaptive_size: True
                        color: "black"
                        bold: True
                        pos_hint: {"top": 1, "center_x": 0.5}

                    FitImage:
                        source: "./p.png"
                        size_hint: None, None
                        size: "300dp", "180dp"
                        radius: [12]
                        pos_hint: {"top": 0.75, "center_x": 0.5}


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
        ]
        self.filter_menu = MDDropdownMenu(
            caller=self.ids.filter_button,
            items=self.menu_items,
            width_mult=3,
        )

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