# Length converter v1.
# Objective: to develop a length measure converter.

import localization as lc                                   # Import localization packages from "localization.py".

lc.lang = str()                                             # Language selection.

print(lc.measures_list)                                     # Print The list of supported measures of length.

length_unit = input(lc.length_unit_choose)                  # Choice of measures of length.

if length_unit == 'mm':
    length = int(input(lc.input_length_in_mm))              # Enter a length in millimeters.

    if length == 1:
        print(length, lc.mm_in_cm1, length * 0.1)           # Сonversion from millimeters to millimeters.
        print(length, lc.mm_in_inch1, length * 0.039)       # Сonversion from millimeters to inches.
        print(length, lc.mm_in_dm1, length * 0.01)          # Сonversion from millimeters to inches.
        print(length, lc.mm_in_m1, length * 0.001)          # Сonversion from millimeters to meters.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.mm_in_cm2, length * 0.1)           # Сonversion from millimeters to millimeters.
        print(length, lc.mm_in_inch2, length * 0.039)       # Сonversion from millimeters to inches.
        print(length, lc.mm_in_dm2, length * 0.01)          # Сonversion from millimeters to decimeters.
        print(length, lc.mm_in_m2, length * 0.001)          # Сonversion from millimeters to meters.

    else:
        print(length, lc.mm_in_cm3, length * 0.1)           # Сonversion from millimeters to millimeters.
        print(length, lc.mm_in_inch3, length * 0.039)       # Сonversion from millimeters to inches.
        print(length, lc.mm_in_dm3, length * 0.01)          # Сonversion from millimeters to decimeters.
        print(length, lc.mm_in_m3, length * 0.001)          # Сonversion from millimeters to meters.

if length_unit == 'cm':
    length = int(input(lc.input_length_in_cm))              # Enter a length in centimeters.

    if length == 1:
        print(length, lc.cm_in_mm1, length * 10)            # Сonversion from centimeters to millimeters.
        print(length, lc.cm_in_inch1, length * 0.39)        # Сonversion from centimeters to inches.
        print(length, lc.cm_in_dm1, length * 0.1)           # Сonversion from centimeters to decimeters.
        print(length, lc.cm_in_m1, length * 0.01)           # Сonversion from centimeters to meters.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.cm_in_mm2, length * 10)            # Сonversion from centimeters to millimeters.
        print(length, lc.cm_in_inch2, length * 0.39)        # Сonversion from centimeters to inches.
        print(length, lc.cm_in_dm2, length * 0.1)           # Сonversion from centimeters to meters.
        print(length, lc.cm_in_m2, length * 0.01)           # Сonversion from centimeters to kilometers.

    else:
        print(length, lc.cm_in_mm3, length * 10)            # Сonversion from centimeters to millimeters.
        print(length, lc.cm_in_inch3, length * 0.3937)      # Сonversion from centimeters to inches.
        print(length, lc.cm_in_dm3, length * 0.1)           # Сonversion from centimeters to decimeters.
        print(length, lc.cm_in_m1, length * 0.01)           # Сonversion from centimeters to meters.
        print(length, lc.cm_in_km3, length * 0.00001)       # Сonversion from centimeters to kilometers.

if length_unit == 'inch':
    length = int(input(lc.input_length_in_inch))            # Enter a length in inches.

    if length == 1:
        print(length, lc.inch_in_mm1, length * 25.4)        # Сonversion from inch to millimeters.
        print(length, lc.inch_in_cm1, length * 2.54)        # Сonversion from inch to centimeters.
        print(length, lc.inch_in_dm1, length * 0.254)       # Сonversion from inch to decimeters.
        print(length, lc.inch_in_m1, length * 0.0254)       # Сonversion from inch to meters.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.inch_in_mm2, length * 25.4)        # Сonversion from inches to millimeters.
        print(length, lc.inch_in_cm2, length * 2.54)        # Сonversion from inches to centimeters.
        print(length, lc.inch_in_dm2, length * 0.254)       # Сonversion from inches to decimeters.
        print(length, lc.inch_in_m2, length * 0.0254)       # Сonversion from inches to meters.

    else:
        print(length, lc.inch_in_mm3, length * 25.4)        # Сonversion from inches to millimeters.
        print(length, lc.inch_in_cm3, length * 2.54)        # Сonversion from inches to centimeters.
        print(length, lc.inch_in_dm3, length * 0.254)       # Сonversion from inches to decimeters.
        print(length, lc.inch_in_m3, length * 0.0254)       # Сonversion from inches to meters.
        print(length, lc.inch_in_km3, length * 0.000025)    # Сonversion from inches to kilometers.

