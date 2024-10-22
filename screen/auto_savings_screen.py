from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel


class AutoSavingsScreen(Screen):
    def __init__(self, **kwargs):
        super(AutoSavingsScreen, self).__init__(**kwargs)
        self.add_widget(
            MDLabel(text="Cakto Kursime Automatike", halign="center"))
        # Mund të shtosh form për kursime automatike
