from datetime import datetime, timedelta
import re

# print('HW3_1')

# Функція, яка розраховує кількість днів між заданою датою {Date} і поточною датою.


def get_days_from_today(date: str) -> int:
    data_today = datetime.now().date()
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        return (data_today - target_date).days
    except ValueError:
        raise ValueError(
            "Error: Incorrect Date Format. Must be like 'YYYY-MM-DD'")


pattern = r"^\d{4}-\d{2}-\d{2}$"  # Задаємо патерн для перевірки формату
flag_to_stop = True
while flag_to_stop:
    date = input(
        "Enter target data in YYYY-MM-DD format (or exit - to cancel): ")
    if re.match(pattern, date):
        print(
            f"The distance to target Date is: {get_days_from_today(date)} days.")
    elif date == 'exit':
        flag_to_stop = False
    else:
        print("Error: Incorrect Date Format. Try again..")
