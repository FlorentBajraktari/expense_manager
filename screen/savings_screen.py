from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from models.savings import add_savings_goal, update_savings_amount, get_savings_goals


class SavingsScreen(Screen):  # Sigurohu që të trashëgojë nga Screen
    def __init__(self, **kwargs):
        # Përdor këtë format për të shmangur probleme të trashëguara
        super(SavingsScreen, self).__init__(**kwargs)

        # Krijo një layout të brendshëm
        layout = MDBoxLayout(orientation='vertical')

        self.goal_input = MDTextField(
            hint_text="Synimi i Kursimeve", size_hint_x=None, width=300)
        self.target_amount_input = MDTextField(
            hint_text="Shuma e Synuar", size_hint_x=None, width=300)
        self.add_button = MDRaisedButton(
            text="Shto Synim", on_release=self.add_goal)

        layout.add_widget(MDLabel(text="Menaxhimi i Kursimeve",
                          font_style="H4", halign="center"))
        layout.add_widget(self.goal_input)
        layout.add_widget(self.target_amount_input)
        layout.add_widget(self.add_button)

        self.add_widget(layout)  # Shto layout në ekran

    def add_goal(self, instance):
        goal = self.goal_input.text
        target_amount = float(self.target_amount_input.text)
        add_savings_goal(goal, target_amount)
        self.show_savings_goals()

    def show_savings_goals(self):
        savings = get_savings_goals()
        for saving in savings:
            goal, target_amount, current_amount = saving[1], saving[2], saving[3]
            self.add_widget(MDLabel(
                text=f"{goal}: Synim ${target_amount}, Aktualisht ${current_amount}", halign="left"))
