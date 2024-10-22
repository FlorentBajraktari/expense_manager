from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from models.bills import get_paid_bills


class PaidBillsScreen(Screen):
    def __init__(self, **kwargs):
        super(PaidBillsScreen, self).__init__(**kwargs)
        self.display_paid_bills()

    def display_paid_bills(self):
        bills = get_paid_bills()
        for bill in bills:
            name, amount, due_date, status = bill[1], bill[2], bill[3], bill[4]
            label = MDLabel(
                text=f"{name}: ${amount} - Due: {due_date}", halign="left")
            self.add_widget(label)
