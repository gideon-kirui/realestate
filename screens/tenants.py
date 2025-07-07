from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.card import MDCard

d_kv = '''

<TenantsScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        MDRelativeLayout:
            MDGridLayout:
                cols: 2
                adaptive_height: True
                adaptive_width: True
                pos_hint: {"center_x": 0.5, "center_y": .5}
                MDCard:
                    size_hint: None, None
                    size: "460dp", "590dp"
                    MDRelativeLayout:
                        MDTextField:
                            pos_hint: {"center_x": 0.5, "center_y": .95}
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
                            adaptive_size: True
                            spacing: "8dp"
                            pos_hint: {"center_x": 0.5, "center_y": .87}
                            MDFillRoundFlatButton:
                                text: "All"
                                text_color: "blue"
                                md_bg_color: (.8,.8,.8,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                elevation: 0
                                bold: True

                            MDFillRoundFlatButton:
                                text: "Active"
                                md_bg_color: (.8,.8,.8,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                elevation: 0

                            MDFillRoundFlatButton:
                                text: "Suspended"
                                md_bg_color: (.8,.8,.8,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                elevation: 0

                            MDFillRoundFlatButton:
                                text: "Inactive"
                                md_bg_color: (.8,.8,.8,1)
                                pos_hint: {"center_x": .7, "center_y": .1}
                                elevation: 0

                        BoxLayout:
                            orientation: "vertical"
                            pos_hint: {"center_x": 0.5, "center_y": .3}
                            padding: "20dp"
                            MDScrollView:
                                MDList:
                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True
                                        
                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"

                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"

                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"

                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"

                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"

                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True

                                    TwoLineAvatarListItem:
                                        text: "Okinyi Owino"
                                        secondary_text: "01RSGGFS1"

                                        ImageLeftWidget:
                                            source: "asset/images/profiles/nophoto.png"
                                        
                                        ContainerRight:
                                            MDCard:
                                                adaptive_size: True
                                                md_bg_color: 0, 1, 0, .5
                                                radius: [10,10, 10,10]
                                                MDLabel:
                                                    text: "Active"
                                                    halign: "center"
                                                    adaptive_size: True
                                                    padding: "20dp", "5dp"
                                                    bold: True
                            
                MDCard:
                    size_hint: None, None
                    size: "850dp", "590dp"
                    md_bg_color: 1, 1, 1, 1
                    orientation: 'vertical'
                    MDRelativeLayout:
                        MDGridLayout:
                            cols: 2
                            adaptive_height: True
                            adaptive_width: True 
                            spacing: "8dp"
                            pos_hint: {"center_x": 0.487}
                            MDCard:
                                size_hint: None, None
                                size: "400dp", "590dp"
                                md_bg_color: 0.95, 0.95, 0.95, 1
                                MDRelativeLayout:
                                    MDLabel:
                                        text: "Property Details"
                                        font_size: "24dp"
                                        adaptive_size: True
                                        padding: "20dp", "5dp"
                                        pos_hint: {"center_x": 0.3, "center_y": .96}
                                        bold: True

                                    MDSeparator:
                                        height: "1dp"
                                        color: 0, 1, 0, 1
                                        pos_hint: {"center_x": 0.5, "center_y": .92}

                                    MDGridLayout:
                                        cols: 2
                                        adaptive_height: True
                                        adaptive_width: True
                                        spacing: "20dp"
                                        pos_hint: {"center_x": .5, "center_y": .55}
                                        MDLabel:
                                            text: "Owner"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "Caroline Ochieng"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Category"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "Rental"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        
                                        MDLabel:
                                            text: "Type"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Bed Seater"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Rent Payable"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "12000"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        
                                        MDLabel:
                                            text: "Number"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "P0001434BC"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Condition"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Mantainance Required"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        MDLabel:
                                            text: "Location"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Along Ngong road"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        
                                    MDRaisedButton:
                                        text: "Download Agreement Form"
                                        font_size: "16sp"
                                        pos_hint: {"center_x": .33, "center_y": .16}
                                        elevation: 0 

                                    MDRaisedButton:
                                        text: "Download T&Cs Form"
                                        font_size: "16sp"
                                        pos_hint: {"center_x": .28, "center_y": .07}
                                        elevation: 0


                            MDCard:
                                size_hint: None, None
                                size: "400dp", "590dp"
                                md_bg_color: 0.95, 0.95, 0.95, 1
                                MDRelativeLayout:
                                    MDLabel:
                                        text: "Payment Details"
                                        font_size: "24dp"
                                        adaptive_size: True
                                        padding: "20dp", "5dp"
                                        pos_hint: {"center_x": 0.3, "center_y": .96}
                                        bold: True

                                    MDSeparator:
                                        height: "1dp"
                                        color: 0, 1, 0, 1
                                        pos_hint: {"center_x": 0.5, "center_y": .92}

                                    MDGridLayout:
                                        cols: 2
                                        adaptive_height: True
                                        adaptive_width: True
                                        spacing: "10dp"
                                        pos_hint: {"center_x": .5, "center_y": .55}
                                        MDLabel:
                                            text: "Rent amount"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "8,000"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Water Bill"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "500"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        
                                        MDLabel:
                                            text: "Power Bill"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "500"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Defaults"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                            
                                        MDLabel:
                                            text: "7000(3)"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True
                                        
                                        MDLabel:
                                            text: "Penalties"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "2000"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Other Charges"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "20000"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDSeparator:
                                            height: "2dp"
                                            color: 1, 0, 0, 1
                                        
                                        MDSeparator:
                                            height: "2dp"
                                            color: 1, 0, 0, 1

                                        MDLabel:
                                            text: "Location"
                                            font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDLabel:
                                            text: "Along Ngong road"
                                            # font_size: "24dp"
                                            adaptive_size: True
                                            padding: "20dp", "5dp"
                                            bold: True

                                        MDSeparator:
                                            height: "2dp"
                                            color: 1, 0, 0, 1
                                        
                                        MDSeparator:
                                            height: "2dp"
                                            color: 1, 0, 0, 1
                                        
                                    MDRaisedButton:
                                        text: "Download Satement"
                                        font_size: "16sp"
                                        pos_hint: {"center_x": .25, "center_y": .185}
                                        elevation: 0
                                    
                                    MDRaisedButton:
                                        text: "Send Invocise"
                                        font_size: "16sp"
                                        pos_hint: {"center_x": .8, "center_y": .185}
                                        elevation: 0

                                    MDRaisedButton:
                                        text: "Update Tenant's profile"
                                        font_size: "16sp"
                                        pos_hint: {"center_x": .28, "center_y": .07}
                                        elevation: 0
                                        on_release: app.change_screen('tenantprofile')

                                    MDIconButton:
                                        icon: "plus"
                                        adaptive_size: True
                                        icon_size: "40dp"
                                        md_bg_color: 0, 0.95, 0, 1
                                        pos_hint: {"center_x": .8, "center_y": .08}
                                        rounded_button: True
                                        elevation: 0
                        
<ContainerRight>:
    adaptive_height: True
    adaptive_width: True
    pos_hint: {"center_x": 0.88, "center_y": 0.5}

'''
Builder.load_string(d_kv)

class ContainerRight(MDCard):
    pass

class TenantsScreen(MDScreen):
    pass    
