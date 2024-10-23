from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.toast import toast
from datetime import datetime


class DebtPlanningScreen(Screen):  # Riemërimi i klasës për të përputhur importin
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Krijo një layout të brendshëm
        layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

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

        # Shto butonin "Back" për t'u kthyer në ekranin e mëparshëm
        back_button = MDRaisedButton(
            text="Back", on_release=self.go_back_to_dashboard)

        # Shto të gjitha elementët në layout
        layout.add_widget(MDLabel(text="Planifikimi i Shlyerjeve",
                          font_style="H4", halign="center"))
        layout.add_widget(self.debtor_input)
        layout.add_widget(self.amount_input)
        layout.add_widget(self.interest_input)
        layout.add_widget(self.due_date_input)
        layout.add_widget(self.add_button)
        layout.add_widget(back_button)  # Shto butonin "Back"

        self.add_widget(layout)

    def add_debt(self, *args):
        debtor = self.debtor_input.text.strip()
        amount = self.amount_input.text.strip()
        interest = self.interest_input.text.strip()
        due_date = self.due_date_input.text.strip()

        # Kontrollo që të gjitha fushat janë plotësuar
        if not self.validate_inputs(debtor, amount, interest, due_date):
            return

        # Për momentin, thjesht printo borxhin e ri dhe pastaj pastro fushat
        print(
            f"Shtuar borxhi: Debitori={debtor}, Shuma={amount}, Norma e Interesit={interest}, Data e Afatit={due_date}")
        toast("Borxhi u shtua me sukses!")

        # Pastro fushat e tekstit pasi të shtohet borxhi
        self.clear_inputs()

    def validate_inputs(self, debtor, amount, interest, due_date):
        """Funksion për të verifikuar hyrjet e përdoruesit."""
        # Kontrollo që të gjitha fushat janë plotësuar
        if not debtor:
            toast("Ju lutem plotësoni fushën 'Debitori'")
            return False
        if not amount:
            toast("Ju lutem plotësoni fushën 'Shuma'")
            return False
        if not interest:
            toast("Ju lutem plotësoni fushën 'Norma e Interesit'")
            return False
        if not due_date:
            toast("Ju lutem plotësoni fushën 'Data e Afatit'")
            return False

        # Kontrollo që shuma dhe norma e interesit janë numra validë dhe pozitivë
        try:
            amount = float(amount)
            interest = float(interest)
            if amount <= 0:
                toast("Shuma duhet të jetë një numër pozitiv")
                return False
            if interest < 0:
                toast("Norma e interesit nuk mund të jetë negative")
                return False
        except ValueError:
            toast("Shuma dhe norma e interesit duhet të jenë numra validë")
            return False

        # Kontrollo që data e afatit është e formatit të duhur dhe është në të ardhmen
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj < datetime.now():
                toast("Data e afatit duhet të jetë në të ardhmen")
                return False
        except ValueError:
            toast("Data e afatit duhet të jetë e formatit yyyy-mm-dd")
            return False

        return True

    def clear_inputs(self):
        """Funksion për të pastruar të gjitha fushat e tekstit."""
        self.debtor_input.text = ""
        self.amount_input.text = ""
        self.interest_input.text = ""
        self.due_date_input.text = ""

    def go_back_to_dashboard(self, *args):
        # Kalo në ekranin e dashboard-it
        self.manager.current = "dashboard"
