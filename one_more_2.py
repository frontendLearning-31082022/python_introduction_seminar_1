# Напишите программу, которая принимает на вход
# координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# в этой четверти (x и y).
import main


def run():
    main.print_console("Enter x")
    x_val = main.input_int_not_zero(False)

    main.print_console("Enter y")
    y_val = main.input_int_not_zero(False)

    if x_val > 0 and y_val > 0:
        main.print_console("Point in 1 quart")
    elif x_val < 0 and y_val < 0:
        main.print_console("Point in 3 quart")
    elif x_val > 0 and y_val < 0:
        main.print_console("Point in 4 quart")
    elif x_val < 0 and y_val > 0:
        main.print_console("Point in 2 quart")
