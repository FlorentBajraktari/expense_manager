from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from models.debts import get_debts, plan_debt_payment, add_debt, update_debt, delete_debt


class DebtPlanningScreen(Screen):
    def __init__(self, **kwargs):
        super(DebtPlanningScreen, self).__init__(**kwargs)
        self.build_layout()

    def build_layout(self):
        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        back_button = MDRaisedButton(
            text="Back",
            size_hint=(1, None),
            height=50,
            on_release=self.go_back
        )

        buttons_layout = MDBoxLayout(
            orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        plan_button = MDRaisedButton(
            text="Plan Payment", on_release=self.plan_payment)
        add_button = MDRaisedButton(text="Add", on_release=self.add_debt)
        update_button = MDRaisedButton(
            text="Update", on_release=self.update_debt)
        delete_button = MDRaisedButton(
            text="Delete", on_release=self.delete_debt)

        buttons_layout.add_widget(plan_button)
        buttons_layout.add_widget(add_button)
        buttons_layout.add_widget(update_button)
        buttons_layout.add_widget(delete_button)

        debts = get_debts()
        self.data_tables = MDDataTable(
            size_hint=(1, 0.7),
            column_data=[
                ("ID", dp(30)),
                ("Borxhi", dp(60)),
                ("Shuma Totale", dp(30)),
                ("Shuma e Mbetur", dp(60))
            ],
            row_data=[
                (str(debt[0]), debt[1], f"${debt[2]:.2f}", f"${debt[3]:.2f}")
                for debt in debts
            ]
        )

        layout.add_widget(back_button)
        layout.add_widget(buttons_layout)
        layout.add_widget(self.data_tables)
        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "dashboard"

    def plan_payment(self, *args):
        pass

    def add_debt(self, *args):
        pass

    def update_debt(self, *args):
        pass

    def delete_debt(self, *args):
        pass
