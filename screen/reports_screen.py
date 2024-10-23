from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
import matplotlib.pyplot as plt
from io import BytesIO
from kivy.core.image import Image as CoreImage
from models.reports import generate_monthly_report


from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen


class ReportsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Krijimi i një layouti të ri
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Butoni 'Back'
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(None, None),
            size=(150, 40),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.go_back_to_dashboard()  # Përdorim funksionin për kthim
        )

        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back_to_dashboard(self):
        self.manager.current = 'dashboard'

    def generate_report(self, *args):
        report_data = generate_monthly_report()
        fig, ax = plt.subplots()
        categories = list(report_data.keys())
        amounts = list(report_data.values())
        ax.bar(categories, amounts)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        im = CoreImage(BytesIO(buf.read()), ext='png').texture
        self.canvas.add(im)
