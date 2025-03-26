import random
import calendar
from datetime import datetime, timedelta


# створимо функцію, яка згенерує список співробітників
def generate_employees(num_employees: int) -> list:
    employees = []

    for i in range(1, num_employees + 1):
        # Формируем имя сотрудника
        name = f'name{i}'

        # Генерируем случайную дату рождения
        start_date = datetime(1970, 1, 1)  # Начало диапазона (01.01.1970)
        end_date = datetime(2007, 12, 31)  # Конец диапазона (31.12.2000)
        delta = end_date - start_date

        # Случайная дата рождения
        random_days = random.randint(0, delta.days)
        birth_date = start_date + timedelta(days=random_days)

        # Форматируем дату в строку YYYY-MM-DD
        birth_date_str = birth_date.strftime('%Y-%m-%d')

        # Добавляем словарь в список
        employees.append({'name': name, 'birthday': birth_date_str})

    return employees


# Створюємо функцію, яка надаст інформацію про найближчі ДН
def get_upcoming_birthdays(users):
    today = datetime.today().date()  # поточна дата
    upcoming_birthdays = []
    # перебираємо всі словники
    for user in users:
        # Перетворюємо дату народження користувача з рядка в об'єкт datetime
        try:
            birthday = datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        except ValueError:
            # Якщо дата не вірного формату, викидаємо виключення
            print(
                f"Помилка: Невірний формат дати для користувача {user['name']}: {user['birthday']}")
          # Пропускаємо цього користувача і продовжуємо далі

        # Перевірка, чи день народження вже був у цьому році
        # flag_pass_b - true якщо ДН вже був в цьому році
        # перевірка віключення, якщо ДН був у високосному році 29 лютого то
        # порівняння робимо з урахуванням помилки
        try:
            flag_pass_b = datetime(
                today.year, birthday.month, birthday.day).date() < today
        except ValueError:
            flag_pass_b = datetime(
                today.year, birthday.month, birthday.day-1).date() < today
        # Якщо ДН вже був в цьому році, то змінюємо рік на наступній с урахуванням високосного року
        if flag_pass_b:
            # перевіряємо, чи не є дата народження 29 лютого у високосному році.
            # якщо ДН вже в цьому році був, то переносимо на наступний рік, але якщо
            # наступний рік не високосний - змінюемо день народженя 29 лютого на -1 день
            if birthday.month == 2 and birthday.day == 29 and not calendar.isleap(today.year+1):
                birthday = datetime(
                    today.year + 1, birthday.month, birthday.day-1).date()
            else:
                birthday = datetime(
                    today.year + 1, birthday.month, birthday.day).date()

        else:
            birthday = datetime(today.year, birthday.month,
                                birthday.day).date()

        # Перевіряємо, чи дата народження припадає на наступні 7 днів
        if birthday-today <= timedelta(days=7):
           # today-birthday <= today + timedelta(days=7):
           # print(birthday-today)
           # Перевірка, чи день народження припадає на вихідний
            if birthday.weekday() >= 5:  # 5 - субота, 6 - неділя
                # Якщо на вихідний, переносимо на наступний понеділок
                days_to_monday = 7 - birthday.weekday()
                birthday = birthday + timedelta(days=days_to_monday)

            # Додаємо до списку результуючий словник з ім'ям і датою привітання
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday.strftime("%Y-%m-%d")
            })

    return upcoming_birthdays


# генеруємо список з 20 співробытників
employee_list = generate_employees(20000)

# видаємо список
for employee in employee_list:
    # print(employee)
    pass


# Викликаємо функцію
upcoming_birthdays = get_upcoming_birthdays(employee_list)

# Виводимо результат
for user in upcoming_birthdays:
    print(user)
