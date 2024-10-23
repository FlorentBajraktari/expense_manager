from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from models.database import verify_user_credentials


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', spacing=10, padding=20)

        # Fusha për emrin e përdoruesit dhe fjalëkalimin
        self.username_input = MDTextField(
            hint_text="Username", size_hint=(0.8, None), height="40dp"
        )
        self.password_input = MDTextField(
            hint_text="Password", size_hint=(0.8, None), height="40dp", password=True
        )

        # Butoni për login
        login_button = MDRaisedButton(
            text="Login", size_hint=(0.5, None), height="40dp"
        )
        login_button.bind(on_release=self.authenticate_user)

        # Shto elementët në layout
        layout.add_widget(
            MDLabel(text="Welcome! Please Login", halign='center'))
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def authenticate_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        if verify_user_credentials(username, password):
            self.manager.current = 'dashboard'
        else:
            print("Invalid login credentials!")
