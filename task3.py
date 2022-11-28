import main


# 3) Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

def task3():
    int_input = int(main.input_int(False))
    string_this = str(int_input)
    list_nums = []
    for i in range(int_input):
        list_nums.append(string_this * (i + 1))
    result = 0
    for val in list_nums:
        result = result + int(val)
    main.print_console(result)
