from kivy.clock import Clock


def send_notification(message, delay=0):
    """ Dërgo një njoftim pas një kohe të caktuar """
    if delay > 0:
        Clock.schedule_once(lambda dt: print(
            f"NOTIFICATION: {message}"), delay)
    else:
        print(f"NOTIFICATION: {message}")


def remind_bill_payment(bill_name, due_date):
    """ Dërgo një kujtesë për pagesën e faturës """
    message = f"Kujtesë: Pagesa për '{bill_name}' është e afërta në datën {due_date}."
    send_notification(message, delay=5)


def alert_budget_exceeded(category):
    """ Paralajmëro kur shpenzimet kalojnë buxhetin """
    message = f"Paralajmërim: Shpenzimet për '{category}' kanë tejkaluar buxhetin e caktuar."
    send_notification(message)
