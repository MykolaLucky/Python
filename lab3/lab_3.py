#1
import math

μ = 0
σ = 2

x = float(input("Введіть значення x: "))
y = 1 / (σ * math.sqrt(2 * math.pi)) * math.exp(-((x - μ) ** 2) / (2 * σ ** 2))
print(f'Значення функції Гауса для x = {x}, μ = {μ}, σ = {σ}: {y}')
#2

john = 5
mary = 7
adam = 3
print(f'Змінні: {john}, {mary}, {adam}')
total_apples = john + mary + adam
print(f'Загальна кількість яблук: {total_apples}')
#3
miles = 7.38
kilometers = 12.25

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#3
x = 1
x = float(x)
y = 3 * (x**3) - 2 * (x**2) + 3**x - 1
print("y =", y)
#4
# this program computes the number of seconds in a given number of hours

hours = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Seconds in Hours: ", hours * seconds) # printing the number of seconds in a given number of hours

#this is the end of the program that computes the number of seconds in 2 hour
#5
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

print("Додавання:",a+b)
print("Віднімання:",a-b)
print("Множення:",a*b)
print("Ділення:", a / b)
#6
x = float(input("Enter value for x: "))

y= 1 / (x + (1 / (x + (1 / (x + (1 / (x + (1 / x))))))))

print("y =", y)
#7
start_hour = int(input("Введіть години початку (0-23): "))
start_minute = int(input("Введіть хвилини початку (0-59): "))
duration_minutes = int(input("Введіть тривалість події у хвилинах: "))
end_hour = (start_hour + (start_minute + duration_minutes) // 60) % 24
end_minute = (start_minute + duration_minutes) % 60
print(f"Подія закінчується о {end_hour}:{end_minute}")