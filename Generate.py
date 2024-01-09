import random

name = ["Френч маникюр", "Лунный маникюр", "Омбре-маникюр", "Маникюр с геометрическими узорами",
        "Маникюр с животным принтом", "Маникюр с блестками", "Маникюр с мраморным эффектом",
        "Маникюр с цветочным дизайном", "Маникюр с фруктовым дизайном", "Маникюр с градиентом", "Маникюр с фольгой",
        "Маникюр с рисунком", "Маникюр с переливающимися лаками", "Маникюр с абстрактным дизайном",
        "Маникюр с геометрическими фигурами", "Маникюр с золотыми акцентами", "Маникюр с серебряными акцентами",
        "Маникюр с розовыми оттенками", "Маникюр с красными оттенками", "Маникюр с синими оттенками",
        "Маникюр с фиолетовыми оттенками", "Маникюр с зелеными оттенками", "Маникюр с оранжевыми оттенками",
        "Маникюр с коричневыми оттенками", "Маникюр с черным лаком", "Маникюр с белым лаком",
        "Маникюр с нюдовым оттенком", "Маникюр с пастельными оттенками", "Маникюр с яркими цветами",
        "Маникюр с пастельными цветами", "Маникюр с мятным оттенком", "Маникюр с лимонным оттенком",
        "Маникюр с малиновым оттенком", "Маникюр с оранжевым оттенком", "Маникюр с голубым оттенком",
        "Маникюр с фиолетовым оттенком", "Маникюр с персиковым оттенком", "Маникюр с розовым оттенком",
        "Маникюр с серым оттенком", "Маникюр с фуксией", "Маникюр с бирюзовым оттенком",
        "Маникюр с мятно-зеленым оттенком", "Маникюр с оливковым оттенком", "Маникюр с горчичным оттенком",
        "Маникюр с бежевым оттенком", "Маникюр с лавандовым оттенком", "Маникюр с бирюзовым лаком",
        "Маникюр с голографическим эффектом", "Маникюр с хромированным эффектом", "Маникюр с матовым покрытием",
        "Маникюр с глянцевым покрытием", "Маникюр с металлическим оттенком", "Маникюр с переливающимися пайетками",
        "Маникюр с камеями", "Маникюр с росписью", "Маникюр с декоративными стразами", "Маникюр с акварельным дизайном",
        "Маникюр с мраморной фактурой", "Маникюр с геометрическими рисунками",
        "Маникюр с акцентом на безымянном пальце",
        "Маникюр с акцентом на указательном пальце", "Маникюр с акцентом на среднем пальце",
        "Маникюр с акцентом на указательном и безымянном пальцах",
        "Маникюр с акцентом на указательном и среднем пальцах", "Маникюр с акцентом на безымянном и среднем пальцах",
        "Маникюр с акцентом на всех пальцах", "Маникюр с акцентами в форме сердечек",
        "Маникюр с акцентами в форме звезд", "Маникюр с акцентами в форме полос", "Маникюр с акцентами в форме точек",
        "Маникюр с акцентами в форме камней", "Маникюр с акцентами в форме лент", "Маникюр с акцентами в форме цветков",
        "Маникюр с акцентами в форме птиц", "Маникюр с акцентами в форме бабочек",
        "Маникюр с акцентами в форме листьев",
        "Маникюр с акцентами в форме фруктов", "Маникюр с акцентами в форме животных",
        "Маникюр с акцентами в форме символов", "Маникюр с акцентами в форме букв", "Маникюр с акцентами в форме цифр",
        "Маникюр с акцентами в форме геометрических фигур", "Маникюр с акцентами в форме абстрактных элементов",
        "Маникюр с акцентами в форме пайеток", "Маникюр с акцентами в форме страз",
        "Маникюр с акцентами в форме перьев",
        "Маникюр с акцентами в форме волнистых линий", "Маникюр с акцентами в форме глаз",
        "Маникюр с акцентами в форме губ", "Маникюр с акцентами в форме усов", "Маникюр с акцентами в форме капель",
        "Маникюр с акцентами в форме пятен", "Маникюр с акцентами в форме роз", "Маникюр с акцентами в форме бабочек",
        "Маникюр с акцентами в форме веток", "Маникюр с акцентами в форме флажков",
        "Маникюр с акцентами в форме сердец", "Маникюр с акцентами в форме знаков бесконечности",
        "Маникюр с акцентами в форме вензелей", "Маникюр с акцентами в форме плетения",
        "Маникюр с акцентами в форме бусин", "Маникюр с акцентами в форме паутинок", "Маникюр с акцентами в форме птиц",
        "Маникюр с акцентами в форме драгоценных камней", "Маникюр с акцентами в форме фруктов",
        "Маникюр с акцентами в форме символов", "Маникюр с акцентами в форме букв", "Маникюр с акцентами в форме цифр",
        "Маникюр с акцентами в форме геометрических фигур", "Маникюр с акцентами в форме абстрактных элементов",
        "Маникюр с акцентами в форме перьев", "Маникюр с акцентами в форме полос", "Маникюр с акцентами в форме глаз",
        "Маникюр с акцентами в форме губ", "Маникюр с акцентами в форме усов", "Маникюр с акцентами в форме капель",
        "Маникюр с акцентами в форме пятен", "Маникюр с акцентами в форме роз", "Маникюр с акцентами в форме бабочек",
        "Маникюр с акцентами в форме веток", "Маникюр с акцентами в форме флажков",
        "Маникюр с акцентами в форме сердец", "Маникюр с акцентами в форме знаков бесконечности",
        "Маникюр с акцентами в форме вензелей", "Маникюр с акцентами в форме плетения",
        "Маникюр с акцентами в форме бусин", "Маникюр с акцентами в форме паутинок", "Маникюр с акцентами в форме птиц",
        "Маникюр с акцентами в форме драгоценных камней", "Маникюр с акцентами в форме фруктов",
        "Маникюр с акцентами в форме символов", "Маникюр с акцентами в форме букв", "Маникюр с акцентами в форме цифр",
        "Маникюр с акцентами в форме геометрических фигур", "Маникюр с акцентами в форме абстрактных элементов",
        "Маникюр с акцентами в форме перьев", "Маникюр с акцентами в форме полос", "Маникюр с акцентами в форме глаз",
        "Маникюр с акцентами в форме губ", "Маникюр с акцентами в форме усов", "Маникюр с акцентами в форме капель",
        "Маникюр с акцентами в форме пятен", "Маникюр с акцентами в форме роз", "Маникюр с акцентами в форме бабочек",
        "Маникюр с акцентами в форме веток", "Маникюр с акцентами в форме флажков",
        "Маникюр с акцентами в форме сердец", "Маникюр с акцентами в форме знаков бесконечности",
        "Маникюр с акцентами в форме вензелей", "Маникюр с акцентами в форме плетения",
        "Маникюр с акцентами в форме бусин", "Маникюр с акцентами в форме паутинок", "Маникюр с акцентами в форме птиц",
        "Маникюр с акцентами в форме драгоценных камней", "Маникюр с акцентами в форме фруктов",
        "Маникюр с акцентами в форме символов", "Маникюр с акцентами в форме букв", "Маникюр с акцентами в форме цифр",
        "Маникюр с акцентами в форме геометрических фигур", "Маникюр с акцентами в форме абстрактных элементов",
        "Маникюр с акцентами в форме перьев", "Маникюр с акцентами в форме полос", "Маникюр с акцентами в форме глаз",
        "Маникюр с акцентами в форме губ", "Маникюр с акцентами в форме усов", "Маникюр с акцентами в форме капель",
        "Маникюр с акцентами в форме пятен", "Маникюр с акцентами в форме роз", "Маникюр с акцентами в форме бабочек",
        "Маникюр с акцентами в форме веток", "Маникюр с акцентами в форме флажков",
        "Маникюр с акцентами в форме сердец", "Маникюр с акцентами в форме знаков бесконечности",
        "Маникюр с акцентами в форме вензелей", "Маникюр с акцентами в форме плетения",
        "Маникюр с акцентами в форме бусин", "Маникюр с акцентами в форме паутинок", "Маникюр с акцентами в форме птиц",
        "Маникюр с акцентами в форме драгоценных камней", "Маникюр с акцентами в форме фруктов",
        "Маникюр с акцентами в форме символов", "Маникюр с акцентами в форме букв"]

