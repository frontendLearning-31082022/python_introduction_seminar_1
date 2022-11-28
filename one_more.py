# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли
# этот день выходным.
import main


# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def run():
    main.print_console("Input number of week day")
    number_inputed = int(main.input_day_of_week())
    result = (number_inputed < 6) and "It's not weekend" or "It's weekend!"
    main.print_console(result)
