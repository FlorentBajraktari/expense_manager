from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from functools import partial


class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        self.buttons = []  # Store buttons for easier management

        main_layout = MDBoxLayout(orientation='horizontal')
        menu_layout = MDBoxLayout(orientation='vertical', padding=(
            10, 10), spacing=10, size_hint=(0.2, 1))

        # Define buttons and screens
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
                md_bg_color=[0.1, 0.4, 0.5, 1],  # Default color
                on_release=partial(self.switch_screen, screen_name)
            )
            self.buttons.append((button, screen_name))
            menu_layout.add_widget(button)

        # Add sign-out button
        sign_out_button = MDRaisedButton(
            text="Sign-Out",
            size_hint=(1, None),
            height=50,
            md_bg_color=[0.1, 0.4, 0.5, 1],
            on_release=self.sign_out
        )
        menu_layout.add_widget(sign_out_button)

        # Right content area
        self.content_area = MDBoxLayout(orientation='vertical', padding=(
            10, 10), spacing=10, size_hint=(0.8, 1))
        main_layout.add_widget(menu_layout)
        main_layout.add_widget(self.content_area)
        self.add_widget(main_layout)

    def switch_screen(self, screen_name, *args):
        self.reset_button_styles()  # Reset styles before highlighting
        button = self.get_button_by_screen_name(screen_name)
        if button:
            button.md_bg_color = [0.2, 0.6, 0.8, 1]  # Example highlight color
        self.manager.current = screen_name

    def reset_button_styles(self):
        for btn, _ in self.buttons:
            btn.md_bg_color = [0.1, 0.4, 0.5, 1]  # Reset to default

    def get_button_by_screen_name(self, screen_name):
        return next((btn for btn, scr in self.buttons if scr == screen_name), None)

    def sign_out(self, *args):
        self.manager.current = "login"

    def show_paid_bills(self):
        print("Shfaq faturat e paguara")
        self.content_area.clear_widgets()

    def show_unpaid_bills(self):
        print("Shfaq faturat e papaguara")
        self.content_area.clear_widgets()

    def add_new_bill(self):
        print("Shto faturë të re")
        self.content_area.clear_widgets()
