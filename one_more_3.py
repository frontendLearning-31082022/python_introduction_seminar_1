# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

import main


def run():
    main.print_console("Input x coord point 1")
    x_coord1 = main.input_int(False)

    main.print_console("Input y coord point 1")
    y_coord1 = main.input_int(False)

    main.print_console("Input x coord point 2")
    x_coord2 = main.input_int(False)

    main.print_console("Input y coord point 2")
    y_coord2 = main.input_int(False)

    d = (x_coord2 - x_coord1) ** 2 + (y_coord2 - y_coord1) ** 2
    d = math.sqrt(d)

    main.print_console("Distance between " + str('{:.2f}'.format(d)))
