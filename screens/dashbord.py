from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import numpy as np
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock


d_kv = '''

<TntsCircularProgressBar>
    canvas.before:
        Color:
            rgba: root.bar_colortn + [0.3]
        Line:
            width: root.bar_widthtn
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_colortn
        Line:
            width: root.bar_widthtn
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_valuetn*3.6)

    MDRelativeLayout:
        MDLabel:
            text: root.texttn
            color: root.bar_colortn
            adaptive_size: True
            font_size: "16dp"
            pos_hint: {"center_x":.5, "center_y":.6}
            valuetn: 99

        MDLabel:
            text: "100 / 120"
            color: root.bar_colortn
            adaptive_size: True
            font_size: "10dp"
            pos_hint: {"center_x":.5, "center_y":.35}

<CircularProgressBar>
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
    
    MDLabel:
        text: root.text
        color: root.bar_color
        adaptive_size: True
        font_size: "40dp"
        pos_hint: {"center_x":.2, "center_y":.5}
        value: 50

<CircularProgressBarRe>
    canvas.before:
        Color:
            rgba: root.bar_colorre + [0.3]
        Line:
            width: root.bar_widthre
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_colorre
        Line:
            width: root.bar_widthre
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_valuere*3.6)
    
    MDLabel:
        text: root.textre
        color: root.bar_colorre
        adaptive_size: True
        font_size: "20dp"
        pos_hint: {"center_x":.2, "center_y":.5}
        valuere: 90

        
<CircularProgressBarPp>
    canvas.before:
        Color:
            rgba: root.bar_colorpp + [0.3]
        Line:
            width: root.bar_widthpp
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_colorpp
        Line:
            width: root.bar_widthpp
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_valuepp*3.6)
    
    MDLabel:
        text: root.textpp
        color: root.bar_colorpp
        adaptive_size: True
        font_size: "20dp"
        pos_hint: {"center_x":.2, "center_y":.5}
        valuepp: 70

<CircularProgressBarLp>
    canvas.before:
        Color:
            rgba: root.bar_colorlp + [0.3]
        Line:
            width: root.bar_widthlp
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_colorlp
        Line:
            width: root.bar_widthlp
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_valuelp*3.6)
    
    MDLabel:
        text: root.textlp
        color: root.bar_colorlp
        adaptive_size: True
        font_size: "20dp"
        pos_hint: {"center_x":.2, "center_y":.5}
        valuelp: 99
    
    
<GraphArea>:
    
        
<DashboardScreen>:
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
                size: "600dp", "290dp"
                md_bg_color: 0.95, 0.95, 0.95, 1
                MDGridLayout:
                    cols: 2
                    spacing: "10dp"
                    padding: "10dp"
                    adaptive_height: True
                    size_hint_x: None
                    width: self.minimum_width
                    pos_hint: {"center_x": 0.5, "center_y": 0.5}

                    MDCard:
                        size_hint: None, None
                        size: "280dp", "130dp"
                        md_bg_color: "#ffffff"
                        MDRelativeLayout:
                            MDLabel:
                                text: "KSH 130,000"
                                adaptive_size: True
                                color: (0.58, 0, 0.56, 1)
                                bold: True
                                font_style: "H5"
                                pos_hint: {"top": .9, "x": .05}
                            
                            MDIcon:
                                icon: "cash"
                                font_size: "34dp"
                                adaptive_size: True
                                pos_hint: {"top": .95, "right": .95}
                                theme_text_color: "Custom"
                                text_color: 0, 0, 1, 1 
                            
                            MDIcon:
                                icon: "asset/images/icons/moneyup.png"
                                font_size: "70dp"
                                adaptive_size: True
                                pos_hint: {"top": .7, "right": .86}
                                theme_text_color: "Custom"
                                text_color: 1, 0, 0, 1 

                            MDCard:
                                adaptive_size: True
                                radius: [5, 5, 5, 5]
                                pos_hint: {"top": .6, "right": .36}
                                md_bg_color: (0, 1, 0, 1)

                                MDBoxLayout:
                                    orientation: "horizontal"
                                    adaptive_size: True  
                                    padding: "5dp"
                                    spacing: "5dp"

                                    MDIcon:
                                        icon: "plus"
                                        font_size: "14dp"
                                        adaptive_size: True
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1  

                                    MDLabel:
                                        text: "56.00%"
                                        adaptive_size: True
                                        font_style: "Caption"
                                        halign: "center"
                                        valign: "center"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1  

                                    MDIcon:
                                        icon: "arrow-up"
                                        font_size: "14dp"
                                        adaptive_size: True
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1 

                            MDLabel:
                                text: "Total Income"
                                adaptive_size: True
                                color: "black"
                                bold: True
                                pos_hint: {"top": .3, "x": .05}
 

                    MDCard:
                        size_hint: None, None
                        size: "280dp", "130dp"
                        md_bg_color: "#ffffff"
                        MDRelativeLayout:
                            
                            MDCard:
                                size_hint: None, None
                                size: "80dp", "80dp"
                                radius: [50, 50, 50, 50]
                                pos_hint: {"top": .95, "right": .33}
                                md_bg_color: "#efa8ff"
                                elavetion: 5

                                MDRelativeLayout:
                                    MDLabel:
                                        text: "1000"
                                        adaptive_size: True
                                        color: (0, 0, 0, 1)
                                        bold: True
                                        font_style: "H5"
                                        pos_hint: {"top": .69, "x": .15}
                            
                            MDIcon:
                                icon: "home-city"
                                font_size: "28dp"
                                adaptive_size: True
                                pos_hint: {"top": .95, "right": .95}
                                theme_text_color: "Custom"
                                text_color: 0, 0, 1, 1 
                            
                            MDIcon:
                                icon: "asset/images/icons/prpt.png"
                                font_size: "80dp"
                                adaptive_size: True
                                pos_hint: {"top": .8, "right": .83}
                                theme_text_color: "Custom"
                                text_color: 1, 0, 0, 1 

                            MDLabel:
                                text: "Total Properties"
                                adaptive_size: True
                                color: "black"
                                bold: True
                                pos_hint: {"top": .27, "x": .05}

                            MDCard:
                                adaptive_size: True
                                radius: [5, 5, 5, 5]
                                pos_hint: {"top": .3, "right": .95}
                                md_bg_color: (0, 1, 0, 1)

                                MDBoxLayout:
                                    orientation: "horizontal"
                                    adaptive_size: True  
                                    padding: "5dp"
                                    spacing: "5dp"
                                    

                                    # Left icon
                                    MDIcon:
                                        icon: "plus"
                                        font_size: "14dp"
                                        adaptive_size: True
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1  

                                    # Label (text)
                                    MDLabel:
                                        text: "16.00%"
                                        adaptive_size: True
                                        font_style: "Caption"
                                        halign: "center"
                                        valign: "center"
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1   

                                    # Right icon
                                    MDIcon:
                                        icon: "arrow-up"
                                        font_size: "14dp"
                                        adaptive_size: True
                                        theme_text_color: "Custom"
                                        text_color: 1, 1, 1, 1  
                            
                    MDCard:
                        size_hint: None, None
                        size: "280dp", "130dp"
                        md_bg_color: 0, 0, 0, 0.0
                        MDGridLayout:
                            cols: 2
                            spacing: "2dp"
                            pos_hint: {"center_x": 0.7, "center_y": 0.5}
                            adaptive_height: True
                            adaptive_width: True
                            MDCard:
                                size_hint: None, None
                                size: "135dp", "120dp"
                                md_bg_color: "#ffffff"
                                MDRelativeLayout:
                                    MDLabel:
                                        text: "Tenants"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                        pos_hint: {"top": .95, "x": .08}

                                    TntsCircularProgressBar:
                                        size_hint: None, None
                                        size: 70, 70
                                        pos_hint: {"center_x":.5, "center_y":.4}       

                            MDCard:
                                size_hint: None, None
                                size: "135dp", "120dp"
                                md_bg_color: "#ffffff"
                                MDRelativeLayout:
                                    MDLabel:
                                        text: "LandLords"
                                        adaptive_size: True
                                        color: "black"
                                        bold: True
                                        pos_hint: {"top": .95, "x": .4}

                                    BoxLayout:
                                        id: landlords_donut_box
                                        size_hint: None, None
                                        size: "80dp", "100dp"
                                        pos_hint: {"center_x": 0.3, "center_y": 0.5}
                                    
                                    MDGridLayout:
                                        cols: 2
                                        adaptive_height: True
                                        adaptive_width: True
                                        spacing: "5dp"
                                        pos_hint: {"center_x": 0.77, "center_y": .23}

                                        MDCard:
                                            size_hint: None, None
                                            size: "10dp", "10dp"
                                            radius: [50]
                                            md_bg_color: "#4CAF50"
                                        MDLabel:
                                            text: "Active"
                                            adaptive_size: True
                                            font_size: "10dp"
                                            color: "black"
                                            bold: True

                                        MDCard:
                                            size_hint: None, None
                                            size: "10dp", "10dp"
                                            radius: [50]
                                            md_bg_color: "#FFC107"
                                        MDLabel:
                                            text: "Suspended"
                                            adaptive_size: True
                                            font_size: "8dp"
                                            color: "black"
                                            bold: True

                                        MDCard:
                                            size_hint: None, None
                                            size: "10dp", "10dp"
                                            radius: [50]
                                            md_bg_color: "#FF1100"
                                        MDLabel:
                                            text: "Inactive"
                                            adaptive_size: True
                                            font_size: "8dp"
                                            color: "black"
                                            bold: True

                    MDCard:
                        size_hint: None, None
                        size: "280dp", "130dp"
                        md_bg_color: "#ffffff"
                        MDRelativeLayout:
                            MDLabel:
                                text: "Vochures"
                                adaptive_size: True
                                color: "black"
                                bold: True
                                pos_hint: {"top": .95, "x": .02}
                            
                            MDIcon:
                                icon: "ticket-percent"
                                font_size: "28dp"
                                adaptive_size: True
                                pos_hint: {"top": .95, "right": .95}
                                theme_text_color: "Custom"
                                text_color: 0, 0, 1, 1

                            BoxLayout:
                                id: vochures_chart_box
                                size_hint: None, None
                                size: "200dp", "120dp"
                                pos_hint: {"center_x": 0.5, "center_y": 0.4}


            MDCard:
                size_hint: None, None
                size: "600dp", "290dp"
                md_bg_color: 0.95, 0.95, 0.95, 1
                MDRelativeLayout:
                    MDCard:
                        adaptive_size: True
                        radius: [5, 5, 5, 5]
                        pos_hint: {"top": .98, "right": .5}
                        md_bg_color: (0, 1, 0, 1)

                        MDBoxLayout:
                            orientation: "horizontal"
                            adaptive_size: True  
                            padding: "5dp"
                            MDLabel:
                                text: "Collection for the month Ending 31/04/2025"
                                adaptive_size: True
                                color: (1, 1, 1, 1)
                                bold: True
                                font_size: "14dp"

                    CircularProgressBar:
                        size_hint: None, None
                        size: 180, 180
                        pos_hint: {"center_x":.2, "center_y":.5}

                    MDLabel:
                        text: "Total Collection"
                        color: (1,0,100/255, 1)
                        adaptive_size: True
                        font_size: "20dp"
                        bold: True
                        pos_hint: {"top": .13, "x": .08}
                    
                    MDCard:
                        size_hint: None, None
                        size: "70dp", "60dp"
                        radius: [5, 5, 5, 5]
                        pos_hint: {"top": .3, "right": .48}
                        md_bg_color: 1, 1, 1, 1
                        MDRelativeLayout:
                            MDCard:
                                size_hint: None, None
                                size: "15dp", "15dp"
                                radius: [50, 50, 50, 50]
                                pos_hint: {"top": .85, "right": .3}
                                md_bg_color: [1,0,100/255]
                            
                            MDCard:
                                size_hint: None, None
                                size: "15dp", "15dp"
                                radius: [50, 50, 50, 50]
                                pos_hint: {"top": .4, "right": .3}
                                md_bg_color: [1,0,100/255, 0.3]

                            MDLabel:
                                text: "Colected"
                                adaptive_size: True
                                color: (0, 0, 0, 1)
                                bold: True
                                font_size: "10dp"
                                pos_hint: {"top": .85, "right": .95}

                            MDLabel:
                                text: "Pending"
                                adaptive_size: True
                                color: (0, 0, 0, 1)
                                bold: True
                                font_size: "10dp"
                                pos_hint: {"top": .4, "right": .95}

                    MDCard:
                        size_hint: None, None
                        size: "80dp", "80dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .95, "right": .65}
                        md_bg_color: 1, 1, 1, 1
                        
                    CircularProgressBarRe:
                        size_hint: None, None
                        size: 80, 80
                        pos_hint: {"center_x":.58, "center_y":.8}
                            
                    MDLabel:
                        text: "Rental Payments"
                        adaptive_size: True
                        color: (0, 0, 0, 1)
                        bold: True
                        font_size: "16dp"
                        pos_hint: {"top": .87, "x": .7}

                        
                    MDCard:
                        size_hint: None, None
                        size: "80dp", "80dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .61, "right": .65}
                        md_bg_color: 1, 1, 1, 1
                        
                    CircularProgressBarPp:
                        size_hint: None, None
                        size: 80, 80
                        pos_hint: {"center_x":.58, "center_y":.485}
                    
                    MDLabel:
                        text: "Property Purchases"
                        adaptive_size: True
                        color: (0, 0, 0, 1)
                        bold: True
                        font_size: "16dp"
                        pos_hint: {"top": .53, "x": .7}

                    MDCard:
                        size_hint: None, None
                        size: "80dp", "80dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .3, "right": .65}
                        md_bg_color: 1, 1, 1, 1
                        
                    CircularProgressBarLp:
                        size_hint: None, None
                        size: 80, 80
                        pos_hint: {"center_x":.58, "center_y":.17}

                    MDLabel:
                        text: "Leased Properties"
                        adaptive_size: True
                        color: (0, 0, 0, 1)
                        bold: True
                        font_size: "16dp"
                        pos_hint: {"top": .2, "x": .7}


            MDCard:
                size_hint: None, None
                size: "600dp", "290dp"
                md_bg_color: 0.95, 0.95, 0.95, 1
                MDRelativeLayout:
                    MDLabel:
                        text: "Performance for the month Ending 31/04/2025"
                        adaptive_size: True
                        color: (0.0, 0.0, 0.545)
                        bold: True
                        font_size: "14dp"
                        pos_hint: {"top": .98, "right": .53}

                    MDBoxLayout:
                        orientation: "horizontal"
                        spacing: "3dp"
                        pos_hint: {"top": .98, "right": .8}
                        size_hint: None, None
                        height: dp(40)
                        padding: dp(3)
                        MDIconButton:
                            icon: "chart-line"
                            on_release: root.ids.graph_area.set_graph_type("line")
                            

                        MDIconButton:
                            icon: "chart-bar"
                            on_release: root.ids.graph_area.set_graph_type("bar")
                            

                        MDIconButton:
                            icon: "chart-pie"
                            on_release: root.ids.graph_area.set_graph_type("pie")
                            

                        MDIconButton:
                            icon: "chart-donut"
                            on_release: root.ids.graph_area.set_graph_type("donut")
                            

                    
                    GraphArea:
                        size_hint: 1, None
                        height: self.parent.height - dp(50) 
                        pos_hint: {"top": 0.85}

            MDCard:
                size_hint: None, None
                size: "600dp", "290dp"
                md_bg_color: 0.95, 0.95, 0.95, 1
                MDRelativeLayout:
                    MDCard:
                        adaptive_size: True
                        radius: [5, 5, 5, 5]
                        pos_hint: {"top": .95, "right": .35}
                        md_bg_color: [0.9, 0, 0, 0.8]
                        MDBoxLayout:
                            orientation: "horizontal"
                            adaptive_size: True  
                            padding: "5dp"
                            MDLabel:
                                text: "Attention Needed"
                                adaptive_size: True
                                color: (1, 1, 1, 1)
                                bold: True
                                font_size: "24dp"
                    MDCard:
                        size_hint: None, None
                        size: "70dp", "70dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .78, "right": .15}
                        md_bg_color: (0.0, 0.0, 0.545)

                    MDIcon:
                        icon: "home-account"
                        font_size: "40dp"
                        adaptive_size: True
                        pos_hint: {"top": .74, "x": .06}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1 
                    
                    MDLabel:
                        text: "30 Tentants Complaining"
                        adaptive_size: True
                        color: (1, 0, .7, 1)
                        # bold: True
                        font_size: "18dp"
                        pos_hint: {"right": .65, "y": .6}
                
                    MDRaisedButton:
                        text: "Explore Complains"
                        theme_text_color: "Custom"
                        text_color: "white"
                        font_size: "12sp"
                        pos_hint: {"right": .95, "y": .6}
                        size_hint: None, None
                        size: "100dp", "20dp"
                        elevation: 0
                        on_release: app.change_screen('finance')
                    
                    MDCard:
                        size_hint: None, None
                        size: "70dp", "70dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .53, "right": .15}
                        md_bg_color: (0.0, 0.0, 0.545)

                    MDIcon:
                        icon: "account-key"
                        font_size: "40dp"
                        adaptive_size: True
                        pos_hint: {"top": .49, "x": .06}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1 
                    
                    MDLabel:
                        text: "5 LandLords Complaining"
                        adaptive_size: True
                        color: (1, 0, .7, 1)
                        # bold: True
                        font_size: "18dp"
                        pos_hint: {"right": .65, "y": .35}
                
                    MDRaisedButton:
                        text: "Explore Complains"
                        theme_text_color: "Custom"
                        text_color: "white"
                        font_size: "12sp"
                        pos_hint: {"right": .95, "y": .33}
                        size_hint: None, None
                        size: "100dp", "20dp"
                        elevation: 0
                        on_release: app.change_screen('finance')

                    MDCard:
                        size_hint: None, None
                        size: "70dp", "70dp"
                        radius: [50, 50, 50, 50]
                        pos_hint: {"top": .27, "right": .15}
                        md_bg_color: (0.0, 0.0, 0.545)

                    MDIcon:
                        icon: "alert-decagram"
                        font_size: "40dp"
                        adaptive_size: True
                        pos_hint: {"top": .22, "x": .06}
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1 

                    MDLabel:
                        text: "1 system update"
                        adaptive_size: True
                        color: (1, 0, .7, 1)
                        # bold: True
                        font_size: "18dp"
                        pos_hint: {"right": .65, "y": .1}
                
                    MDRaisedButton:
                        text: "See Update"
                        theme_text_color: "Custom"
                        text_color: "white"
                        font_size: "12sp"
                        pos_hint: {"right": .95, "y": .08}
                        size_hint: None, None
                        size: "100dp", "20dp"
                        elevation: 0
                        on_release: app.change_screen('finance')
'''
Builder.load_string(d_kv)

