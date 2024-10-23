from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from models.savings import get_auto_savings, add_saving_goal, update_saving_goal, delete_saving_goal


class AutoSavingsScreen(Screen):
    def __init__(self, **kwargs):
        super(AutoSavingsScreen, self).__init__(**kwargs)
        self.build_layout()

    def build_layout(self):
        layout = MDBoxLayout(orientation='vertical',
                             padding=(10, 10), spacing=10)

        # Butoni për kthim mbrapa
        back_button = MDRaisedButton(
            text="Back",
            size_hint=(1, None),
            height=50,
            on_release=self.go_back
        )

        # Butonat për Add, Update dhe Delete
        buttons_layout = MDBoxLayout(
            orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        add_button = MDRaisedButton(text="Add", on_release=self.add_saving)
        update_button = MDRaisedButton(
            text="Update", on_release=self.update_saving)
        delete_button = MDRaisedButton(
            text="Delete", on_release=self.delete_saving)

        buttons_layout.add_widget(add_button)
        buttons_layout.add_widget(update_button)
        buttons_layout.add_widget(delete_button)

        # Tabela për kursimet automatike
        savings = get_auto_savings()
        self.data_tables = MDDataTable(
            size_hint=(1, 0.7),
            column_data=[
                ("ID", dp(30)),
                ("Përshkrimi", dp(60)),
                ("Shuma", dp(30)),
                ("Frequenca", dp(60))
            ],
            row_data=[
                (str(saving[0]), saving[1], f"${saving[2]:.2f}", saving[3])
                for saving in savings
            ]
        )

        layout.add_widget(back_button)
        layout.add_widget(buttons_layout)
        layout.add_widget(self.data_tables)
        self.add_widget(layout)

    def go_back(self, *args):
        self.manager.current = "dashboard"

    def add_saving(self, *args):
        pass

    def update_saving(self, *args):
        pass

    def delete_saving(self, *args):
        pass
