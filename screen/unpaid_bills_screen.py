from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from models.bills import get_unpaid_bills


class UnpaidBillsScreen(Screen):
    def __init__(self, **kwargs):
        super(UnpaidBillsScreen, self).__init__(**kwargs)
        self.display_unpaid_bills()

    def display_unpaid_bills(self):
        bills = get_unpaid_bills()
        for bill in bills:
            name, amount, due_date, status = bill[1], bill[2], bill[3], bill[4]
            label = MDLabel(
                text=f"{name}: ${amount} - Due: {due_date}", halign="left")
            self.add_widget(label)
