#1
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year_to_check = 2020
if is_leap_year(year_to_check):
    print(f"{year_to_check} є високосним роком.")
else:
    print(f"{year_to_check} не є високосним роком.")
#2
def days_in_month(year, month):
    days_per_month = {
        1: 31,  # січень
        2: 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28,  # лютий
        3: 31,  # березень
        4: 30,  # квітень
        5: 31,  # травень
        6: 30,  # червень
        7: 31,  # липень
        8: 31,  # серпень
        9: 30,  # вересень
        10: 31,  # жовтень
        11: 30,  # листопад
        12: 31   # грудень
    }
    if month < 1 or month > 12:
        return "Некоректний місяць"
    return days_per_month[month]
year_to_check = 2020
month_to_check = 2
result = days_in_month(year_to_check, month_to_check)
if isinstance(result, int):
    print(f"У {year_to_check} році, у місяці {month_to_check} - {result} днів.")
else:
    print(result)
#3
def day_of_year(year, month, day):
    days_per_month = {
        1: 31,  # січень
        2: 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28,  # лютий
        3: 31,  # березень
        4: 30,  # квітень
        5: 31,  # травень
        6: 30,  # червень
        7: 31,  # липень
        8: 31,  # серпень
        9: 30,  # вересень
        10: 31,  # жовтень
        11: 30,  # листопад
        12: 31   # грудень
    }
    if month < 1 or month > 12 or day < 1 or day > days_per_month[month]:
        return None
    day_count = sum(days_per_month[i] for i in range(1, month)) + day

    return day_count
year_to_check = 2021
month_to_check = 4
day_to_check = 12

result = day_of_year(year_to_check, month_to_check, day_to_check)

if result is not None:
    print(f"У {year_to_check} році, {month_to_check} місяці, {day_to_check} числа - це {result}-й день року.")
else:
    print("Введені дані некоректні.")
#4
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


num_to_check = 13

if is_prime(num_to_check):
    print(f"{num_to_check} є простим числом.")
else:
    print(f"{num_to_check} не є простим числом.")
#5
def liters_100km_to_miles_gallon(liters):
    miles_per_gallon = (100 * 3.785) / (liters * 1.609)
    return miles_per_gallon
def miles_gallon_to_liters_100km(miles):
    liters_per_100km = (100* 3.785) / (miles * 1.609)
    return liters_per_100km
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
#6
def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
side1 = 3
side2 = 4
side3 = 5

if is_a_triangle(side1, side2, side3):
    print("Можна побудувати трикутник.")
else:
    print("Не можна побудувати трикутник.")
#7
def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        else:
            return False
    else:
        return False
side1 = 3
side2 = 4
side3 = 5

if is_a_right_triangle(side1, side2, side3):
    print("Трикутник зі сторонами", side1, side2, side3, "є прямокутним.")
else:
    print("Трикутник зі сторонами", side1, side2, side3, "не є прямокутним або не існує.")