form = ["Овал", "Зауженный овал", "Стилет", "Пика", "Стрела", "Манила", "Эйдж", "Скошенная", "Миндаль",
        "Острый квадрат", "Мягкий квадрат", "Балерина"]

colors = ['Прозрачный', 'Белый', 'Черный', 'Красный', 'Розовый', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий',
          'Фиолетовый', 'Бежевый', 'Коричневый', 'Серый', 'Серебряный', 'Золотой', 'Металлический', 'Мятный',
          'Лаймовый', 'Сливовый', 'Бордовый', 'Пурпурный', 'Бирюзовый', 'Индиго', 'Сиреневый', 'Персиковый',
          'Малиновый', 'Коралловый', 'Морская волна', 'Аквамариновый']

length = ["Короткая", "Длинная", "Средняя"]

design = ["Глянцевый маникюр", "Маникюр с рисунком", "Маникюр с блестками", "Нежный маникюр",
          "Однотонный маникюр", "Элегантный маникюр", "Матовый маникюр", "Маникюр со стразами", "Маникюр со слайдерами",
          "Френч маникюр", "Цветочный маникюр", "Школьный маникюр", "Летний маникюр", "Деловой маникюр",
          "Маникюр с полосками", "Трендовый маникюр", "Праздничный маникюр", "Весенний маникюр", "Маникюр с градиентом",
          "Абстрактный маникюр", "Геометрический маникюр", "Контрастный маникюр", "Зимний маникюр",
          "Маникюр с надписями", "Новогодний маникюр", "Маникюр с втиркой", "Классический маникюр",
          "Маникюр с камифубуки", "Маникюр кошачий глаз", "Маникюр с фольгой", "Осенний маникюр", "Мультяшный маникюр",
          "Камуфляж маникюр", "Полупрозрачный маникюр", "Мраморный маникюр", "Лунный маникюр", "Стемпинг маникюр",
          "Леопардовый маникюр", "Песочный маникюр", "Морской маникюр", "Акварельный маникюр", "Маникюр с лепкой",
          "Свадебный маникюр", "Bubble маникюр", "Кружевной маникюр", "Космический маникюр", "Прозрачный маникюр",
          "Вязаный маникюр", "Этнический маникюр", "Маникюр битое стекло"]

sticker = ["Да", "Нет"]

material = ['Акрил', 'Гель-лак', 'Шеллак', 'Гель', 'Биогель', 'Полигель']


def Generate(amount):
    mainArr = []
    while amount != 0:
        temp = []
        if len(name) > 0:
            temp.append(name[random.randint(0, len(form) - 1)])
        if len(form) > 0:
            temp.append(form[random.randint(0, len(form) - 1)])
        if len(colors) > 0:
            temp.append(colors[random.randint(0, len(colors) - 1)])
        if len(length) > 0:
            temp.append(length[random.randint(0, len(length) - 1)])
        if len(design) > 0:
            temp.append(design[random.randint(0, len(design) - 1)])
        if len(sticker) > 0:
            temp.append(sticker[random.randint(0, len(sticker) - 1)])
        if len(material) > 0:
            temp.append(material[random.randint(0, len(material) - 1)])
        temp.append(random.randint(50, 291) * 100)
        mainArr.append(temp)
        amount -= 1
    return mainArr