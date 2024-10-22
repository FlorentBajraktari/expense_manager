from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from models.database import validate_user


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        self.username_input = MDTextField(
            hint_text="Username", size_hint_x=None, width=300)
        self.password_input = MDTextField(
            hint_text="Password", size_hint_x=None, width=300, password=True)
        self.login_button = MDRaisedButton(text="Login", on_release=self.login)

        self.message_label = MDLabel(text="", halign="center")

        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.login_button)
        layout.add_widget(self.message_label)

        self.add_widget(layout)

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if validate_user(username, password):
            self.manager.current = "dashboard"
        else:
            self.message_label.text = "Username or Password is incorrect"
