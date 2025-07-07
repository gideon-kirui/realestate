from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast


class AdminLoginPage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20, pos_hint={"center_y": 0.5}, size_hint_y=None, height=300)

        self.username_field = MDTextField(
            hint_text="Admin Username",
            mode="rectangle"
        )
        self.password_field = MDTextField(
            hint_text="Password",
            password=True,
            mode="rectangle"
        )
        login_button = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5},
            on_release=self.validate_admin
        )

        layout.add_widget(self.username_field)
        layout.add_widget(self.password_field)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def validate_admin(self, instance):
        username = self.username_field.text
        password = self.password_field.text

        if username == "admin" and password == "1234":  
            self.manager.current = "dashboard"
        else:
            toast("Invalid admin credentials")
