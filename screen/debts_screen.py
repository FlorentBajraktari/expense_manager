from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from models.debts import add_debt, get_debts, make_debt_payment


class DebtsScreen(Screen):  # Sigurohu që të trashëgojë nga Screen
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Krijo një layout të brendshëm
        layout = MDBoxLayout(orientation='vertical')

        self.debtor_input = MDTextField(
            hint_text="Debitori", size_hint_x=None, width=300)
        self.amount_input = MDTextField(
            hint_text="Shuma", size_hint_x=None, width=300)
        self.interest_input = MDTextField(
            hint_text="Norma e Interesit", size_hint_x=None, width=300)
        self.due_date_input = MDTextField(
            hint_text="Data e Afatit (yyyy-mm-dd)", size_hint_x=None, width=300)
        self.add_button = MDRaisedButton(
            text="Shto Borxh", on_release=self.add_debt)

        layout.add_widget(MDLabel(text="Menaxhimi i Borxheve",
                          font_style="H4", halign="center"))
        layout.add_widget(self.debtor_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.interest_input)
        layout.add_widget(self.due_date_input)
        layout.add_widget(self.add_button)

        self.add_widget(layout)

    def add_debt(self, instance):
        debtor = self.debtor_input.text
        amount = float(self.amount_input.text)
        interest_rate = float(self.interest_input.text)
        due_date = self.due_date_input.text
        add_debt(debtor, amount, interest_rate, due_date)
        self.show_debts()

    def show_debts(self):
        debts = get_debts()
        for debt in debts:
            debtor, amount, interest_rate, due_date = debt[1], debt[2], debt[3], debt[4]
            self.add_widget(MDLabel(
                text=f"{debtor}: ${amount}, Interest: {interest_rate}%, Due: {due_date}", halign="left"))
