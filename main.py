from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from screen.login_screen import LoginScreen
from screen.dashboard_screen import DashboardScreen
from screen.bills_screen import BillsScreen
from screen.paid_bills_screen import PaidBillsScreen
from screen.unpaid_bills_screen import UnpaidBillsScreen
from screen.add_bill_screen import AddBillScreen
from screen.auto_savings_screen import AutoSavingsScreen
from screen.debt_planning_screen import DebtPlanningScreen
from models.database import create_tables


class ExpenseManagerApp(MDApp):
    def build(self):
        create_tables()
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(PaidBillsScreen(name="paid_bills"))
        sm.add_widget(UnpaidBillsScreen(name="unpaid_bills"))
        sm.add_widget(AddBillScreen(name="add_bill"))
        sm.add_widget(AutoSavingsScreen(name="auto_savings"))
        sm.add_widget(DebtPlanningScreen(name="debt_planning"))
        return sm


if __name__ == '__main__':
    ExpenseManagerApp().run()