class DashboardScreen(MDScreen):
    def on_kv_post(self, base_widget):
        self.add_vochures_pie_chart()
        self.add_landlords_donut_chart()

    def add_vochures_pie_chart(self):
        # Pie data
        labels = ['Used', 'Unused', 'Expired']
        sizes = [50, 30, 20]
        colors = ['#4CAF50', '#2196F3', '#FF5722']

        # Create the figure
        fig, ax = plt.subplots(figsize=(1.2, 1.2), dpi=100)
        fig.patch.set_facecolor('none')
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        ax.axis('equal')

        # Inject into the layout
        self.ids.vochures_chart_box.add_widget(FigureCanvasKivyAgg(fig))
    
    def add_landlords_donut_chart(self):
        sizes = [60, 25, 15]
        colors = ['#4CAF50', '#FFC107', "#FF1100"]

        fig, ax = plt.subplots(figsize=(2, 2), dpi=100)
        fig.patch.set_facecolor('none')
        wedges, texts, autotexts = ax.pie(
            sizes,
            colors=colors,
            wedgeprops=dict(width=0.4),
            autopct='%1.1f%%',
            startangle=90,
            pctdistance=0.9 
        )

        for autotext in autotexts:
            autotext.set_color("black")
            autotext.set_fontsize(6)
            autotext.set_fontweight("bold")

        ax.set(aspect="equal")

        donut = FigureCanvasKivyAgg(fig)
        self.ids.landlords_donut_box.add_widget(donut)


