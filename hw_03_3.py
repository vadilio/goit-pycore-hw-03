# Завдання 3
# У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах.
import re


def normalize_phone(phone_number: str) -> str:
    # прибираємо все, що не є + (\+) або digit (\d)
    pattern = r"[^\+\d]"
    result = re.sub(pattern, '', phone_number)
    # прибираємо все +, окрім першого, якщо вони є
    pattern = r"(?<!^)\+"
    result = re.sub(pattern, '', result)
    # перевіряємо префікси та змінюємо
    if result.startswith('+380'):
        return result
    elif result.startswith('380'):
        result = '+'+result
        return result
    elif result.startswith('80'):
        result = '+3'+result
        return result
    elif result.startswith('0'):
        result = '+38'+result
        return result
    else:
        result = '+380'+result
        return result


# задаємо тестову стрічку
input_str = """
    +38(050)123-32-34"
     0503451234
(050)8889900
38050-111-22-22
  +38050 111+22 11
 50 400 57 21
"""
# розділяємо текст на елементі списку по срічках та прибираємо пусті елементи
number_list = list(filter(bool, re.split('\n+', input_str)))
# нормалізуємо текст
number_list = [normalize_phone(item) for item in number_list]
print(number_list)
