#1
n = int(input("Введіть ціле число n: "))
result = n >= 100
print(result)
#2
number1 = float(input("Введіть перше дійсне число: "))
number2 = float(input("Введіть друге дійсне число: "))

if number1 > number2:
    max_number = number1
else:
    max_number = number2

print("Найбільше число: ", max_number)
#3
user_input = input()

if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever")
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {user_input}!")
#4
income = float(input("Enter the annual income: "))
if income <= 85528:
    tax = income * 0.18 - 556.02
    if tax < 0:
        tax = 0
else:
    tax = 14839.02 + (income - 85528) * 0.32
tax = round(tax)
print("The tax is:", tax, "thalers")
#5
year = int(input("Введіть рік: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - високосний рік")
else:
    print(f"{year} - звичайний рік")
#6
секретне_число_фокусника = 42

while True:
    введене_число = int(input("Введіть ціле число: "))
    if введене_число == секретне_число_фокусника:
        print(f"Молодець, магле! Тепер ти вільний.")
        break
    else:
        print("Ха-ха! Ви застрягли у моїй петлі! Спробуйте ще раз.")
#7
import time

for i in range(1, 6):
    print("Міссісіпі", i)
    time.sleep(1)

print("Ready or not, here I come!")
#8
while True:
    user_input = input("Введіть слово: ")

    if user_input == "chupacabra":
        print("You've successfully left the loop.")
        break
#9
user_word = input("Введіть слово: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)
#10
user_word = input("Введіть слово: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)
#11
blocks_available = int(input("Введіть кількість доступних блоків: "))

height = 0

while blocks_available >= height + 1:
    height += 1
    blocks_available -= height

print("Максимальна висота піраміди:", height)
#12
c0 = int(input("Введіть натуральне число c0: "))
initial_c0 = c0
кількість_кроків = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    кількість_кроків += 1
print(f"Для досягнення 1 з числа {initial_c0} знадобилося {кількість_кроків} кроків.")
