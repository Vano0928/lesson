import requests
from decorators import message_handler, handle_all_handlers

# Ваш токен для доступу до Telegram Bot API
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
URL = f'https://api.telegram.org/bot{TOKEN}'

# Функція для отримання оновлень від бота
def get_updates(offset=None):
    # Формування URL для запиту оновлень
    url = f'{URL}/getUpdates?timeout=100'

    # Якщо є offset, додаємо його до URL
    if offset:
        url += f'&offset={offset}'

    # Виконання запиту до Telegram API
    response = requests.get(url)

    # Повернення відповіді у форматі JSON
    return response.json()

# Функція для надсилання повідомлення
def send_message(chat_id, text):
    # Формування URL для надсилання повідомлення
    url = f"{URL}/sendMessage"
    # Підготовка даних для відправки
    payload = {'chat_id': chat_id, 'text': text}
    # Виконання POST-запиту для надсилання повідомлення
    requests.post(url, payload)

# Декоратор для обробки повідомлень, які містять текст "hello"
@message_handler(lambda t: t == "hello")
def hello(message):
    # Отримання chat_id з повідомлення
    chat_id = message['chat']['id']
    # Відправка повідомлення "hello world"
    send_message(chat_id, 'hello world')

# Декоратор для обробки всіх інших повідомлень
@message_handler()
def echo(message):
    # Отримання chat_id і тексту з повідомлення
    chat_id = message['chat']['id']
    text = message['text']
    # Відправка того ж тексту назад (ехо)
    send_message(chat_id, text)

# Головна функція
def main():
    # Початкове значення offset
    offset = None

    # Безкінечний цикл для постійного отримання оновлень
    while True:
        # Отримання оновлень від бота
        updates = get_updates(offset)

        # Друк оновлень у консоль
        print(updates)
        if updates['result']:
            # Оновлення offset для отримання наступних оновлень
            offset = updates['result'][-1]['update_id'] + 1

            # Обробка всіх отриманих повідомлень
            handle_all_handlers(updates)

# Запуск головної функції
if __name__ == '__main__':
    main()
