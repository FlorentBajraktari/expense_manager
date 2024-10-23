from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from models.bills import get_paid_bills, add_bill, update_bill, delete_bill


class PaidBillsScreen(Screen):
    def __init__(self, **kwargs):
        super(PaidBillsScreen, self).__init__(**kwargs)
        self.build_layout()

    def build_layout(self):
        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        # Statistika (Totali i faturave të paguara)
        total = sum(bill[2] for bill in get_paid_bills())
        stats_label = MDRaisedButton(
            text=f"Totali i Faturave të Paguara: ${total:.2f}", size_hint=(1, None), height=50)

        # Butoni për kthim mbrapa
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(1, None),
            height=50,
            on_release=self.go_back
        )

        # Butonat për Add, Update dhe Delete
        buttons_layout = MDBoxLayout(
            orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        add_button = MDRaisedButton(text="Add", on_release=self.add_bill)
        update_button = MDRaisedButton(
            text="Update", on_release=self.update_bill)
        delete_button = MDRaisedButton(
            text="Delete", on_release=self.delete_bill)

        buttons_layout.add_widget(add_button)
        buttons_layout.add_widget(update_button)
        buttons_layout.add_widget(delete_button)

        # Tabela e të dhënave për faturat e paguara
        bills = get_paid_bills()
        self.data_tables = MDDataTable(
            size_hint=(1, 0.7),
            column_data=[
                ("ID", dp(30)),
                ("Emri i Faturës", dp(60)),
                ("Shuma", dp(30)),
                ("Data e Afatit", dp(60)),
                ("Statusi", dp(30))
            ],
            row_data=[
                (str(bill[0]), bill[1], f"${bill[2]:.2f}", bill[3], bill[4])
                for bill in bills
            ]
        )

        layout.add_widget(stats_label)
        layout.add_widget(back_button)
        layout.add_widget(buttons_layout)
        layout.add_widget(self.data_tables)
        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "dashboard"

    def add_bill(self, *args):
        # Implementimi për të shtuar një faturë të re
        pass

    def update_bill(self, *args):
        # Implementimi për të përditësuar faturën e zgjedhur
        pass

    def delete_bill(self, *args):
        # Implementimi për të fshirë faturën e zgjedhur
        pass
