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

Builder.load_file("kv/properties.kv")

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