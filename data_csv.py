import csv
from faker import Faker
from random import randint, choice

# Створення Faker об'єкта з українською локалізацією
fake = Faker(locale='uk_UA')

# Словники по батькові для чоловіків і жінок
male_patronymics = [
    "Олександрович", "Іванович", "Васильович", "Миколайович", "Петрович",
    "Андрійович", "Володимирович", "Борисович", "Георгійович", "Дмитрович",
    "Сергійович", "Григорович", "Михайлович", "Євгенович", "Максимович",
    "Олегович", "Павлович", "Романович", "Степанович", "Тарасович"
]

female_patronymics = [
    "Олександрівна", "Іванівна", "Василівна", "Миколаївна", "Петрівна",
    "Андріївна", "Володимирівна", "Борисівна", "Георгіївна", "Дмитрівна",
    "Сергіївна", "Григорівна", "Михайлівна", "Євгенівна", "Максимівна",
    "Олегівна", "Павлівна", "Романівна", "Степанівна", "Тарасівна"
]

# Генерація одного запису співробітника
def generate_employee(gender):
    if gender == 'Чоловік':
        first_name = fake.first_name_male()
        patronymic = choice(male_patronymics)
    else:
        first_name = fake.first_name_female()
        patronymic = choice(female_patronymics)

    return [
        fake.last_name(),  # Прізвище
        first_name,        # Ім'я
        patronymic,        # По батькові
        gender,            # Стать
        fake.date_of_birth(minimum_age=16, maximum_age=85).strftime("%Y-%m-%d"),  # Дата народження
        fake.job(),        # Посада
        fake.city(),       # Місто проживання
        fake.address(),    # Адреса проживання
        fake.phone_number(), # Телефон
        fake.email()       # Email
    ]

# Створення CSV-файлу з 2000 записами
def create_csv_file(filename, num_records=2000):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'Прізвище', 'Ім’я', 'По батькові', 'Стать', 'Дата народження',
            'Посада', 'Місто проживання', 'Адреса проживання', 'Телефон', 'Email'
        ])

        # 60% чоловіків і 40% жінок
        for _ in range(num_records):
            gender = 'Чоловік' if randint(1, 100) <= 60 else 'Жінка'
            writer.writerow(generate_employee(gender))

# Запуск генерації
if __name__ == "__main__":
    create_csv_file('employees.csv')
    print("CSV файл успішно створено!")
