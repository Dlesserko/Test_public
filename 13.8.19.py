a = int(input('Введите какое колличество билетов вам нужно? '))
b = int(input('Сколько вам лет? '))
if b <= 18:
    print('Проходите бесплатно')
elif all([18 <= b <= 25, a <= 3]):
    c = a * 990
    print(f'Цена за {a} биллета(ов) = {c}')
elif all([18 <= b <= 25, a > 3]):
    c = a * 990 - a*990/10
    print (f'Цена {a} биллета(ов) со скидкой {c}')
elif all([b > 25, a <= 3]):
    c = a * 1390
    print(f'Цена за {a} биллета(ов) = {c}')
else:
    c = a * 1390 - a * 1390 / 10
    print(f'Цена {a} биллета(ов) со скидкой {c}')