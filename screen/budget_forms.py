from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddBudgetForm(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        # Fushat e tekstit për të shtuar informacionin për buxhetin
        self.budget_name = MDTextField(
            hint_text="Emri i Buxhetit", mode="rectangle")
        self.budget_amount = MDTextField(
            hint_text="Shuma e Buxhetit", mode="rectangle")

        # Shto fushat në formë
        self.add_widget(self.budget_name)
        self.add_widget(self.budget_amount)


class UpdateBudgetForm(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        # Fushat e tekstit për përditësimin e informacionit për buxhetin
        self.budget_name = MDTextField(
            hint_text="Emri i Buxhetit (Përditësim)", mode="rectangle")
        self.budget_amount = MDTextField(
            hint_text="Shuma e Buxhetit (Përditësim)", mode="rectangle")

        # Shto fushat në formë
        self.add_widget(self.budget_name)
        self.add_widget(self.budget_amount)
