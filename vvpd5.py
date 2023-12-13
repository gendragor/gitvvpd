"""Преобразование полной строки в сжатую и наоборот"""


def input_string():
    """
    Функция для ввода строки.

    Фукнция, которая возращает введенную пользователем строку.
    Нельзя вводить строку, состоящую только из чисел.

    Args: None

    Returns:
        Строка символов

    Raises:
        TypeError, ValueError

    Examples:
        >>> input_string()
        Введите строку символов: aaaa
        "aaaa"

        >>> input_string()
        Введите строку символов: 123
        Traceback (most recent call last):
        ...
        TypeError: object of type 'int' has no len()
    """

    while True:
        print('Введите строку символов:')
        string = input()
        try:
            len(int(string))
        except TypeError:
            print('НЕЛЬЗЯ ВВОДИТЬ СТРОКУ ТОЛЬКО ИЗ ЧИСЕЛ')
        except ValueError:
            return string


def compression(string1):
    """
    Функция, которая преобразует обычную строку в сжатую строку.

    Данная фукнция принимает на вход какую-то строку,
    состоящую из любых символов, если в строке идут
    несколько повторяющийхся подряд символов, то сжимает их,
    оставляя один символ, а после него число повторений.

    Args:
        string1: Строка символов

    Returns:
        Сжатая строка

    Examples:
        >>>compression('aaadd')
        "a3d2"

        >>>compression('adfg')
        "adfg"
    """

    if len(string1) == 1:
        return string1
    new_string = ''
    el_string_before = string1[0]
    count_el_string = 1
    for i in range(1, len(string1)):
        if el_string_before == string1[i]:
            count_el_string += 1
        else:
            if count_el_string == 1:
                new_string += el_string_before
            else:
                new_string += el_string_before + str(count_el_string)
            count_el_string = 1
        el_string_before = string1[i]
    if count_el_string == 1:
        new_string += string1[i]
    else:
        new_string += string1[i] + str(count_el_string)
    return new_string


def decompression(string2):
    """
    Преобразование сжатой строки в полную.

    Данная фукнция принимает на вход какую-то строку,
    состоящую из любых символов, если в строке идет сначала символ,
    а затем число, то символ записывается столько раз подряд,
    сколько указано в числе.

    Args:
        string2: Строка символов

    Returns:
        Сжатая строка

    Examples:
        >>>decompression('a3d2')
        "aaad2"

        >>>decompression('ads')
        "ads"
    """

    new_string = ''
    number_el_string2 = ''
    symbol_el_string2 = ''
    el_string_before = string2[0]
    for i in range(1, len(string2)):
        if el_string_before < '0' or el_string_before > '9':
            if symbol_el_string2 != '' and number_el_string2 != '':
                new_string += symbol_el_string2 * int(number_el_string2)
                symbol_el_string2 = ''
                number_el_string2 = ''
            if '0' <= string2[i] <= '9':
                symbol_el_string2 = el_string_before
            else:
                new_string += el_string_before

        else:
            number_el_string2 += el_string_before
        el_string_before = string2[i]
    if string2[i] < '0' or string2[i] > '9':
        new_string += symbol_el_string2 * int(number_el_string2)
        new_string += string2[i]
    else:
        number_el_string2 += string2[i]
        new_string += symbol_el_string2 * int(number_el_string2)
    return new_string


if __name__ == '__main__':

    print('СПИСОК КОМАНД')
    print('Введите >1< : Сокращение строки')
    print('Введите >2< : Преобразование сжатой строки в полную')
    print('Введите >3< : Вывести меню')
    print('Введите >4< : Выход из программы')
    while True:
        command = input('Введите команду: ')
        if command == '1':
            print(f'Сокращенная строка: \n'
                  f'{compression(input_string())}')
        elif command == '2':
            print(f'Полная строка: \n'
                  f'{decompression(input_string())}')
        elif command == '3':
            print('Введите 1: Сокращение строки')
            print('Введите 2: Преобразование сжатой строки в полную')
            print('Введите 3: Вывести меню')
            print('Введите 4: Выход из программы')
        elif command == '4':
            print('<Вы вышли из программы>')
            break
        else:
            print("НЕПРАВИЛЬНАЯ КОМАНДА")
            print('Введите 1: Сокращение строки')
            print('Введите 2: Преобразование сжатой строки в полную')
            print('Введите 3: Вывести меню')
            print('Введите 4: Выход из программы')
            continue