class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    bar_color = ListProperty([1,0,100/255])
    bar_width = NumericProperty(10)
    value = NumericProperty(80)
    duration = NumericProperty(1.5)
    text = StringProperty("0%")
    counter = 0

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.duration/self.value)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarRe(AnchorLayout):
    set_valuere = NumericProperty(0)
    bar_colorre = ListProperty([0.937, 0.658, 1.0])
    bar_widthre = NumericProperty(3)
    valuere = NumericProperty(90)
    durationre = NumericProperty(1.5)
    textre = StringProperty("0%")
    counterre = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarRe, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationre/self.valuere)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterre < self.valuere:
            self.counterre += 1
            self.textre = f"{self.counterre}%"
            self.set_valuere = self.counterre
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarPp(AnchorLayout):
    set_valuepp = NumericProperty(0)
    bar_colorpp = ListProperty([0, 191/255, 255/255])
    bar_widthpp = NumericProperty(3)
    valuepp = NumericProperty(70)
    durationpp = NumericProperty(1.5)
    textpp = StringProperty("0%")
    counterpp = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarPp, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationpp/self.valuepp)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterpp < self.valuepp:
            self.counterpp += 1
            self.textpp = f"{self.counterpp}%"
            self.set_valuepp = self.counterpp
        else:
            Clock.unschedule(self.percent_counter)

