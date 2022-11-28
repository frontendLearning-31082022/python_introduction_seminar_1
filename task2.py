import main


# 2) Пользователь вводит время в секундах. Переведите время в часы, минуты
# и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

def task2():
    secs_count = int(main.input_int(False))
    hours = int(secs_count / 60 / 60)
    minutes = int((secs_count - (hours * 60 * 60)) / 60)
    secs = secs_count - (hours * 60 * 60) - (minutes * 60)
    main.print_console('Result {:02}:{:02}:{:02}'.format(hours, minutes, secs))
