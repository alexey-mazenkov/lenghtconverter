# File with RU and EN localization packages.

lang = input('''Выберите язык
Choose language(ru/en): ''')

if lang == 'ru':
    length_unit_choose = 'Введите меру длины, которую следует преобразовать (mm, cm, inch, dm, m, km): '

    measures_list = '''Список поддерживаемых мер длины:                                                                  
    Миллиметр : mm
    Сантиметр : cm
    Дюйм : inch
    Дециметр : dm
    Метр : m 
    Километр : km
    '''

    input_length_in_mm = 'Введите длину в миллиметрах: '
    input_length_in_cm = 'Введите длину в сантиметрах: '
    input_length_in_inch = 'Введите длину в дюймах: '
    input_length_in_dm = 'Введите длину в дециметрах: '
    input_length_in_m = 'Введите длину в метрах: '
    input_length_in_km = 'Введите длину в километрах: '

    mm_in_cm1 = 'миллиметр в сантиметрах ='
    mm_in_cm2 = 'миллиметра в сантиметрах ='
    mm_in_cm3 = 'миллиметров в сантиметрах ='

    mm_in_inch1 = 'миллиметр в дюймах ='
    mm_in_inch2 = 'миллиметра в дюймах ='
    mm_in_inch3 = 'миллиметров в дюймах ='

    mm_in_dm1 = 'миллиметр в дециметрах ='
    mm_in_dm2 = 'миллиметра в дециметрах ='
    mm_in_dm3 = 'миллиметров в дециметрах ='

    mm_in_m1 = 'миллиметр в метрах ='
    mm_in_m2 = 'миллиметра в метрах ='
    mm_in_m3 = 'миллиметров в метрах ='

    cm_in_mm1 = 'сантиметр в миллиметрах ='
    cm_in_mm2 = 'сантиметра в миллиметрах ='
    cm_in_mm3 = 'сантиметров в миллиметрах ='

    cm_in_inch1 = 'сантиметр в дюймах ='
    cm_in_inch2 = 'сантиметра в дюймах ='
    cm_in_inch3 = 'сантиметров в дюймах ='

    cm_in_dm1 = 'сантиметр в дециметрах ='
    cm_in_dm2 = 'сантиметра в дециметрах ='
    cm_in_dm3 = 'сантиметров в дециметрах ='

    cm_in_m1 = 'сантиметр в метрах ='
    cm_in_m2 = 'сантиметра в метрах ='
    cm_in_m3 = 'сантиметров в метрах ='

    cm_in_km1 = 'сантиметр в километрах ='
    cm_in_km2 = 'сантиметра в километрах ='
    cm_in_km3 = 'сантиметров в километрах ='

    inch_in_mm1 = 'дюйм в миллиметрах ='
    inch_in_mm2 = 'дюйма в миллиметрах ='
    inch_in_mm3 = 'дюймов в миллиметрах ='

    inch_in_cm1 = 'дюйм в сантиметрах ='
    inch_in_cm2 = 'дюйма в сантиметрах ='
    inch_in_cm3 = 'дюймов в сантиметрах ='

    inch_in_dm1 = 'дюйм в дециметрах ='
    inch_in_dm2 = 'дюйма в дециметрах ='
    inch_in_dm2 = 'дюймов в дециметрах ='

    inch_in_m1 = 'дюйм в метрах ='
    inch_in_m2 = 'дюйма в метрах ='
    inch_in_m3 = 'дюймов в метрах ='

    inch_in_km1 = 'дюйм в километрах ='
    inch_in_km2 = 'дюйма в километрах ='
    inch_in_km3 = 'дюймов в километрах ='

    dm_in_mm1 = 'дециметр в миллиметрах ='
    dm_in_mm2 = 'дециметра в миллиметрах ='
    dm_in_mm3 = 'дециметров в миллиметрах ='

    dm_in_cm1 = 'дециметр в сантиметрах ='
    dm_in_cm2 = 'дециметра в сантиметрах ='
    dm_in_cm3 = 'дециметров в сантиметрах ='

    dm_in_inch1 = 'дециметр в дюймах ='
    dm_in_inch2 = 'дециметра в дюймах ='
    dm_in_inch3 = 'дециметров в дюймах ='

    dm_in_m1 = 'дециметр в метрах ='
    dm_in_m2 = 'дециметра в метрах ='
    dm_in_m3 = 'дециметров в метрах ='

    dm_in_km1 = 'дециметр в километрах ='
    dm_in_km2 = 'дециметра в километрах ='
    dm_in_km3 = 'дециметров в километрах ='

    m_in_mm1 = 'метр в миллиметрах ='
    m_in_mm2 = 'метра в миллиметрах ='
    m_in_mm3 = 'метров в миллиметрах ='

    m_in_cm1 = 'метр в сантиметрах ='
    m_in_cm2 = 'метра в сантиметрах ='
    m_in_cm3 = 'метров в сантиметрах ='

    m_in_inch1 = 'метр в дюймах ='
    m_in_inch2 = 'метра в дюймах ='
    m_in_inch3 = 'метров в дюймах ='

    m_in_dm1 = 'метр в дециметрах ='
    m_in_dm2 = 'метра в дециметрах ='
    m_in_dm3 = 'метров в дециметрах ='

    m_in_km1 = 'метр в километрах ='
    m_in_km2 = 'метра в километрах ='
    m_in_km3 = 'метров в километрах ='

    km_in_mm1 = 'километр в миллиметрах ='
    km_in_mm2 = 'километра в миллиметрах ='
    km_in_mm3 = 'километров в миллиметрах ='

    km_in_cm1 = 'километр в сантиметрах='
    km_in_cm2 = 'километра в сантиметрах='
    km_in_cm3 = 'километров в сантиметрах='

    km_in_inch1 = 'километр в дюймах ='
    km_in_inch2 = 'километра в дюймах ='
    km_in_inch3 = 'километров в дюймах ='

    km_in_dm1 = 'километр в дециметрах ='
    km_in_dm2 = 'километра в дециметрах ='
    km_in_dm3 = 'километров в дециметрах ='

    km_in_m1 = 'километр в метрах ='
    km_in_m2 = 'километра в метрах ='
    km_in_m3 = 'километров в метрах ='

