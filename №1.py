from math import sqrt

n = 0
while n < 2:
    n = int(input("Введите число: ")) 
i = 2
while i <= sqrt(n):
    if n % i == 0:
        print("Это составное число")
        break
    i += 1
else:
    print("это простое число")