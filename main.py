from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from models.database import create_tables
from screen.budget_screen import BudgetScreen
from screen.reports_screen import ReportsScreen
from screen.dashboard_screen import DashboardScreen
from screen.auto_savings_screen import AutoSavingsScreen
from screen.debt_planning_screen import DebtPlanningScreen
from screen.paid_bills_screen import PaidBillsScreen
from screen.unpaid_bills_screen import UnpaidBillsScreen
from screen.add_bill_screen import AddBillScreen
from screen.login_screen import LoginScreen  # Regjistro LoginScreen


class ExpenseManagerApp(MDApp):
    def build(self):
        create_tables()  # Sigurohu që të gjitha tabelat krijohen

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))  # Shto LoginScreen
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(AutoSavingsScreen(name="auto_savings"))
        sm.add_widget(DebtPlanningScreen(name="debt_planning"))
        sm.add_widget(PaidBillsScreen(name="paid_bills"))
        sm.add_widget(UnpaidBillsScreen(name="unpaid_bills"))
        sm.add_widget(AddBillScreen(name="add_bill"))
        sm.add_widget(BudgetScreen(name="budget"))
        sm.add_widget(ReportsScreen(name="reports"))

        return sm


if __name__ == '__main__':
    ExpenseManagerApp().run()


# Cakto Kursimet Automatike, Menaxho Buxhetin , Planifiko Shlyrjet, Buxheti, Gjenero Raporte
