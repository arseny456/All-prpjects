def arifmetic(Num1,Num2,Dectvie):
    if Dectvie == '+':
        return Num1+Num2
    elif Dectvie == '-':
        return Num1 - Num2
    elif Dectvie == '*':
        return Num1 * Num2
    elif Dectvie == '/':
        return Num1 / Num2
    else:
        return "Неверный знак операции!"


print(arifmetic(5, 4, ''))