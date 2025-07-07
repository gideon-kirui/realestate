from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty

from screens.dialogs import MultiStepForm
from kivy.uix.filechooser import FileChooserIconView
from kivymd.uix.label import MDLabel

d_kv = '''
<MultiStepForm>:
    orientation: 'vertical'
    spacing: '2dp'
    size_hint_y: None
    height: "500dp"
    MDRelativeLayout:
        MDLabel:
            text: "Register Tenant/Landlord"
            bold: True
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .98}
            font_style: "H4"
    
        MDLabel:
            id: name
            text: "Basic Info"
            adaptive_size: True
            pos_hint: {"center_x": .08, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: nm
            icon: "numeric-1-circle"
            adaptive_size: True
            pos_hint: {"center_x": .08, "center_y": .8}
            user_font_size: "48sp"
            theme_text_color: "Custom"

        MDProgressBar:
            id: progress
            size_hint_x: .3
            size_hint_y: .013
            pos_hint: {"center_x": .28, "center_y": .8}

        MDLabel:
            id: contact
            text: "Address"
            adaptive_size: True
            pos_hint: {"center_x": 0.49, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: cntct
            icon: "numeric-2-circle"
            pos_hint: {"center_x": .49, "center_y": .8}
            user_font_size: "35sp"
            theme_text_color: "Custom"

        MDProgressBar:
            id: progress1
            size_hint_x: .3
            size_hint_y: .013
            pos_hint: {"center_x": .7, "center_y": .8}

        MDLabel:
            id: submit
            text: "Validation"
            pos_hint: {"center_x": 1.35, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: sb
            icon: "numeric-3-circle"
            pos_hint: {"center_x": .91, "center_y": .8}
            user_font_size: "35sp"
            theme_text_color: "Custom"

        Carousel:
            id: slide
            height: "400dp"
            MDFloatLayout:
                MDTextField:
                    hint_text: "Full Name"
                    icon_left: "account"
                    mode: "rectangle"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .71}
                MDTextField:
                    hint_text: "ID Number"
                    mode: "rectangle"
                    icon_left: "card-account-details-outline"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .58}
                MDTextField:
                    hint_text: "Phone Number"
                    mode: "rectangle"
                    icon_left: "phone-outline"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                MDTextField:
                    hint_text: "Email Address"
                    mode: "rectangle"
                    icon_left: "email"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .32}
                MDBoxLayout:
                    id: radio_box
                    orientation: "horizontal"
                    spacing: "10dp"
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .2}

                    BoxLayout:
                        size_hint_x: None
                        width: "200dp"
                        spacing: "8dp"
                        MDCheckbox:
                            group: "feat"
                            on_active: if self.active: root.selected_feature = "Tenant"
                        MDLabel:
                            text: "Tenant"
                            valign: "middle"

                    BoxLayout:
                        size_hint_x: None
                        width: "200dp"
                        spacing: "8dp"
                        MDCheckbox:
                            group: "feat"
                            on_active: if self.active: root.selected_feature = "Landlord"
                        MDLabel:
                            text: "Landlord"
                            valign: "middle"

                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .5
                    pos_hint: {"center_x": .5, "center_y": .1}
                    on_release: app.next()
                    elevation: 0

            MDFloatLayout:
                MDTextField:
                    hint_text: "County"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .65}
                MDTextField:
                    hint_text: "Consituency"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .51}
                MDTextField:
                    hint_text: "Ward"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .37}
                MDTextField:
                    hint_text: "Location"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .23}


                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .1}
                    on_release: app.previous()
                    elevation: 0
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .1}
                    on_release: app.next1()
                    elevation: 0

            MDFloatLayout:
                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .7, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            text: "Upload Agreement form"
                            size_hint_x: .4
                            on_release: app.open_file_chooser()
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0

                        MDIcon:
                            icon: "handshake"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .95, "center_y": .5}
                        
                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .575, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            id: dropdown_button
                            text: "Upload Id Card"
                            size_hint_x: .4
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0
                            
                        MDIcon:
                            icon: "card-account-details-outline"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .95, "center_y": .5}


                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .45, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            text: "Upload passport photo"
                            on_release: app.open_file_chooser()
                            size_hint_x: .4
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0

                        MDIcon:
                            icon: "image"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .95, "center_y": .5}
                    
                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .32, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "Update property"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 1)

                        MDRaisedButton:
                            id: dropdown_button
                            text: "Assign Property"
                            size_hint_x: .4
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0
                            
                        MDIcon:
                            icon: "home"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .95, "center_y": .5}
                
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .1}
                    on_release: app.previous1()
                    elevation: 0

                MDRaisedButton:
                    text: "Submit"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .1}
                    elevation: 0

<MultiStepAddpForm>:
    orientation: 'vertical'
    spacing: '2dp'
    size_hint_y: None
    height: "500dp"
    MDRelativeLayout:
        MDLabel:
            text: "Register Property"
            bold: True
            adaptive_size: True
            pos_hint: {"center_x": .5, "center_y": .98}
            font_style: "H4"
    
        MDLabel:
            id: name
            text: "Identification"
            adaptive_size: True
            pos_hint: {"center_x": .08, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: nm
            icon: "numeric-1-circle"
            adaptive_size: True
            pos_hint: {"center_x": .08, "center_y": .8}
            user_font_size: "48sp"
            theme_text_color: "Custom"

        MDProgressBar:
            id: progress
            size_hint_x: .3
            size_hint_y: .013
            pos_hint: {"center_x": .28, "center_y": .8}

        MDLabel:
            id: contact
            text: "Description"
            adaptive_size: True
            pos_hint: {"center_x": 0.49, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: cntct
            icon: "numeric-2-circle"
            pos_hint: {"center_x": .49, "center_y": .8}
            user_font_size: "35sp"
            theme_text_color: "Custom"

        MDProgressBar:
            id: progress1
            size_hint_x: .3
            size_hint_y: .013
            pos_hint: {"center_x": .7, "center_y": .8}

        MDLabel:
            id: submit
            text: "Validation"
            pos_hint: {"center_x": 1.35, "center_y": .88}
            font_style: "H6"
            theme_text_color: "Custom"

        MDIconButton:
            id: sb
            icon: "numeric-3-circle"
            pos_hint: {"center_x": .91, "center_y": .8}
            user_font_size: "35sp"
            theme_text_color: "Custom"

        Carousel:
            id: slide
            height: "400dp"
            MDFloatLayout:
                MDRaisedButton:
                    text: "Add property owner"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .7}
                    elevation: 0
                MDTextField:
                    hint_text: "Price"
                    mode: "rectangle"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .58}
                MDTextField:
                    hint_text: "location"
                    mode: "rectangle"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .45}
                MDBoxLayout:
                    id: radio_box
                    orientation: "horizontal"
                    spacing: "10dp"
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .32}

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Tenant"
                        MDLabel:
                            text: "Land"
                            valign: "middle"
                            font_size: "12sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "Appartment"
                            valign: "middle"
                            font_size: "12sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "170dp"
                        spacing: "3dp"
                        md_bg_color: "darkgrey"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "House"
                            valign: "middle"
                            font_size: "12sp"
                            
                MDBoxLayout:
                    id: radio_box
                    orientation: "horizontal"
                    spacing: "10dp"
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .2}

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Tenant"
                        MDLabel:
                            text: "For Sale"
                            valign: "middle"
                            font_size: "12sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "For Lease"
                            valign: "middle"
                            font_size: "12sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "170dp"
                        spacing: "3dp"
                        md_bg_color: "darkgrey"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "For Rent"
                            valign: "middle"
                            font_size: "12sp"

                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .5
                    pos_hint: {"center_x": .5, "center_y": .1}
                    on_release: app.next()
                    elevation: 0

            MDFloatLayout:
                MDCard:
                    orientation: "vertical"
                    size_hint_x: None
                    width: "500dp" 
                    size_hint_y: None
                    height: "280dp"
                    pos_hint: {"center_x": .5, "center_y": .45}
                    md_bg_color: (0, 0, 0, 0.08)
                    radius: [10, 10, 0, 0]
                    padding: "10dp"
                    spacing: "10dp"

                    MDTextField:
                        hint_text: "Describe property"
                        multiline: True
                        size_hint_x: 1
                        size_hint_y: None
                        max_height: "270dp"
                        height: "200dp"
                        active_line: False
                        line_color_normal: (0, 0, 0, 0.001)
                        hint_text_color_focus: (0, 0, 0, 0.001)

                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .1}
                    on_release: app.previous()
                    elevation: 0
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .1}
                    on_release: app.next1()
                    elevation: 0

            MDFloatLayout:
                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .7, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            text: "Upload property photo"
                            size_hint_x: .45
                            on_release: app.open_file_chooser()
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0

                        MDIcon:
                            icon: "image"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .97, "center_y": .5}
                        
                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .575, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            id: dropdown_button
                            text: "Upload terms and conditions"
                            size_hint_x: .45
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0
                            
                        MDIcon:
                            icon: "file-document"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .97, "center_y": .5}


                MDCard:
                    size_hint: None, None
                    size: "500dp", "40dp"
                    radius: [5, 5, 5, 5]
                    padding: "5dp"
                    spacing: "5dp"
                    pos_hint: {"top": .45, "right": .9}
                    md_bg_color: (0, 0, 0, 0.1)
                    MDRelativeLayout:
                        MDLabel:
                            text: "No file uploaded yet"
                            pos_hint: {"center_x": .6, "center_y": .5}
                            color: (0, 0, 0, 0.35)

                        MDRaisedButton:
                            text: "Upload business permit"
                            on_release: app.open_file_chooser()
                            size_hint_x: .45
                            pos_hint: {"center_x": .7, "center_y": .5}
                            elevation: 0

                        MDIcon:
                            icon: "file-certificate"
                            size_hint_x: None
                            width: "24dp"
                            pos_hint: {"center_x": .97, "center_y": .5}

                MDBoxLayout:
                    id: radio_box
                    orientation: "horizontal"
                    spacing: "10dp"
                    adaptive_size: True
                    pos_hint: {"center_x": .5, "center_y": .3}

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Tenant"
                        MDLabel:
                            text: "Vaccant"
                            valign: "middle"
                            font_size: "14sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "150dp"
                        spacing: "3dp"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "Occupied"
                            valign: "middle"
                            font_size: "14sp"

                    BoxLayout:
                        size_hint_x: None
                        width: "170dp"
                        spacing: "3dp"
                        md_bg_color: "darkgrey"
                        MDCheckbox:
                            group: "features"
                            on_active: if self.active: app.form.selected_feature = "Landlord"
                        MDLabel:
                            text: "On Renovation"
                            valign: "middle"
                            font_size: "12sp"
                    
                MDRaisedButton:
                    text: "Add Care Taker"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .2}
                    elevation: 0
                
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .1}
                    on_release: app.previous1()
                    elevation: 0

                MDRaisedButton:
                    text: "Submit"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .1}
                    elevation: 0




'''
Builder.load_string(d_kv)

