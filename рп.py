import random

# Словарь с информацией о уровнях
levels = {
    1: {"name": "Вход в замок",
        "description": "Перед тобой огромные дубовые ворота, ведущие в замок. Над воротами висит табличка с надписью: \"Добро пожаловать!\"."},
    2: {"name": "Большой зал",
        "description": "Ты в огромном зале, стены которого украшены гобеленами. В центре зала стоит большой камин."},
    3: {"name": "Тайная комната",
        "description": "Ты оказался в небольшой комнате. В центре комнаты стоит сундук. Над сундуком висит герб с тремя ключами."}
}

# Словарь с информацией о дверях
level_doors = {
    1: {"key": "Ключ от главного входа", "description": "Дверь из толстого дуба, запертая на огромный замок."},
    2: {"key": "Ключ от зала", "description": "Дверь из темного дерева, украшенная резными фигурами."},
    3: {"key": "Ключ от тайной комнаты", "description": "Дверь из железа, запертая на сложный механизм."}
}

# Действия персонажа
do_list = {
    1: {"do": "Нужно попасть в замок. Ты оглядываешься в раздумьях и нвходишь ключ, лежащий не подалеку. 'Наверно кто-то его обранил!' - подумал ты."},
    2: {"do": "Подходишь к камину ближе, и видишь, как странно лежит один из камней. Отодвигаешь его и начинаешь внимательно их рассматривать. Вдруг ты заметил что на них на царапан какой то текст. Это была загадка! Ты ее отгадал и...."},
    3: {"do": "'Наконец-то сундук!'. Ты пытаешь взломать замок, но все без успешно. От злости ты пинаешь сундук, он падает и с герба падает ключ. 'Точно!' - подумал ты. И начал внимательно их рассматривать. Вдруг ты заметил что на них на царапан какой то текст. Это была загадка! Ты ее отгадал и.... "}
}

# Список предметов, которые можно найти в замке
items = [
    "Ключ от главного входа",
    "Ключ от зала",
    "Ключ от тайной комнаты",
    "Статуэтка грифона",
    "Карта замка",
    "Посох"
]

# Множество найденных ключей
collected_keys = set()

# Инвентарь игрока
inventory = []

# Текущий уровень игрока
current_level = 1

# Функция для вывода описания уровня
def show_level_description(level_num):
    print(levels[level_num]["description"])

# Функция для вывода информации о дверях
def show_door_description(level_num):
    print(level_doors[level_num]["description"])

#Функция для описания действий персонажа
def do_list_description(level_num):
    print(do_list[level_num]["do"])

# Функция для добавления предмета в инвентарь
def add_item_to_inventory(item):
    inventory.append(item)
    print(f"Вы нашли {item}!")

# Функция для удаления предмета из инвентаря
def remove_item_from_inventory(item):
    inventory.remove(item)
    print(f"Вы использовали {item}!")

# Функция для генерации загадки
def generate_riddle():
    # Выбор случайной загадки из списка
    riddle = random.choice([
        "Что имеет ключи, но не замков, пространство, но не комнаты, вода, но не рыб?",
        "Я легка, как перо, но сильнейшая из женщин. Я могу быть покорна, но могу быть и жестокой. Я могу быть теплой, но могу быть и холодной. Что я?",
        "У меня много голов, но не мозга, я умею бегать, но не могу ходить. Что я?"
    ])
    return riddle

# Функция для проверки ответа на загадку
def check_riddle_answer(riddle, answer):
    if answer.lower() == "клавиатура":
        print("Правильно!")
        return True
    else:
        print("Неверно!")
        return False

# Функция для обработки команды
def process_command(command):
    global current_level, collected_keys

    if command.lower() == "взять ключ":
        if current_level == 1:
            add_item_to_inventory("Ключ от главного входа")
            collected_keys.add("Ключ от главного входа")
        elif current_level == 2:
            add_item_to_inventory("Ключ от зала")
            collected_keys.add("Ключ от зала")
        elif current_level == 3 :
            add_item_to_inventory("Ключ от тайной комнаты")
            collected_keys.add("Ключ от тайной комнаты")
        else:
            print("Здесь нет ключа.")
    elif command.lower() == "использовать ключ":
        if current_level == 1 and "Ключ от главного входа" in collected_keys:
            print("Вы открыли дверь в Большой зал.")
            current_level = 2
        elif current_level == 2 and "Ключ от зала" in collected_keys:
            print("Вы открыли дверь в Тайную комнату.")
            current_level = 3
            add_item_to_inventory("Ключ от тайной комнаты")
            collected_keys.add("Ключ от тайной комнаты")
        else:
            print("У вас нет ключа, чтобы открыть эту дверь.")
    elif command.lower() == "инвентарь":
        if inventory:
            print("В вашем инвентаре:")
            for item in inventory:
                print(f"- {item}")
        else:
            print("Ваш инвентарь пуст.")
    elif command.lower() == "загадка":
        riddle = generate_riddle()
        print(riddle)
        answer = input("Ответ: ")
        if check_riddle_answer(riddle, answer):
            # В качестве награды за правильный ответ добавить ключ в инвентарь
            if current_level == 1:
                add_item_to_inventory("Ключ от главного входа")
                collected_keys.add("Ключ от главного входа")
            elif current_level == 2:
                add_item_to_inventory("Ключ от зала")
                collected_keys.add("Ключ от зала")
            elif current_level == 3 :
                add_item_to_inventory("Ключ от тайной комнаты")
                collected_keys.add("Ключ от тайной комнаты")
    elif command.lower() == "помощь":
        print("Доступные команды: взять ключ, использовать ключ, инвентарь, загадка, помощь")
    else:
        print("Я не понимаю эту команду.")

# Основной цикл игры
while True:
    # Вывод описания уровня
    show_level_description(current_level)
    # Вывод описания двери, если есть
    if current_level in level_doors:
        show_door_description(current_level)
        do_list_description(current_level)
        # Вывод действий персонажа
    # Получение команды от игрока
    command = input("Введите команду: ")
    # Обработка команды
    process_command(command)

    # Проверка на завершение игры
    if current_level == 3 and "Ключ от тайной комнаты" in collected_keys:
        print("Поздравляем! Вы раскрыли тайну замка!")
        break