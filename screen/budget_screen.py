from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from models.budget import add_budget, get_budgets, update_budget


class BudgetScreen(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.category_input = MDTextField(
            hint_text="Kategoria e Buxhetit", size_hint_x=None, width=300)
        self.limit_input = MDTextField(
            hint_text="Limiti i Buxhetit", size_hint_x=None, width=300)
        self.add_button = MDRaisedButton(
            text="Shto Buxhet", on_release=self.add_budget)

        self.add_widget(MDLabel(text="Menaxhimi i Buxhetit",
                        font_style="H4", halign="center"))
        self.add_widget(self.category_input)
        self.add_widget(self.limit_input)
        self.add_widget(self.add_button)

        self.show_budgets()

    def add_budget(self, instance):
        category = self.category_input.text
        limit = float(self.limit_input.text)
        add_budget(category, limit)
        self.show_budgets()

    def show_budgets(self):
        budgets = get_budgets()
        for budget in budgets:
            category, limit = budget[1], budget[2]
            self.add_widget(
                MDLabel(text=f"{category}: ${limit}", halign="left"))
