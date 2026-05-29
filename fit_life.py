# Проект FitLife - MVP версия 1.0

# рекомендуемый объём воды в мл на кг веса
WATER_PER_KG = 30


def is_blank(user_input: str) -> bool:
    """
    Проверяет, пустая переданная строка или нет.

    :param user_input: Проверяемая строка
    :return: True, если строка пустая, иначе False
    """
    return user_input.strip() == ""


def is_float(user_input: str) -> bool:
    """
    Проверяет, преобразуется ли проверяемая
    строка в float

    :param user_input: Проверяемая строка
    :return: True, если строка float, иначе False
    """
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def is_int(user_input: str) -> bool:
    """
    Проверяет, преобразуется ли проверяемая
    строка в int

    :param input: Проверяемая строка
    :return: True, если строка может быть преобразована
    в int, иначе False
    """
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def get_user_name() -> str:
    """
    Приглашает пользователя ко вводу имени
    и сохраняет его в переменную.

    :return: Имя пользователя
    """
    name = input("Введите имя: ")
    # проверяем, что пользователь не передает пустую строку
    if is_blank(name):
        print("Вы ничего не ввели.")
        return get_user_name()
    return name


def get_user_age() -> int:
    """
    Приглашает пользователя ко вводу возраста
    и сохраняет его в переменную.

    :return: Возраст пользователя
    """
    age = input("Введите Ваш возраст в годах (например, 27): ")
    # проверяем, что пользователь не передает пустую строку
    if is_blank(age):
        print("Вы ничего не ввели.")
        return get_user_age()
    # проверяем, что передаваемое пользователем значение преобразуется в int
    if not is_int(age):
        print("Вы ввели возраст в неверном формате.")
        return get_user_age()
    return int(age)


def get_user_weight() -> float:
    """
    Запрашивает у пользователя вес в кг

    :return: Вес пользователя в кг
    """
    weight = input("Введите Ваш вес в килограммах, "
                   "например, 50.5 или 73: ")
    # проверяем, что пользователь не передает пустую строку
    if is_blank(weight):
        print("Вы ничего не ввели.")
        return get_user_weight()
    # проверяем, что передаваемое пользователем значение преобразуется в float
    if not is_float(weight):
        print("Вы ввели вес в неверном формате.")
        return get_user_weight()
    return float(weight)


def get_user_height() -> float:
    """
    Запрашивает рост пользователя в метрах

    :return: Рост пользователя в метрах
    """
    height = input("Пожалуйста, введите Ваш рост в метрах "
                   "(например, 1.75 или 2): ")
    # проверяем, что пользователь не передает пустую строку
    if is_blank(height):
        print("Вы ничего не ввели.")
        return get_user_height()
    # проверяем, что передаваемое пользователем значение преобразуется в float
    if not is_float(height):
        print("Вы ввели рост в неверном формате.")
        return get_user_height()
    return float(height)


def calculate_bmi(weight: float, height: float) -> float:
    """
    Рассчитывает индекс массы тела

    :param weight: Вес человека
    :param heigh: Рост человека
    :return: Индекс массы тела, округленный до десятых
    """
    index = weight / (height ** 2)
    return round(index, 1)


def calculate_water_needed(weight: float) -> float:
    """
    Рассчитывает рекомендуемое количество воды в сутки

    :param weight: Вес человека в килограммах
    :return: Объем воды в литрах, округленный до сотых
    """
    return weight * WATER_PER_KG / 1000


def fit_life() -> None:
    """
    Собирает данные о пользователе, производит вычисление
    ИМТ и рекомендуемой нормы воды в день, выводит в
    терминал полученную информацию
    """
    print("Здравствуйте!", end=" ")
    user_name = get_user_name()
    user_age = get_user_age()
    user_weight = get_user_weight()
    user_height = get_user_height()
    bmi = calculate_bmi(user_weight, user_height)
    water_needed = calculate_water_needed(user_weight)
    delimeter = "=================================================="
    print(f"\n{delimeter}")
    print(f"Отчет для пользователя: {user_name}, возраст: {user_age}")
    print(f"Ваш Индекс Массы Тела: {bmi}")
    print(f"Рекомендуемая норма воды в день: {water_needed:.2f} л.")
    print("Расчет окончен. Будьте здоровы!")
    print(delimeter)


fit_life()
