from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.pickers import MDDatePicker
from models.bills import get_bills


class CalendarScreen(Screen):  # Sigurohu që të trashëgojë nga Screen
    def __init__(self, **kwargs):
        # Përdor formatin korrekt të super
        super(CalendarScreen, self).__init__(**kwargs)

        # Krijo një layout të brendshëm
        layout = MDBoxLayout(orientation='vertical')

        # Shto përmbajtjen në layout
        self.show_bills_calendar(layout)

        self.add_widget(layout)  # Shto layout në ekran

    def show_bills_calendar(self, layout):
        bills = get_bills()
        for bill in bills:
            name, amount, due_date, status = bill[1], bill[2], bill[3], bill[4]
            label = f"{name}: ${amount} - Due {due_date}"
            layout.add_widget(MDLabel(text=label, halign="center"))

    def open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        print(f"Data e përzgjedhur: {value}")
