from functools import wraps  # Імпортуємо wraps для збереження метаданих функцій при використанні декораторів

# Списки для збереження обробників повідомлень і умов
handlers = []
conditions = []

def message_handler(condition=True):
    """
    Декоратор для реєстрації обробників повідомлень з певною умовою.

    Параметри:
    condition (bool або функція) - Умова для обробки повідомлення. Може бути булевим значенням або функцією.
    """
    def decorator(func):
        @wraps(func)  # Зберігає метадані функції func
        def wraper(message):
            # Викликає функцію обробки з повідомленням
            return func(message)
        
        # Додаємо обгорнуту функцію та умову до відповідних списків
        handlers.append(wraper)
        conditions.append(condition)

        return wraper
    
    return decorator
        

def handle_all_handlers(updates):
    """
    Функція для обробки всіх зареєстрованих обробників повідомлень.

    Параметри:
    updates (dict) - Оновлення, що містять результати з повідомленнями.
    """
    for i in range(len(handlers)):
        for update in updates['result']:
            # Отримуємо текст повідомлення
            message_text = update['message']['text']

            # Перевіряємо, чи умова для обробника виконується
            if conditions[i] == True or conditions[i](message_text):
                # Викликаємо обробник з повідомленням
                handlers[i](update['message'])

                # Повертаємо після обробки одного повідомлення (можна змінити, якщо потрібно обробити всі)
                return
