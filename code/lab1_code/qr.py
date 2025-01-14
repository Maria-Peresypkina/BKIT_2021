import sys
import math


def get_coef(index, prompt):
    global coef
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)

    # Переводим строку в действительное число
    while True:
        try:
            coef_str = input()
            coef = float(coef_str)
        except ValueError:
            print("Коэффицент не верный, повторите ввод")
            continue
        if index == 1 and coef == 0.0:
            print("Коэффицент не может равняться 0, повторите ввод")
        else:
            break
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)

        if root < 0:
            root = 0
        else:
            r1 = math.sqrt(root)
            r2 = - r1
            if r1 == r2:
                result.append(r1)
            else:
                result.append(r1)
                result.append(r2)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        if root1 < 0:
            root1 = 0
        else:
            r1 = math.sqrt(root1)
            r2 = - r1
            if r1 == r2:
                result.append(r1)
            else:
                result.append(r1)
                result.append(r2)
        if root2 < 0:
            root2 = 0
        else:
            r3 = math.sqrt(root2)
            r4 = - r3
            if r3 == r4:
                result.append(r3)
            else:
                result.append(r3)
                result.append(r4)
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()