# Objective: to develop a length measure converter.

import localization as lc       # Import localization packages from "localization.py".

lc.lang = str()        # Language selection.

print(lc.measures_list)  # Print The list of supported measures of length.

length_unit = input(lc.length_unit_choose)  # Choice of measures of length.

if length_unit == 'mm':
    length = int(input(lc.input_length_in_mm))

    if length == 1:
        print(length, lc.mm_in_cm1, length * 0.1)
        print(length, lc.mm_in_inch1, length * 0.039)
        print(length, lc.mm_in_dm1, length * 0.01)
        print(length, lc.mm_in_m1, length * 0.001)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.mm_in_cm2, length * 0.1)
        print(length, lc.mm_in_inch2, length * 0.039)
        print(length, lc.mm_in_dm2, length * 0.01)
        print(length, lc.mm_in_m2, length * 0.001)

    else:
        print(length, lc.mm_in_cm3, length * 0.1)
        print(length, lc.mm_in_inch3,  length * 0.039)
        print(length, lc.mm_in_dm3,  length * 0.01)
        print(length, lc.mm_in_m3,  length * 0.001)

if length_unit == 'cm':
    length = int(input(lc.input_length_in_cm))

    if length == 1:
        print(length, lc.cm_in_mm1, length * 10)
        print(length, lc.cm_in_inch1, length * 0.39)
        print(length, lc.cm_in_dm1, length * 0.1)
        print(length, lc.cm_in_m1, length * 0.01)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.cm_in_mm2, length * 10)
        print(length, lc.cm_in_inch2, length * 0.39)
        print(length, lc.cm_in_dm2, length * 0.1)
        print(length, lc.cm_in_m2, length * 0.01)

    else:
        print(length, lc.cm_in_mm3, length * 10)
        print(length, lc.cm_in_inch3, length * 0.3937)
        print(length, lc.cm_in_dm3, length * 0.1)
        print(length, lc.cm_in_m1, length * 0.01)
        print(length, lc.cm_in_km3, length * 0.00001)

if length_unit == 'inch':
    length = int(input(lc.input_length_in_inch))

    if length == 1:
        print(length, lc.inch_in_mm1, length * 25.4)
        print(length, lc.inch_in_cm1, length * 2.54)
        print(length, lc.inch_in_dm1, length * 0.254)
        print(length, lc.inch_in_m1, length * 0.0254)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.inch_in_mm2, length * 25.4)
        print(length, lc.inch_in_cm2, length * 2.54)
        print(length, lc.inch_in_dm2, length * 0.254)
        print(length, lc.inch_in_m2, length * 0.0254)

    else:
        print(length, lc.inch_in_mm3, length * 25.4)
        print(length, lc.inch_in_cm3, length * 2.54)
        print(length, lc.inch_in_dm3, length * 0.254)
        print(length, lc.inch_in_m3, length * 0.0254)
        print(length, lc.inch_in_km3, length * 0.000025)

if length_unit == 'dm':
    length = int(input(lc.input_length_in_dm))

    if length == 1:
        print(length, lc.dm_in_mm1, length * 100)
        print(length, lc.dm_in_cm1, length * 10)
        print(length, lc.dm_in_inch1, length * 3.94)
        print(length, lc.dm_in_m1, length * 0.1)
        print(length, lc.dm_in_km1, length * 0.0001)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.dm_in_mm2, length * 100)
        print(length, lc.dm_in_cm2, length * 10)
        print(length, lc.dm_in_inch2, length * 3.94)
        print(length, lc.dm_in_m2, length * 0.1)
        print(length, lc.dm_in_km2, length * 0.0001)

    else:
        print(length, lc.dm_in_mm3, length * 100)
        print(length, lc.dm_in_cm3, length * 10)
        print(length, lc.dm_in_inch3, length * 3.94)
        print(length, lc.dm_in_m3, length * 0.1)
        print(length, lc.dm_in_km3, length * 0.0001)

if length_unit == 'm':
    length = int(input(lc.input_length_in_m))

    if length == 1:
        print(length, lc.m_in_mm1, length * 1000)
        print(length, lc.m_in_cm1, length * 100)
        print(length, lc.m_in_inch1, length * 39.4)
        print(length, lc.m_in_dm1, length * 10)
        print(length, lc.m_in_km1, length * 0.001)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.m_in_mm2, length * 1000)
        print(length, lc.m_in_cm2, length * 100)
        print(length, lc.m_in_inch2, length * 39.4)
        print(length, lc.m_in_dm2, length * 10)
        print(length, lc.m_in_km2, length * 0.001)

    else:
        print(length, lc.m_in_mm3, length * 1000)
        print(length, lc.m_in_cm3, length * 100)
        print(length, lc.m_in_inch3, length * 39.4)
        print(length, lc.m_in_dm3, length * 10)
        print(length, lc.m_in_km3, length * 0.001)

if length_unit == 'km':
    length = int(input(lc.input_length_in_km))

    if length == 1:
        print(length, lc.km_in_mm1, length * 1000000)
        print(length, lc.km_in_cm1, length * 100000)
        print(length, lc.km_in_inch1, length * 39370)
        print(length, lc.km_in_dm1, length * 10000)
        print(length, lc.km_in_m1, length * 1000)

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.km_in_mm2, length * 1000000)
        print(length, lc.km_in_cm2, length * 100000)
        print(length, lc.km_in_inch2, length * 39370)
        print(length, lc.km_in_dm2, length * 10000)
        print(length, lc.km_in_m2, length * 1000)

    else:
        print(length, lc.km_in_mm3, length * 1000000)
        print(length, lc.km_in_cm3, length * 100000)
        print(length, lc.km_in_inch3, length * 39370)
        print(length, lc.km_in_dm3, length * 10000)
        print(length, lc.km_in_m3, length * 1000)