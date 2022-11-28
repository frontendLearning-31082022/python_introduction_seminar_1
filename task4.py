import main


# 4) Пользователь вводит целое положительное число. Найдите самую большую
# цифру в числе.
# Для решения используйте цикл while и арифметические операции.

def run():
    int_positive = int(main.input_int(True))

    iter = len(str(int_positive)) - 1
    max_num = int(str(int_positive)[iter])

    while (iter > -1):
        char_current = str(int_positive)[iter]
        if int(char_current) > max_num:
            max_num = int(char_current)
        iter -= 1
    main.print_console("Max value in inputed number " + str(max_num))

    # for val in str(int_positive):
    #     if int(val)>max_num:
    #         max_num=int(val)
