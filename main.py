from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from screen.dashboard_screen import DashboardScreen
from screen.paid_bills_screen import PaidBillsScreen
from screen.unpaid_bills_screen import UnpaidBillsScreen
from screen.add_bill_screen import AddBillScreen
from screen.auto_savings_screen import AutoSavingsScreen
from screen.debts_screen import DebtsScreen
from screen.debt_planning_screen import DebtPlanningScreen
from screen.budget_screen import BudgetScreen
from screen.reports_screen import ReportsScreen
from screen.login_screen import LoginScreen


class ExpenseManagerApp(MDApp):
    def build(self):
        sm = ScreenManager()

        # Shto të gjitha ekranet në `ScreenManager`
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(PaidBillsScreen(name="paid_bills"))
        sm.add_widget(UnpaidBillsScreen(name="unpaid_bills"))
        sm.add_widget(AddBillScreen(name="add_bill"))
        sm.add_widget(AutoSavingsScreen(name="auto_savings"))
        sm.add_widget(DebtsScreen(name="debts"))
        sm.add_widget(DebtPlanningScreen(name="debt_planning"))
        sm.add_widget(BudgetScreen(name="budget"))
        sm.add_widget(ReportsScreen(name="reports"))

        return sm


if __name__ == '__main__':
    ExpenseManagerApp().run()
