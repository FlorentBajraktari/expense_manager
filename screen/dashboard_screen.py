from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from functools import partial


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)

        # Layout kryesor për butonat në të majtë dhe përmbajtjen në të djathtë
        main_layout = MDBoxLayout(orientation='horizontal')

        # Menu layout në anën e majtë për butonat
        menu_layout = MDBoxLayout(orientation='vertical', padding=(
            10, 10), spacing=10, size_hint=(0.2, 1))

        # Definimi i butonave
        buttons = [
            ("Shiko Faturat e Paguara", "paid_bills"),
            ("Shiko Faturat e Papaguara", "unpaid_bills"),
            ("Shto Faturë të Re", "add_bill"),
            ("Cakto Kursime Automatike", "auto_savings"),
            ("Menaxho Borxhet", "debts"),
            ("Planifiko Shlyerjet", "debt_planning"),
            ("Buxheti", "budget"),
            ("Gjenero Raporte", "reports")
        ]

        for text, screen_name in buttons:
            button = MDRaisedButton(
                text=text,
                size_hint=(1, None),
                height=50,
                on_release=partial(self.switch_screen, screen_name)
            )
            menu_layout.add_widget(button)

        # Shto butonin për sign-out
        sign_out_button = MDRaisedButton(
            text="Sign-Out",
            size_hint=(1, None),
            height=50,
            on_release=self.sign_out
        )
        menu_layout.add_widget(sign_out_button)

        # Pjesa e djathtë për shfaqjen e përmbajtjes (tabelat, statistikat, etj.)
        self.content_area = MDBoxLayout(orientation='vertical', padding=(
            10, 10), spacing=10, size_hint=(0.8, 1))

        # Shto menu dhe përmbajtje në layout kryesor
        main_layout.add_widget(menu_layout)
        main_layout.add_widget(self.content_area)

        self.add_widget(main_layout)

    def switch_screen(self, screen_name, *args):
        self.manager.current = screen_name

    def sign_out(self, *args):
        self.manager.current = "login"