class MultiStepForm(MDBoxLayout):
    selected_feature = StringProperty() 

class MultiStepAddpForm(MDBoxLayout):
    selected_feature = StringProperty()

    def open_registration_form(self):
            if hasattr(self, 'dialog') and self.dialog:
                self.dialog.open()
                return

            self.form = MultiStepForm()
            self.dialog = MDDialog(
                type="custom",
                content_cls=self.form,
                size_hint=(0.5, 0.5),
                auto_dismiss=False
            )
            self.dialog.open()

    def next(self):
        self.form.ids.slide.load_next(mode="next")
        self.form.ids.name.text_color = self.theme_cls.primary_color
        self.form.ids.progress.value = 100
        self.form.ids.nm.text_color = self.theme_cls.primary_color
        self.form.ids.nm.icon = "check-decagram"

    def next1(self):
        self.form.ids.slide.load_next(mode="next")
        self.form.ids.contact.text_color = self.theme_cls.primary_color
        self.form.ids.progress1.value = 100
        self.form.ids.cntct.text_color = self.theme_cls.primary_color
        self.form.ids.cntct.icon = "check-decagram"

    def previous(self):
        self.form.ids.slide.load_previous()
        self.form.ids.name.text_color = 0, 0, 0, 1
        self.form.ids.nm.text_color = 0, 0, 0, 1
        self.form.ids.progress.value = .001
        self.form.ids.nm.icon = "numeric-1-circle"

    def previous1(self):
        self.form.ids.slide.load_previous()
        self.form.ids.contact.text_color = 0, 0, 0, 1
        self.form.ids.cntct.text_color = 0, 0, 0, 1
        self.form.ids.progress1.value = .001
        self.form.ids.cntct.icon = "numeric-2-circle"
        
    def open_file_chooser(self):
        if hasattr(self, 'file_dialog') and self.file_dialog:
            self.file_dialog.open()
            return

        file_box = MDBoxLayout(orientation='vertical', spacing="12dp", padding="12dp")
        filechooser = FileChooserIconView(size_hint_y=0.85)
        file_box.add_widget(filechooser)

        # Label to show selected file
        self.file_label = MDLabel(text="No file selected", halign="center", size_hint_y=0.15)
        file_box.add_widget(self.file_label)

        def on_select_file(instance, *args):
            selected = filechooser.selection
            if selected:
                self.file_label.text = f"Selected: {selected[0]}"

        filechooser.bind(on_selection=on_select_file)

        self.file_dialog = MDDialog(
            title="Choose File",
            type="custom",
            content_cls=file_box,
            buttons=[
                MDFlatButton(text="CANCEL", on_release=lambda x: self.file_dialog.dismiss()),
                MDFlatButton(text="OK", on_release=lambda x: self.file_dialog.dismiss())
            ],
            size_hint=(0.9, 0.9)
        )
        self.file_dialog.open()
    
    def open_addproperty_form(self):
        if hasattr(self, 'dialog') and self.dialog:
            self.dialog.open()
            return

        self.form = MultiStepAddpForm()
        self.dialog = MDDialog(
            type="custom",
            content_cls=self.form,
            size_hint=(0.5, 0.5),
            auto_dismiss=False
        )
        self.dialog.open()