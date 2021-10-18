from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from lab_python_oop.figure import Figure

from colorama import Fore, Back, Style

def get_colorText():
    print(Fore.RED + 'красный текст')
    print(Back.GREEN + 'зеленый фон')
    print(Style.RESET_ALL)
    print('Обычный текст')

def main():
    r = Rectangle("синего", 11, 11)
    c = Circle("зеленого", 11)
    s = Square("красного", 11)
    f= Figure()
    print(r)
    print(c)
    print(s)

    get_colorText()

if __name__ == "__main__":
    main()