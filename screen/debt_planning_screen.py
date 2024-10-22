from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel


class DebtPlanningScreen(Screen):
    def __init__(self, **kwargs):
        super(DebtPlanningScreen, self).__init__(**kwargs)
        self.add_widget(
            MDLabel(text="Planifiko Shlyerjet e Borxheve", halign="center"))
        # Mund të shtosh form për planifikimin e shlyerjeve të borxheve
