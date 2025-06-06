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

d_kv = '''
<FinanceGraphArea>:
<FinanceScreen>:
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
                            id: finance_search_field
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
                                id: finance_filter_button
                                icon: "filter-variant"
                                adaptive_size: True
                                icon_size: "24dp"
                                pos_hint: {"center_y": 0.5}
                                on_release: root.open_filter_menu()

                    MDTabs:
                        id: finance_tabs
                        tab_bar_height: "30dp"
                        on_tab_switch: root.on_tab_switch(*args)
                        background_color: 1, 1, 1, 1
                        text_color_normal: 0, 1, 0, 1
                        text_color_active: 0, .9, 0, .9
                        indicator_color: 1, 0, 0, 1
                        elevation: 0
                        FinanceTab:
                            title: "Rent Properties"

                        FinanceTab:
                            title: "Lease properties"

                        FinanceTab:
                            title: "Sale Properties"

            MDCard:
                id: details_card
                size_hint: None, None
                size: "460dp", "585dp"
                md_bg_color: 0.95, 0.95, 0.95, 1
                orientation: 'vertical'
                padding: "10dp"
                spacing: "10dp"
                MDRelativeLayout:
                    FinanceGraphArea:
                        size_hint: 1, None
                        height: self.parent.height - dp(300) 
                        pos_hint: {"top": 1}

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
                                    pos_hint: {"top": .95, "center_x": 0.4}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Tenant:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "Gideon Kirui"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDSeparator:
                                    height: "1dp"
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": 0.5, "center_y": .85}

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .8, "center_x": 0.45}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Rental Amount:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "4,000"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .7, "center_x": 0.41}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Water Charges:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "12"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .6, "center_x": 0.45}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Power Chages:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "4,000"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .5, "center_x": 0.45}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Other Charges:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "4,000"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"
                                
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .4, "center_x": 0.53}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Penalties:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "400,000"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                                MDSeparator:
                                    height: "1dp"
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": 0.5, "center_y": .26}
                                
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .23, "center_x": 0.47}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Total Amount:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "4,000"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"
                                        bold: True
                                    
                                MDSeparator:
                                    height: "1dp"
                                    color: 0, 1, 0, 1
                                    pos_hint: {"center_x": 0.5, "center_y": .14}

                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    adaptive_size: True
                                    pos_hint: {"top": .1, "center_x": 0.45}
                                    spacing: "10dp"
                                    MDLabel:
                                        text: "Owner:"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                    MDLabel:
                                        text: "Fred Mwahi"
                                        adaptive_size: True
                                        color: "grey"
                                        font_size: "12sp"

                        MDCard:
                            size_hint: None, None
                            size: "210dp", "280dp"
                            padding: "10dp"
                            md_bg_color: 1, 1, 1, 1
                            

<FinanceTab>:
    name: ''
    MDBoxLayout:
        id: finance_table_box
        orientation: 'vertical'
        padding: "10dp"

'''
Builder.load_string(d_kv)

class FinanceTab(MDBoxLayout, MDTabsBase):
    pass

