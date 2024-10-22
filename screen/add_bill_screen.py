from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from models.bills import add_new_bill


class AddBillScreen(Screen):
    def __init__(self, **kwargs):
        super(AddBillScreen, self).__init__(**kwargs)

        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        self.name_input = MDTextField(
            hint_text="Emri i Faturës", size_hint_x=None, width=300)
        self.amount_input = MDTextField(
            hint_text="Shuma", size_hint_x=None, width=300)
        self.due_date_input = MDTextField(
            hint_text="Data e Afatit (yyyy-mm-dd)", size_hint_x=None, width=300)
        self.add_button = MDRaisedButton(
            text="Shto Faturë", on_release=self.add_bill)

        layout.add_widget(self.name_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.due_date_input)
        layout.add_widget(self.add_button)

        self.add_widget(layout)

    def add_bill(self, instance):
        name = self.name_input.text
        amount = float(self.amount_input.text)
        due_date = self.due_date_input.text
        add_new_bill(name, amount, due_date, "unpaid", 0)
        print("Faturë e re u shtua.")
