# Проект FitLife - MVP версия 1.1

# рекомендуемый объём воды в мл на кг веса
WATER_ML_PER_KG = 30
ML_IN_LITER = 1000


def is_blank(user_input: str) -> bool:
    """Проверяет, является ли строка пустой."""
    return user_input.strip() == ""


def is_float(user_input: str) -> bool:
    """Проверяет, преобразуется ли строка в float."""
    try:
        float(user_input)
        return True
    except ValueError:
        return False


def is_int(user_input: str) -> bool:
    """Проверяет, преобразуется ли строка в int."""
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def get_user_name() -> str:
    """
    Запрашивает у пользователя имя, возвращает полученое имя.

    Получает от попьзователя строку, проверяет, не пустая ли она. Затем
    возвращает полученную строку, написанную с заглавной буквы.
    """
    name = input("Введите имя: ")
    if is_blank(name):
        print("Вы ничего не ввели.")
        return get_user_name()
    return name.title()


def get_user_age() -> int:
    """
    Запрашивает у пользователя возраст, возвращает полученный возраст.

    Получает от пользователя строку, проверяет её на пустоту, на возможность
    преобразовать в int. Возвращает возраст в метрах.
    """
    age = input("Введите Ваш возраст в годах (например, 27): ")
    if is_blank(age):
        print("Вы ничего не ввели.")
        return get_user_age()
    if not is_int(age):
        print("Вы ввели возраст в неверном формате.")
        return get_user_age()
    return int(age)


def get_user_weight() -> float:
    """
    Запрашивает у пользователя вес в кг, возвращает полученный вес.

    Получает от пользователя строку, проверяет её на пустоту, на возможность
    преобразовать в float. Возвращает вес в кг.
    """
    weight = input("Введите Ваш вес в килограммах, "
                   "например, 50.5 или 73: ")
    if is_blank(weight):
        print("Вы ничего не ввели.")
        return get_user_weight()
    # подстраховка на случай, если пользователь введёт вес с запятой
    if ',' in weight:
        weight = weight.replace(',', '.')
    if not is_float(weight):
        print("Вы ввели вес в неверном формате.")
        return get_user_weight()
    return float(weight)


def get_user_height() -> float:
    """
    Запрашивает рост пользователя в метрах, возвращает полученный рост.

    Получает от пользователя строку, проверяет её на пустоту, на возможность
    преобразовать в float. Возвращает рост в метрах.
    """
    height = input("Пожалуйста, введите Ваш рост в метрах "
                   "(например, 1.75 или 2): ")
    if is_blank(height):
        print("Вы ничего не ввели.")
        return get_user_height()
    # подстраховка на случай, если пользователь введёт рост с запятой
    if "," in height:
        height = height.replace(',', '.')
    if not is_float(height):
        print("Вы ввели рост в неверном формате.")
        return get_user_height()
    return float(height)


def calculate_bmi(weight: float, height: float) -> float:
    """
    Возвращает индекс массы тела.

    weight -- вес человека в кг
    heigh -- рост человека в м
    """
    return weight / (height ** 2)


def calculate_water_needed(weight: float) -> float:
    """
    Возвращает рекомендуемое количество воды в сутки в литрах.

    weight -- вес человека в кг
    """
    return weight * WATER_ML_PER_KG / ML_IN_LITER


def fit_life() -> None:
    """
    Формирует отчёт с рекомендациями для пользователя.

    Получает от пользователя имя, возраст, вес и рост.
    Высчитывает индекс массы тела и рекомендуемое потребление
    воды в сутки в литрах. Выводит полученные результаты в терминал.
    """
    print("Здравствуйте!", end=" ")
    user_name = get_user_name()
    user_age = get_user_age()
    user_weight = get_user_weight()
    user_height = get_user_height()
    bmi = round(calculate_bmi(user_weight, user_height), 1)
    water_needed = calculate_water_needed(user_weight)
    delimeter = "=================================================="
    print(f"\n{delimeter}")
    print(f"Отчет для пользователя: {user_name}, возраст: {user_age}")
    print(f"Ваш Индекс Массы Тела: {bmi}")
    print(f"Рекомендуемая норма воды в день: {water_needed:.2f} л.")
    print("Расчет окончен. Будьте здоровы!")
    print(delimeter)


fit_life()
