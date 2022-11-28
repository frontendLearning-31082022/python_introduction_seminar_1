import main


# 6) Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

def run():
    first_day_km = None
    need_get_km = None
    current_km_walked = 0

    main.print_console("Input KM on first day pls")
    first_day_km = int(main.input_int(True))

    main.print_console("Input what KM need to get")
    need_get_km = int(main.input_int(True))

    current_km_walked = first_day_km;
    main.print_console("1 days gone. KM getted "
                       + str('{:.2f}'.format(current_km_walked)))

    days_gone = 1
    while (current_km_walked < need_get_km):
        days_gone += 1
        current_km_walked = current_km_walked + current_km_walked * 0.1
        main.print_console(str(days_gone) + " days gone. KM getted "
                           + str('{:.2f}'.format(current_km_walked)))

    main.print_console("Finished. " + str(need_get_km) + "KM getted in "
                       + str(days_gone) + " days")
