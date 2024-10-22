from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from functools import partial


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical', padding=(
            10, 10), spacing=10, size_hint=(None, 1), width=250)

        buttons = [
            ("Shiko Faturat e Paguara", "paid_bills"),
            ("Shiko Faturat e Papaguara", "unpaid_bills"),
            ("Shto Faturë të Re", "add_bill"),
            ("Cakto Kursime Automatike", "auto_savings"),
            ("Menaxho Borxhet", "debts"),
            ("Planifiko Shlyerjet", "debt_planning"),
            ("Gjenero Raporte", "reports")
        ]

        for text, screen_name in buttons:
            button = MDRaisedButton(
                text=text,
                size_hint=(1, None),
                height=50,
                on_release=partial(self.switch_screen, screen_name),
                pos_hint={"left": 1}
            )
            layout.add_widget(button)

        # Shto butonin për Sign-Out
        sign_out_button = MDRaisedButton(
            text="Sign-Out",
            size_hint=(1, None),
            height=50,
            on_release=self.sign_out,
            pos_hint={"left": 1}
        )
        layout.add_widget(sign_out_button)

        self.add_widget(layout)

    def switch_screen(self, screen_name, *args):
        self.manager.current = screen_name

    def sign_out(self, instance):
        self.manager.current = "login"