class CircularProgressBarLp(AnchorLayout):
    set_valuelp = NumericProperty(0)
    bar_colorlp = ListProperty([0.0, 0.0, 0.545])
    bar_widthlp = NumericProperty(3)
    valuelp = NumericProperty(86)
    durationlp = NumericProperty(1.5)
    textlp = StringProperty("0%")
    counterlp = 0

    def __init__(self, **kwargs):
        super(CircularProgressBarLp, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationlp/self.valuelp)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.counterlp < self.valuelp:
            self.counterlp += 1
            self.textlp = f"{self.counterlp}%"
            self.set_valuelp = self.counterlp
        else:
            Clock.unschedule(self.percent_counter)

class TntsCircularProgressBar(AnchorLayout):
    set_valuetn = NumericProperty(0)
    bar_colortn = ListProperty([0.0, 0.0, 0.545])
    bar_widthtn = NumericProperty(3)
    valuetn = NumericProperty(86)
    durationtn = NumericProperty(1.5)
    texttn = StringProperty("0%")
    countertn = 0

    def __init__(self, **kwargs):
        super(TntsCircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)
    
    def animate(self, dt):  # Accept dt here
        Clock.schedule_interval(self.percent_counter, self.durationtn/self.valuetn)
    
    def percent_counter(self, dt):  # Accept dt here too
        if self.countertn < self.valuetn:
            self.countertn += 1
            self.texttn = f"{self.countertn}%"
            self.set_valuetn = self.countertn
        else:
            Clock.unschedule(self.percent_counter)

