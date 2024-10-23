from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from models.bills import add_bill  # Përditësuar emrin e funksionit


class AddBillScreen(Screen):
    def __init__(self, **kwargs):
        super(AddBillScreen, self).__init__(**kwargs)
        self.build_layout()

    def build_layout(self):
        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        # Fushat e inputit për emrin, shumën, datën e afatit dhe statusin
        self.name_input = MDTextField(hint_text="Emri i Faturës")
        self.amount_input = MDTextField(hint_text="Shuma", input_filter='int')
        self.due_date_input = MDTextField(
            hint_text="Data e Afatit (yyyy-mm-dd)")
        self.status_input = MDTextField(hint_text="Statusi (paid/unpaid)")

        # Butoni për të shtuar faturën e re
        add_button = MDRaisedButton(
            text="Shto Faturë", on_release=self.add_bill)

        # Butoni për kthim mbrapa
        back_button = MDRaisedButton(text="Back", on_release=self.go_back)

        # Shto të gjitha komponentët në layout
        layout.add_widget(self.name_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.due_date_input)
        layout.add_widget(self.status_input)
        layout.add_widget(add_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_bill(self, *args):
        name = self.name_input.text
        amount = self.amount_input.text
        due_date = self.due_date_input.text
        status = self.status_input.text

        # Përdor `add_bill` për të shtuar faturën e re në bazën e të dhënave
        add_bill(name, amount, due_date, status)

        # Pasi të shtohet fatura, kthehu në dashboard
        self.manager.current = "dashboard"

    def go_back(self, *args):
        self.manager.current = "dashboard"