class FinanceScreen(MDScreen):
    finace_table_cache = {}
    def on_kv_post(self, base_widget):
        finance_first_tab = self.ids.finance_tabs.get_slides()[0]
        self.load_finance_table("Rent Properties", finance_first_tab.ids.finance_table_box) 

        self.menu_items = [
            {"text": "Active", "on_release": lambda x="Active": self.filter_table(x)},
            {"text": "Suspended", "on_release": lambda x="Suspended": self.filter_table(x)},
            {"text": "Inactive", "on_release": lambda x="Inactive": self.filter_table(x)},
        ]
        self.filter_menu = MDDropdownMenu(
            caller=self.ids.finance_filter_button,
            items=self.menu_items,
            width_mult=3,
        )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tabs_label, tab_text):
        self.load_finance_table(tab_text, instance_tab.ids.finance_table_box)

    def load_finance_table(self, category, container):
        finance_table = MDDataTable()
        container.clear_widgets()
        if category in self.finace_table_cache:
            container.add_widget(self.finace_table_cache[category])
            return

        if category == "Rent Properties":
            row_data = [
                ("00123", "Sunset Villas", "Downtown", "Active"),
                ("00234", "Green Acres", "Uptown", "Active"),
                ("00564", "Blue Horizon", "Riverside", "Active"),
                ("00873", "Palm Heights", "Midtown", "Active"),
                ("00890", "By Grace homes", "Rvist", "Inactive"),
                ("00750", "Kiamunyi Phase II", "Kiamunyi", "Suspended"),
                ("00750", "Blessed Hostels", "Kabarak", "Suspended"),
                ("00750", "Sweet Banana", "Freehold", "Inactive"),
            ]
        elif category == "Lease properties":
            row_data = [
                ("00873", "Maple Estate", "Lakeside", "Available"),
                ("000865", "Stone Ridge", "Hills", "Sold"),
            ]
        elif category == "Sale Properties":
            row_data = [
                ("89965", "Ocean Breeze", "Coastal", "Leased"),
                ("76854", "Forest View", "Suburbs", "Available"),
            ]
        else:
            row_data = []
        
        finance_table = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=7,
            column_data=[
                ("Property ID", dp(25)),
                ("Property Name", dp(40)),
                ("Property Location", dp(50)),
                ("Payment Status", dp(30)),
            ],
            row_data=row_data,
        )

        self.finace_table_cache[category] = finance_table
        container.add_widget(finance_table)

    def open_filter_menu(self):
        self.filter_menu.caller = self.ids.finance_filter_button
        self.filter_menu.open()

    def filter_table(self, status):
        self.filter_menu.dismiss()
        current_tab = self.ids.finance_tabs.get_current_tab()
        category = current_tab.title
        container = current_tab.ids.finance_table_box

        if category not in self.finace_table_cache:
            return

        # Filter data from cache
        original_table = self.finace_table_cache[category]
        filtered_data = [row for row in original_table.row_data if status.lower() in row[3].lower()]
        
        # Create and show filtered table
        container.clear_widgets()
        finace_table = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            column_data=original_table.column_data,
            row_data=filtered_data,
        )
        container.add_widget(finace_table)

    def on_search(self, query):
        query = query.lower()
        current_tab = self.ids.finance_tabs.get_current_tab().title
        original_rows = self.get_original_rows(current_tab)

        if not query:
            filtered_rows = original_rows
        else:
            filtered_rows = [
                row for row in original_rows
                if any(query in str(cell).lower() for cell in row)
            ]

        container = self.ids.finance_tabs.get_current_tab().ids.finance_table_box
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
            "Rent Properties": [
                ("00123", "Sunset Villas", "Downtown", "Active"),
                ("00234", "Green Acres", "Uptown", "Active"),
                ("00564", "Blue Horizon", "Riverside", "Active"),
                ("00873", "Palm Heights", "Midtown", "Active"),
                ("00890", "By Grace homes", "Rvist", "Inactive"),
                ("00750", "Kiamunyi Phase II", "Kiamunyi", "Suspended"),
                ("00750", "Blessed Hostels", "Kabarak", "Suspended"),
                ("00750", "Sweet Banana", "Freehold", "Inactive"),
            ],
            "Lease properties": [
                ("00873", "Maple Estate", "Lakeside", "Available"),
                ("000865", "Stone Ridge", "Hills", "Sold"),
            ],
            "Sale Properties": [
                ("89965", "Ocean Breeze", "Coastal", "Leased"),
                ("76854", "Forest View", "Suburbs", "Available"),
            ]
        }
        return data.get(category, [])

class FinanceGraphArea(AnchorLayout):
    def on_kv_post(self, base_widget):
        # Example: Line graph
        weeks = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        percentage = [0,1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        fig, ax = plt.subplots()
        ax.plot(weeks, percentage, marker='o')
        # ax.set_title("Sample Line Graph")
        # ax.set_xlabel("X Axis")
        # ax.set_ylabel("Y Axis")

        graph = FigureCanvasKivyAgg(fig)
        self.add_widget(graph)