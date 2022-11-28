# This is a sample Python script.
import main
import one_more
import one_more_2
import one_more_3
import task1
import task2
import task3
import task4
import task5
import re
import task6

if __name__ == '__main__':
    one_more_3.run()
    # one_more_2.run()
    # one_more.run()
    # task6.run()
    # task5.run()
    # task4.run()
    # task3.task3()
    # task2.task2()
    #  task1.task1()

def input_string():
    inputed = input()
    return inputed


def input_int_not_zero(positive):
    # where my method overload? o rly?
    not_zero = True
    while (not_zero):
        inputed_now = input_int(positive)
        not_zero = inputed_now == 0
    return inputed_now


def input_int(positive_only):
    while True:
        inputed = input()
        result = re.findall(r'\D', inputed)
        result = list(filter(lambda x: not (str(x).__eq__("-")), result))
        result = list(filter(lambda x: not (str(x).__eq__(",")), result))
        result = list(filter(lambda x: not (str(x).__eq__(".")), result))
        corrected_input = len(result) == 0
        if (positive_only and corrected_input):
            corrected_input = int(inputed) > -1
        if corrected_input:
            break
        main.print_console("Input integer again")

    inputed = int(inputed)
    return inputed


def input_day_of_week():
    while True:
        inputed = input()
        result = re.findall(r'\D', inputed)
        corrected_input = len(result) == 0
        if (corrected_input and int(corrected_input) < 8 > 0):
            break
        main.print_console("Input integer for day of week again")

    inputed = int(inputed)
    return inputed


def print_console(textt=''):
    print(textt)

    # sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
    # print(textt.decode('utf-8'))
    # sys.setdefaultencoding("utf-8")
    # print(textt)
    #  print(textt.encode('cp1251'))