if length_unit == 'dm':
    length = int(input(lc.input_length_in_dm))              # Enter a length in decimeters.

    if length == 1:
        print(length, lc.dm_in_mm1, length * 100)           # Сonversion from decimeter to millimeters.
        print(length, lc.dm_in_cm1, length * 10)            # Сonversion from decimeter to centimeters.
        print(length, lc.dm_in_inch1, length * 3.94)        # Сonversion from decimeter to inches.
        print(length, lc.dm_in_m1, length * 0.1)            # Сonversion from decimeter to meters.
        print(length, lc.dm_in_km1, length * 0.0001)        # Сonversion from decimeter to kilometers.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.dm_in_mm2, length * 100)           # Сonversion from decimeters to millimeters.
        print(length, lc.dm_in_cm2, length * 10)            # Сonversion from decimeters to centimeters.
        print(length, lc.dm_in_inch2, length * 3.94)        # Сonversion from decimeters to inches.
        print(length, lc.dm_in_m2, length * 0.1)            # Сonversion from decimeters to meters.
        print(length, lc.dm_in_km2, length * 0.0001)        # Сonversion from decimeters to kilometers.

    else:
        print(length, lc.dm_in_mm3, length * 100)           # Сonversion from decimeters to millimeters.
        print(length, lc.dm_in_cm3, length * 10)            # Сonversion from decimeters to centimeters.
        print(length, lc.dm_in_inch3, length * 3.94)        # Сonversion from decimeters to inches.
        print(length, lc.dm_in_m3, length * 0.1)            # Сonversion from decimeters to meters.
        print(length, lc.dm_in_km3, length * 0.0001)        # Сonversion from decimeters to kilometers.

if length_unit == 'm':
    length = int(input(lc.input_length_in_m))               # Enter a length in meters.

    if length == 1:
        print(length, lc.m_in_mm1, length * 1000)           # Сonversion from meter to millimeters.
        print(length, lc.m_in_cm1, length * 100)            # Сonversion from meter to centimeters.
        print(length, lc.m_in_inch1, length * 39.4)         # Сonversion from meter to inches.
        print(length, lc.m_in_dm1, length * 10)             # Сonversion from meter to decimeters.
        print(length, lc.m_in_km1, length * 0.001)          # Сonversion from meter to kilometers.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.m_in_mm2, length * 1000)           # Сonversion from meters to millimeters.
        print(length, lc.m_in_cm2, length * 100)            # Сonversion from meters to centimeters.
        print(length, lc.m_in_inch2, length * 39.4)         # Сonversion from meters to inches.
        print(length, lc.m_in_dm2, length * 10)             # Сonversion from meters to decimeters.
        print(length, lc.m_in_km2, length * 0.001)          # Сonversion from meters to kilometers.

    else:
        print(length, lc.m_in_mm3, length * 1000)           # Сonversion from meters to millimeters.
        print(length, lc.m_in_cm3, length * 100)            # Сonversion from meters to centimeters.
        print(length, lc.m_in_inch3, length * 39.4)         # Сonversion from meters to inches.
        print(length, lc.m_in_dm3, length * 10)             # Сonversion from meters to decimeters.
        print(length, lc.m_in_km3, length * 0.001)          # Сonversion from meters to kilometers.

if length_unit == 'km':
    length = int(input(lc.input_length_in_km))              # Enter a length in kilometers.

    if length == 1:
        print(length, lc.km_in_mm1, length * 1000000)       # Сonversion from kilometer to millimeters.
        print(length, lc.km_in_cm1, length * 100000)        # Сonversion from kilometer to centimeters.
        print(length, lc.km_in_inch1, length * 39370)       # Сonversion from kilometer to inches.
        print(length, lc.km_in_dm1, length * 10000)         # Сonversion from kilometer to decimeters.
        print(length, lc.km_in_m1, length * 1000)           # Сonversion from kilometer to meters.

    elif length == 2 or length == 3 or length == 4:
        print(length, lc.km_in_mm2, length * 1000000)       # Сonversion from kilometers to millimeters.
        print(length, lc.km_in_cm2, length * 100000)        # Сonversion from kilometers to centimeters.
        print(length, lc.km_in_inch2, length * 39370)       # Сonversion from kilometers to inches.
        print(length, lc.km_in_dm2, length * 10000)         # Сonversion from kilometers to decimeters.
        print(length, lc.km_in_m2, length * 1000)           # Сonversion from kilometers to meters.

    else:
        print(length, lc.km_in_mm3, length * 1000000)       # Сonversion from kilometers to millimeters.
        print(length, lc.km_in_cm3, length * 100000)        # Сonversion from kilometers to centimeters.
        print(length, lc.km_in_inch3, length * 39370)       # Сonversion from kilometers to inches.
        print(length, lc.km_in_dm3, length * 10000)         # Сonversion from kilometers to decimeters.
        print(length, lc.km_in_m3, length * 1000)           # Сonversion from kilometers to meters.