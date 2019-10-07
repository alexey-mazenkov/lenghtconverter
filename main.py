# Objective: to develop a length measure converter.

print("""Список поддерживаемых мер длины:                                                                  
Миллиметр : mm
Сантиметр : cm
Дюйм : inch
Дециметр : dm
Метр : m 
Километр : km
""")  # Print The list of supported measures of length.

length_unit = input(
    'Введите меру длины, которую следует преобразовать (mm, cm, inch, dm, m, km): '
)  # The choice of measures of length.

if length_unit == 'mm':
    length = int(input('Введите длину в миллиметрах: '))

    if length == 1:
        print(length, 'миллиметр в сантиметрах =', length * 0.1)
        print(length, 'миллиметр в дюймах = ', length * 0.039)
        print(length, 'миллиметр в дециметрах =', length * 0.01)
        print(length, 'миллиметр в метрах =', length * 0.001)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'миллиметра в сантиметрах =', length * 0.1)
        print(length, 'миллиметра в дюймах = ', length * 0.039)
        print(length, 'миллиметра в дециметрах =', length * 0.01)
        print(length, 'миллиметра в метрах =', length * 0.001)

    else:
        print(length, 'миллиметров в сантиметрах =', length * 0.1)
        print(length, 'миллиметров в дюймах = ', length * 0.039)
        print(length, 'миллиметров в дециметрах =', length * 0.01)
        print(length, 'миллиметров в метрах =', length * 0.001)

if length_unit == 'cm':
    length = int(input('Введите длину в сантиметрах:'))

    if length == 1:
        print(length, 'сантиметр в миллиметрах =', length * 10)
        print(length, 'сантиметр в дюймах = ', length * 0.39)
        print(length, 'сантиметр в дециметрах =', length * 0.1)
        print(length, 'сантиметр в метрах =', length * 0.01)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'сантиметра в миллиметрах =', length * 10)
        print(length, 'сантиметра в дюймах = ', length * 0.39)
        print(length, 'сантиметра в дециметрах =', length * 0.1)
        print(length, 'сантиметра в метрах =', length * 0.01)

    else:
        print(length, 'сантиметров в миллиметрах =', length * 10)
        print(length, 'сантиметров в дюймах = ', length * 0.3937)
        print(length, 'сантиметров в дециметрах =', length * 0.1)
        print(length, 'сантиметров в метрах =', length * 0.01)
        print(length, 'сантиметров в километрах =', length * 0.00001)

if length_unit == 'inch':
    length = int(input('Введите длину в дюймах:'))

    if length == 1:
        print(length, 'дюйм в миллиметрах =', length * 25.4)
        print(length, 'дюйм в сантиметрах = ', length * 2.54)
        print(length, 'дюйм в дециметрах =', length * 0.254)
        print(length, 'дюйм в метрах =', length * 0.0254)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'дюйма в миллиметрах =', length * 25.4)
        print(length, 'дюйма в сантиметрах = ', length * 2.54)
        print(length, 'дюйма в дециметрах =', length * 0.254)
        print(length, 'дюйма в метрах =', length * 0.0254)

    else:
        print(length, 'дюймов в миллиметрах =', length * 25.4)
        print(length, 'дюймов в сантиметрах = ', length * 2.54)
        print(length, 'дюймов в дециметрах =', length * 0.254)
        print(length, 'дюймов в метрах =', length * 0.0254)
        print(length, 'дюймов в километрах =', length * 0.000025)

if length_unit == 'dm':
    length = int(input('Введите длину в дециметрах:'))

    if length == 1:
        print(length, 'дециметр в миллиметрах =', length * 100)
        print(length, 'дециметр в сантиметрах = ', length * 10)
        print(length, 'дециметр в дюймах =', length * 3.94)
        print(length, 'дециметр в метрах =', length * 0.1)
        print(length, 'дециметр в километрах =', length * 0.0001)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'дециметра в миллиметрах =', length * 100)
        print(length, 'дециметра в сантиметрах = ', length * 10)
        print(length, 'дециметра в дюймах =', length * 3.94)
        print(length, 'дециметра в метрах =', length * 0.1)
        print(length, 'дециметра в километрах =', length * 0.0001)

    else:
        print(length, 'дециметров в миллиметрах =', length * 100)
        print(length, 'дециметров в сантиметрах = ', length * 10)
        print(length, 'дециметров в дюймах =', length * 3.94)
        print(length, 'дециметров в метрах =', length * 0.1)
        print(length, 'дециметров в километрах =', length * 0.0001)

if length_unit == 'm':
    length = int(input('Введите длину в метрах:'))

    if length == 1:
        print(length, 'метр в миллиметрах =', length * 1000)
        print(length, 'метр в сантиметрах = ', length * 100)
        print(length, 'метр в дюймах =', length * 39.4)
        print(length, 'метр в дециметрах =', length * 10)
        print(length, 'метр в километрах =', length * 0.001)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'метра в миллиметрах =', length * 1000)
        print(length, 'метра в сантиметрах = ', length * 100)
        print(length, 'метра в дюймах =', length * 39.4)
        print(length, 'метра в дециметрах =', length * 10)
        print(length, 'метра в километрах =', length * 0.001)

    else:
        print(length, 'метров в миллиметрах =', length * 1000)
        print(length, 'метров в сантиметрах = ', length * 100)
        print(length, 'метров в дюймах =', length * 39.4)
        print(length, 'метров в дециметрах =', length * 10)
        print(length, 'метров в километрах =', length * 0.001)

if length_unit == 'km':
    length = int(input('Введите длину в километрах:'))

    if length == 1:
        print(length, 'километр в миллиметрах =', length * 1000000)
        print(length, 'километр в сантиметрах = ', length * 100000)
        print(length, 'километр в дюймах =', length * 39370)
        print(length, 'километр в дециметрах =', length * 10000)
        print(length, 'километр в метрах =', length * 1000)

    elif length == 2 or length == 3 or length == 4:
        print(length, 'километра в миллиметрах =', length * 1000000)
        print(length, 'километра в сантиметрах = ', length * 100000)
        print(length, 'километра в дюймах =', length * 39370)
        print(length, 'километра в дециметрах =', length * 10000)
        print(length, 'километра в метрах =', length * 1000)

    else:
        print(length, 'километров в миллиметрах =', length * 1000000)
        print(length, 'километров в сантиметрах = ', length * 100000)
        print(length, 'километров в дюймах =', length * 39370)
        print(length, 'километров в дециметрах =', length * 10000)
        print(length, 'километров в метрах =', length * 1000)