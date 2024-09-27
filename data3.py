import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime


# Функція для підрахунку віку
def calculate_age(birthdate):
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


# Функція для зчитування даних з CSV файлу та виконання аналізу
def analyze_employees(csv_filename):
    try:
        # Перевіряємо наявність CSV-файлу
        if not os.path.exists(csv_filename):
            print("Помилка: CSV файл не знайдено!")
            return

        # Змінні для підрахунків
        male_count = 0
        female_count = 0
        age_groups = {
            "younger_18": 0,
            "18-45": 0,
            "45-70": 0,
            "older_70": 0,
        }
        gender_age_groups = {
            "male": {"younger_18": 0, "18-45": 0, "45-70": 0, "older_70": 0},
            "female": {"younger_18": 0, "18-45": 0, "45-70": 0, "older_70": 0},
        }

        # Читаємо дані з CSV файлу
        with open(csv_filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаємо заголовок

            for row in reader:
                gender = row[3]
                birthdate = datetime.strptime(row[4], "%Y-%m-%d")
                age = calculate_age(birthdate)

                # Підрахунок статі
                if gender == 'Чоловік':
                    male_count += 1
                elif gender == 'Жінка':
                    female_count += 1

                # Підрахунок вікових категорій
                if age < 18:
                    age_groups["younger_18"] += 1
                    if gender == 'Чоловік':
                        gender_age_groups["male"]["younger_18"] += 1
                    else:
                        gender_age_groups["female"]["younger_18"] += 1
                elif 18 <= age <= 45:
                    age_groups["18-45"] += 1
                    if gender == 'Чоловік':
                        gender_age_groups["male"]["18-45"] += 1
                    else:
                        gender_age_groups["female"]["18-45"] += 1
                elif 45 < age <= 70:
                    age_groups["45-70"] += 1
                    if gender == 'Чоловік':
                        gender_age_groups["male"]["45-70"] += 1
                    else:
                        gender_age_groups["female"]["45-70"] += 1
                else:
                    age_groups["older_70"] += 1
                    if gender == 'Чоловік':
                        gender_age_groups["male"]["older_70"] += 1
                    else:
                        gender_age_groups["female"]["older_70"] += 1

        # Виведення результатів в консоль
        print("Кількість чоловіків:", male_count)
        print("Кількість жінок:", female_count)

        for group, count in age_groups.items():
            print(f"Кількість співробітників у віковій категорії {group}: {count}")

        # Візуалізація
        # Діаграма статі
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        plt.bar(['Чоловіки', 'Жінки'], [male_count, female_count], color=['blue', 'pink'])
        plt.title('Кількість співробітників за статтю')
        plt.xlabel('Стать')
        plt.ylabel('Кількість')

        # Діаграма вікових категорій
        plt.subplot(1, 2, 2)
        plt.bar(age_groups.keys(), age_groups.values(), color='green')
        plt.title('Кількість співробітників за віковими категоріями')
        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість')

        plt.tight_layout()
        plt.show()

        # Діаграма статі за віковими категоріями
        categories = list(gender_age_groups["male"].keys())
        male_counts = [gender_age_groups["male"][cat] for cat in categories]
        female_counts = [gender_age_groups["female"][cat] for cat in categories]

        plt.figure(figsize=(10, 5))
        x = range(len(categories))
        plt.bar(x, male_counts, width=0.4, label='Чоловіки', color='blue', align='center')
        plt.bar([i + 0.4 for i in x], female_counts, width=0.4, label='Жінки', color='pink', align='center')

        plt.title('Кількість співробітників за віковими категоріями та статтю')
        plt.xlabel('Вікова категорія')
        plt.ylabel('Кількість')
        plt.xticks([i + 0.2 for i in x], categories)
        plt.legend()
        plt.show()

        print("Ok, аналіз успішно завершено!")

    except Exception as e:
        print(f"Помилка: {e}")


# Запуск програми
if __name__ == "__main__":
    csv_file = 'employees.csv'
    analyze_employees(csv_file)
