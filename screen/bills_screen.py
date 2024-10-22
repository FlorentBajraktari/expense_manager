from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


class BillsScreen(Screen):
    def __init__(self, **kwargs):
        super(BillsScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        layout.add_widget(MDRaisedButton(
            text="Shiko Faturat e Paguara", on_release=self.show_paid_bills))
        layout.add_widget(MDRaisedButton(
            text="Shiko Faturat e Papaguara", on_release=self.show_unpaid_bills))
        layout.add_widget(MDRaisedButton(
            text="Shto Faturë të Re", on_release=self.add_new_bill))

        self.add_widget(layout)

    def show_paid_bills(self, instance):
        # Import brenda funksionit për të shmangur rrethin
        from models.bills import get_paid_bills
        bills = get_paid_bills()
        for bill in bills:
            print(f"Paguara: {bill}")

    def show_unpaid_bills(self, instance):
        # Import brenda funksionit për të shmangur rrethin
        from models.bills import get_unpaid_bills
        bills = get_unpaid_bills()
        for bill in bills:
            print(f"E Papaguar: {bill}")

    def add_new_bill(self, instance):
        # Import brenda funksionit për të shmangur rrethin
        from models.bills import add_bill
        add_bill("Fatura e re", 150.0, "2024-11-10", "unpaid", 0)
        print("Faturë e re u shtua.")
