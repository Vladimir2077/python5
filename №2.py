def reversed3(variable): 
    if len(variable) == 1:
        return variable
    return variable[-1] + reversed3(variable[:-1])
n = reversed3(input("Введите числа через пробел: "))
print(f"Числа в обратном порядке: {n} ")