class GraphArea(AnchorLayout):
    graph_type = StringProperty("bar")

    def on_kv_post(self, base_widget):
        self.draw_graph(self.graph_type)

    def draw_graph(self, graph_type):
        self.clear_widgets()
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']

        # Simulated performance data for multiple items
        item_data = {
            'Properties': [100, 70, 45, 8],
            'Rent': [0, 65, 90, 100],
            'tenants': [55, 60, 65, 70],
            '': [55, 60, 65, 70],
        }

        fig, ax = plt.subplots(figsize=(5, 3))
        fig.patch.set_facecolor('none')
        for spine in ax.spines.values():
            spine.set_visible(False)
        ax.grid(False)
        ax.tick_params(left=True, bottom=False, labelleft=True, labelbottom=True)

        if graph_type == "line":
            for label, values in item_data.items():
                ax.plot(weeks, values, marker='o', label=label)
            ax.set_ylabel('Performance (%)')
            ax.set_xlabel('Weeks')
            ax.legend()

        elif graph_type == "bar":
            import numpy as np
            x = np.arange(len(weeks))
            width = 0.15

            for i, (label, values) in enumerate(item_data.items()):
                ax.bar(x + i * width, values, width=width, label=label)

            ax.set_xticks(x + width)
            ax.set_xticklabels(weeks)
            ax.set_ylabel('Performance (%)')
            ax.legend()

        elif graph_type == "pie":
            # Sum each item's total performance
            total_performance = {label: sum(values) for label, values in item_data.items()}
            labels = list(total_performance.keys())
            sizes = list(total_performance.values())
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#FF9999', '#66B3FF', '#99FF99'])

        elif graph_type == "donut":
            total_performance = {label: sum(values) for label, values in item_data.items()}
            labels = list(total_performance.keys())
            sizes = list(total_performance.values())
            wedges, texts, autotexts = ax.pie(sizes, wedgeprops=dict(width=0.5), labels=labels, autopct='%1.1f%%')
            ax.set(aspect="equal")

        fig.tight_layout()
        self.add_widget(FigureCanvasKivyAgg(fig))

    def set_graph_type(self, gtype):
        if gtype != self.graph_type:
            self.graph_type = gtype
            self.draw_graph(gtype)