from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddBudgetForm(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.add_widget(MDTextField(hint_text="Emri i Buxhetit"))
        self.add_widget(MDTextField(hint_text="Shuma", input_filter='float'))


class UpdateBudgetForm(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.add_widget(MDTextField(hint_text="Emri i Buxhetit"))
        self.add_widget(MDTextField(
            hint_text="Shuma e Re", input_filter='float'))
