import time
from Menu import *
from Generate import *
from Sort import *


def show_all(manic):
    for man in manic:
        print()
        print("Наименование маникюра: " + man[0])
        print("Форма маникюра: " + man[1])
        print("Цвет маникюра: " + man[2])
        print("Длинна маникюра: " + man[3])
        print("Дизайн маникюра: " + man[4])
        print("Стикеры маникюра: " + man[5])
        print("Материал маникюра: " + man[6])
        print("Цена: " + str(man[7]) + " руб.")


def choice_of_person(choice, rest):
    print("")
    if choice == 1:
        clear()
        menuForFormFirst()
        time_freeze()
        a = check_input()
        if a < 7:
            rest = sortByFormFirst(a, rest)
        else:
            clear()
            menuForFormSecond()
            time_freeze()
            rest = sortByFormSecond(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 2:
        clear()
        menuForColorsFirst()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByColorsFirst(a, rest)
        else:
            clear()
            menuForColorsSecond()
            time_freeze()
            a = check_input()
            if a < 11:
                rest = sortByColorsSecond(a, rest)
            else:
                clear()
                menuForColorsThird()
                time_freeze()
                rest = sortByColorsThird(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 3:
        clear()
        menuForLength()
        sortByLength(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 4:
        clear()
        menuForDesignFirst()
        time_freeze()
        a = check_input()
        if a < 11:
            rest = sortByDesignFirst(a, rest)
        else:
            clear()
            menuForDesignSecond()
            time_freeze()
            a = check_input()
            if a < 11:
                rest = sortByDesignSecond(a, rest)
            else:
                clear()
                menuForDesignThird()
                time_freeze()
                a = check_input()
                if a < 11:
                    rest = sortByDesignThird(a, rest)
                else:
                    clear()
                    menuForDesignFourth()
                    time_freeze()
                    a = check_input()
                    if a < 11:
                        rest = sortByDesignFourth(a, rest)
                    else:
                        clear()
                        menuForDesignFifth()
                        time_freeze()
                        rest = sortByDesignFifth(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 5:
        clear()
        menuForStickers()
        time_freeze()
        rest = sortByStickers(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 6:
        clear()
        menuForMaterial()
        time_freeze()
        rest = sortByMaterial(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 7:
        clear()
        menuForPrice()
        time_freeze()
        rest = sortByPrice(check_input(), rest)
        check_res(rest)
        return rest
    elif choice == 8:
        clear()
        rest = Generate(1000)
        print("Характеристики были сброшены")
        time_freeze()
        return rest
    elif choice == 9:
        time_freeze()
        if check_res(rest):
            show_all(rest)
    elif choice == 10:
        exit()


def check_input():
    while True:
        a = input("Введите ваш ответ -> ")
        if a.isdigit():
            return int(a)


def check_res(rest):
    if len(rest) == 0:
        print("\nНа данный момент в нашем приложении")
        print("Нет того маникюра который вы предпочитаете")
        print("Попробуйте сбросить характеристики и изменить свой выбор")
        time.sleep(2)
    else:
        return rest


def main(gen_rest):
    print("Подбор маникюра")
    print("")
    rest = gen_rest
    while True:
        time_freeze()
        clear()
        print()
        menu()
        rest = choice_of_person(check_input(), rest)


def time_freeze():
    time.sleep(1)


def clear():
    print('\n'*80)


res = Generate(10000)
main(res)
