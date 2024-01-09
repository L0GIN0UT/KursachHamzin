def sortByFormFirst(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[1] == "Овал" and choice == 1:
            newArrOfCameras.append(man)
        if man[1] == "Зауженный овал" and choice == 2:
            newArrOfCameras.append(man)
        if man[1] == "Стилет" and choice == 3:
            newArrOfCameras.append(man)
        if man[1] == "Пика" and choice == 4:
            newArrOfCameras.append(man)
        if man[1] == "Стрела" and choice == 5:
            newArrOfCameras.append(man)
        if man[1] == "Манила" and choice == 6:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByFormSecond(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[1] == "Эйдж" and choice == 1:
            newArrOfCameras.append(man)
        if man[1] == "Скошенная" and choice == 2:
            newArrOfCameras.append(man)
        if man[1] == "Миндаль" and choice == 3:
            newArrOfCameras.append(man)
        if man[1] == "Острый квадрат" and choice == 4:
            newArrOfCameras.append(man)
        if man[1] == "Мягкий квадрат" and choice == 5:
            newArrOfCameras.append(man)
        if man[1] == "Балерина" and choice == 6:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByColorsFirst(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[2] == "Прозрачный" and choice == 1:
            newArrOfCameras.append(man)
        elif man[2] == "Белый" and choice == 2:
            newArrOfCameras.append(man)
        elif man[2] == "Черный" and choice == 3:
            newArrOfCameras.append(man)
        elif man[2] == "Красный" and choice == 4:
            newArrOfCameras.append(man)
        elif man[2] == "Розовый" and choice == 5:
            newArrOfCameras.append(man)
        elif man[2] == "Оранжевый" and choice == 6:
            newArrOfCameras.append(man)
        elif man[2] == "Желтый" and choice == 7:
            newArrOfCameras.append(man)
        elif man[2] == "Зеленый" and choice == 8:
            newArrOfCameras.append(man)
        elif man[2] == "Голубой" and choice == 9:
            newArrOfCameras.append(man)
        elif man[2] == "Синий" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByColorsSecond(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[2] == "Фиолетовый" and choice == 1:
            newArrOfCameras.append(man)
        elif man[2] == "Бежевый" and choice == 2:
            newArrOfCameras.append(man)
        elif man[2] == "Коричневый" and choice == 3:
            newArrOfCameras.append(man)
        elif man[2] == "Серый" and choice == 4:
            newArrOfCameras.append(man)
        elif man[2] == "Серебряный" and choice == 5:
            newArrOfCameras.append(man)
        elif man[2] == "Золотой" and choice == 6:
            newArrOfCameras.append(man)
        elif man[2] == "Металлический" and choice == 7:
            newArrOfCameras.append(man)
        elif man[2] == "Мятный" and choice == 8:
            newArrOfCameras.append(man)
        elif man[2] == "Лаймовый" and choice == 9:
            newArrOfCameras.append(man)
        elif man[2] == "Сливовый" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByColorsThird(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[2] == "Бордовый" and choice == 1:
            newArrOfCameras.append(man)
        elif man[2] == "Пурпурный" and choice == 2:
            newArrOfCameras.append(man)
        elif man[2] == "Бирюзовый" and choice == 3:
            newArrOfCameras.append(man)
        elif man[2] == "Индиго" and choice == 4:
            newArrOfCameras.append(man)
        elif man[2] == "Сиреневый" and choice == 5:
            newArrOfCameras.append(man)
        elif man[2] == "Персиковый" and choice == 6:
            newArrOfCameras.append(man)
        elif man[2] == "Малиновый" and choice == 7:
            newArrOfCameras.append(man)
        elif man[2] == "Коралловый" and choice == 8:
            newArrOfCameras.append(man)
        elif man[2] == "Морская волна" and choice == 9:
            newArrOfCameras.append(man)
        elif man[2] == "Аквамариновый" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByLength(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[3] == "Короткая" and choice == 1:
            newArrOfCameras.append(man)
        elif man[3] == "Длинная" and choice == 2:
            newArrOfCameras.append(man)
        elif man[3] == "Средняя" and choice == 3:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByDesignFirst(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[4] == "Глянцевый маникюр" and choice == 1:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с рисунком" and choice == 2:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с блестками" and choice == 3:
            newArrOfCameras.append(man)
        elif man[4] == "Нежный маникюр" and choice == 4:
            newArrOfCameras.append(man)
        elif man[4] == "Однотонный маникюр" and choice == 5:
            newArrOfCameras.append(man)
        elif man[4] == "Элегантный маникюр" and choice == 6:
            newArrOfCameras.append(man)
        elif man[4] == "Матовый маникюр" and choice == 7:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр со стразами" and choice == 8:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр со слайдерами" and choice == 9:
            newArrOfCameras.append(man)
        elif man[4] == "Френч маникюр" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByDesignSecond(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[4] == "Цветочный маникюр" and choice == 1:
            newArrOfCameras.append(man)
        elif man[4] == "Школьный маникюр" and choice == 2:
            newArrOfCameras.append(man)
        elif man[4] == "Летний маникюр" and choice == 3:
            newArrOfCameras.append(man)
        elif man[4] == "Деловой маникюр" and choice == 4:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с полосками" and choice == 5:
            newArrOfCameras.append(man)
        elif man[4] == "Трендовый маникюр" and choice == 6:
            newArrOfCameras.append(man)
        elif man[4] == "Праздничный маникюр" and choice == 7:
            newArrOfCameras.append(man)
        elif man[4] == "Весенний маникюр" and choice == 8:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с градиентом" and choice == 9:
            newArrOfCameras.append(man)
        elif man[4] == "Абстрактный маникюр" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByDesignThird(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[4] == "Геометрический маникюр" and choice == 1:
            newArrOfCameras.append(man)
        elif man[4] == "Контрастный маникюр" and choice == 2:
            newArrOfCameras.append(man)
        elif man[4] == "Зимний маникюр" and choice == 3:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с надписями" and choice == 4:
            newArrOfCameras.append(man)
        elif man[4] == "Новогодний маникюр" and choice == 5:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с втиркой" and choice == 6:
            newArrOfCameras.append(man)
        elif man[4] == "Классический маникюр" and choice == 7:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с камифубуки" and choice == 8:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр кошачий глаз" and choice == 9:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с фольгой" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByDesignFourth(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[4] == "Осенний маникюр" and choice == 1:
            newArrOfCameras.append(man)
        elif man[4] == "Мультяшный маникюр" and choice == 2:
            newArrOfCameras.append(man)
        elif man[4] == "Камуфляж маникюр" and choice == 3:
            newArrOfCameras.append(man)
        elif man[4] == "Полупрозрачный маникюр" and choice == 4:
            newArrOfCameras.append(man)
        elif man[4] == "Мраморный маникюр" and choice == 5:
            newArrOfCameras.append(man)
        elif man[4] == "Лунный маникюр" and choice == 6:
            newArrOfCameras.append(man)
        elif man[4] == "Стемпинг маникюр" and choice == 7:
            newArrOfCameras.append(man)
        elif man[4] == "Леопардовый маникюр" and choice == 8:
            newArrOfCameras.append(man)
        elif man[4] == "Песочный маникюр" and choice == 9:
            newArrOfCameras.append(man)
        elif man[4] == "Морской маникюр" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByDesignFifth(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[4] == "Акварельный маникюр" and choice == 1:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр с лепкой" and choice == 2:
            newArrOfCameras.append(man)
        elif man[4] == "Свадебный маникюр" and choice == 3:
            newArrOfCameras.append(man)
        elif man[4] == "Bubble маникюр" and choice == 4:
            newArrOfCameras.append(man)
        elif man[4] == "Кружевной маникюр" and choice == 5:
            newArrOfCameras.append(man)
        elif man[4] == "Космический маникюр" and choice == 6:
            newArrOfCameras.append(man)
        elif man[4] == "Прозрачный маникюр" and choice == 7:
            newArrOfCameras.append(man)
        elif man[4] == "Вязаный маникюр" and choice == 8:
            newArrOfCameras.append(man)
        elif man[4] == "Этнический маникюр" and choice == 9:
            newArrOfCameras.append(man)
        elif man[4] == "Маникюр битое стекло" and choice == 10:
            newArrOfCameras.append(man)
    return newArrOfCameras

def sortByStickers(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[5] == "Да" and choice == 1:
            newArrOfCameras.append(man)
        elif man[5] == "Нет" and choice == 2:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByMaterial(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[6] == "Акрил" and choice == 1:
            newArrOfCameras.append(man)
        elif man[6] == "Гель-лак" and choice == 2:
            newArrOfCameras.append(man)
        elif man[6] == "Шеллак" and choice == 3:
            newArrOfCameras.append(man)
        elif man[6] == "Гель" and choice == 4:
            newArrOfCameras.append(man)
        elif man[6] == "Биогель" and choice == 5:
            newArrOfCameras.append(man)
        elif man[6] == "Полигель" and choice == 5:
            newArrOfCameras.append(man)
    return newArrOfCameras


def sortByPrice(choice, manic):
    newArrOfCameras = []
    for man in manic:
        if man[7] >= 10000 and choice == 1:
            newArrOfCameras.append(man)
        elif man[7] >= 15000 and choice == 2:
            newArrOfCameras.append(man)
        elif man[7] >= 20000 and choice == 3:
            newArrOfCameras.append(man)
        elif man[7] >= 25000 and choice == 4:
            newArrOfCameras.append(man)
    return newArrOfCameras
