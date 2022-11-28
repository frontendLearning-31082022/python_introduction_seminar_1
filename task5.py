import main


# 5) Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

def run():
    main.print_console("Input benefit of company")
    benefit = int(main.input_int(False))

    main.print_console("Input costs of company")
    costs = int(main.input_int(False))

    main.print_console(benefit > costs and "Benefits more than costs" or
                       "Costs more than benefit")

    if benefit > costs:
        profitability = (benefit - costs) / benefit
        main.print_console("profitability " + str(profitability))

    main.print_console("How many people at co?")
    people_count = int(main.input_int(True))
    main.print_console("Profitability on one employ "
                       + str(benefit / people_count))
