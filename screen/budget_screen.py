from .budget_forms import AddBudgetForm, UpdateBudgetForm
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import Screen


class BudgetScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_layout()
        self.dialog = None

    def build_layout(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Butoni për të shtuar buxhet të ri
        add_button = MDRaisedButton(
            text="Shto Buxhet", on_release=self.show_add_budget_dialog)

        # Butoni për të përditësuar buxhetin
        update_button = MDRaisedButton(
            text="Përditëso Buxhetin", on_release=self.show_update_budget_dialog)

        # Butoni për të fshirë buxhetin
        delete_button = MDRaisedButton(
            text="Fshij Buxhetin", on_release=self.show_delete_budget_dialog)

        # Butoni për t'u kthyer
        back_button = MDRaisedButton(
            text="Back", on_release=self.go_back_to_dashboard)

        layout.add_widget(add_button)
        layout.add_widget(update_button)
        layout.add_widget(delete_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    # Definoni metodën 'go_back_to_dashboard'
    def go_back_to_dashboard(self, *args):
        self.manager.current = 'dashboard'

    def show_add_budget_dialog(self, *args):
        self.dialog = MDDialog(
            title="Shto Buxhet të Ri",
            type="custom",
            content_cls=AddBudgetForm(),
            buttons=[
                MDRaisedButton(text="Shto", on_release=self.add_budget),
                MDRaisedButton(
                    text="Mbyll", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()

    def show_update_budget_dialog(self, *args):
        self.dialog = MDDialog(
            title="Përditëso Buxhetin",
            type="custom",
            content_cls=UpdateBudgetForm(),
            buttons=[
                MDRaisedButton(text="Përditëso",
                               on_release=self.update_budget),
                MDRaisedButton(
                    text="Mbyll", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()

    def show_delete_budget_dialog(self, *args):
        # Këtu shtoni funksionalitetin për të fshirë një buxhet
        pass