elif lang == 'en':
    length_unit_choose = 'Enter the measure of length to be converted (mm, cm, inch, dm, m, km): '

    measures_list = '''List of supported length measures:
    Millimeter: mm
    Centimeter: cm
    Inch: inch
    Decimeter: dm
    Meter: m
    Kilometer: km
    '''

    input_length_in_mm = 'Enter the length in millimeters: '
    input_length_in_cm = 'Enter the length in centimeters: '
    input_length_in_inch = 'Enter the length in inches: '
    input_length_in_dm = 'Enter the length in decimeters: '
    input_length_in_m = 'Enter the length in meters:'
    input_length_in_km = 'Enter the length in kilometers: '

    mm_in_cm1 = 'millimeter to centimeters = '
    mm_in_cm2 = 'millimeters to centimeters = '
    mm_in_cm3 = 'millimeters to centimeters = '

    mm_in_inch1 = 'millimeter to inches ='
    mm_in_inch2 = 'millimeters to inches ='
    mm_in_inch1 = 'millimeters to inches ='

    mm_in_dm1 = 'millimeter to decimeters ='
    mm_in_dm2 = 'millimeters to decimeters ='
    mm_in_dm3 = 'millimeters to decimeters ='

    mm_in_m1 = 'millimeter to meters ='
    mm_in_m2 = 'millimeters to meters ='
    mm_in_m3 = 'millimeters to meters ='

    cm_in_mm1 = 'centimeter to millimeters ='
    cm_in_mm2 = 'centimeters to millimeters ='
    cm_in_mm3 = 'centimeters to millimeters ='

    cm_in_inch1 = 'centimeter to inches ='
    cm_in_inch2 = 'centimeters to inches ='
    cm_in_inch3 = 'centimeters to inches ='

    cm_in_dm1 = 'centimeter to decimeters ='
    cm_in_dm2 = 'centimeters to decimeters ='
    cm_in_dm3 = 'centimeters to decimeters ='

    cm_in_m1 = 'centimeter to meters ='
    cm_in_m2 = 'centimeters to meters ='
    cm_in_m3 = 'centimeters to meters ='

    cm_in_km1 = 'centimeter to kilometers ='
    cm_in_km2 = 'centimeters to kilometers ='
    cm_in_km3 = 'centimeters to kilometers ='

    inch_in_mm1 = 'inch to millimeters ='
    inch_in_mm2 = 'inches to millimeters ='
    inch_in_mm3 = 'inches to millimeters ='

    inch_in_cm1 = 'inch to centimeters ='
    inch_in_cm2 = 'inches to centimeters ='
    inch_in_cm3 = 'inches to centimeters ='

    inch_in_dm1 = 'inches to decimeters ='
    inch_in_dm2 = 'inches to decimeters ='
    inch_in_dm3 = 'inches to decimeters ='

    inch_in_m1 = 'inch to meters ='
    inch_in_m2 = 'inches to meters ='
    inch_in_m3 = 'inches to meters ='

    inch_in_km1 = 'inch to kilometers ='
    inch_in_km2 = 'inches to kilometers ='
    inch_in_km3 = 'inches to kilometers ='

    dm_in_mm1 = 'decimeter to millimeters ='
    dm_in_mm2 = 'decimeters to millimeters ='
    dm_in_mm3 = 'decimeters to millimeters ='

    dm_in_cm1 = 'decimeter to centimeters ='
    dm_in_cm2 = 'decimeters to centimeters ='
    dm_in_cm3 = 'decimeters to centimeters ='

    dm_in_inch1 = 'decimeter to inches ='
    dm_in_inch2 = 'decimeters to inches ='
    dm_in_inch3 = 'decimeters to inches ='

    dm_in_m1 = 'decimeter to meters ='
    dm_in_m2 = 'decimeters to meters ='
    dm_in_m3 = 'decimeters to meters ='

    dm_in_km1 = 'decimeter to kilometers ='
    dm_in_km2 = 'decimeters to kilometers ='
    dm_in_km3 = 'decimeters to kilometers ='

    m_in_mm1 = 'meter to millimeters ='
    m_in_mm2 = 'meters to millimeters ='
    m_in_mm3 = 'meters to millimeters ='

    m_in_cm1 = 'meter to centimeters ='
    m_in_cm2 = 'meters to centimeters ='
    m_in_cm3 = 'meters to centimeters ='

    m_in_inch1 = 'meter to inches ='
    m_in_inch2 = 'meters to inches ='
    m_in_inch3 = 'meters to inches ='

    m_in_dm1 = 'meter to decimeters ='
    m_in_dm2 = 'meters to decimeters ='
    m_in_dm3 = 'meters to decimeters ='

    m_in_km1 = 'meter to kilometers ='
    m_in_km2 = 'meters to kilometers ='
    m_in_km3 = 'meters to kilometers ='

    km_in_mm1 = 'kilometer to millimeters ='
    km_in_mm2 = 'kilometers to millimeters ='
    km_in_mm3 = 'kilometers to millimeters ='

    km_in_cm1 = 'kilometer to centimeters='
    km_in_cm2 = 'kilometers to centimeters='
    km_in_cm3 = 'kilometers to centimeters='

    km_in_inch1 = 'kilometer to inches ='
    km_in_inch2 = 'kilometers to inches ='
    km_in_inch3 = 'kilometers to inches ='

    km_in_dm1 = 'kilometer to decimeters ='
    km_in_dm2 = 'kilometers to decimeters ='
    km_in_dm3 = 'kilometers to decimeters ='

    km_in_m1 = 'kilometer to meters ='
    km_in_m2 = 'kilometers to meters ='
    km_in_m3 = 'kilometers to meters ='