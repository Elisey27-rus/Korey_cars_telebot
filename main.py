import sqlite3

from telebot import telebot
from telebot import types
from colorama import Fore
from won_to_ruble import exchange

API = '6219272454:AAE6oEBGeYWrkFWflm1duetbFyeTNpcqO8Y'  # t.me/Korean_Car_bot
bot = telebot.TeleBot(API)


@bot.message_handler(commands=['start'])
def start(message):
    table = types.InlineKeyboardMarkup(row_width=1)
    line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
    line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
    line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
    line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
    table.add(line_1, line_3, line_4, line_2)
    text = f"Привет, {message.from_user.first_name}!\n\n" \
           "Я бот по привозу машин из Кореи 🚗💨\n" \
           "Со мной вы можете рассчитать стоимость авто, узнать курс воны " \
           "по отношению к рублю, получить полную информацию по доставке авто " \
           "и связаться с администратором.\n" \
           "Чтобы начать, выберите одну из кнопок ниже 👇"
    bot.send_message(message.chat.id, text, reply_markup=table)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    call_back = call.data
    if call_back == 'admin':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        text = "🧑‍💻 Елчев Александр 🚗\n" \
               "  ⌚ +79241197014 📲\n" \
               "  📟 firtree@mail.ru ⏱\n" \
               "     📘 @firtree ✏"
        bot.send_message(call.message.chat.id, text)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)

    elif call_back == 'info':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        text_2 = '🚚✈️🚢🇰🇷 Как привозят авто из Кореи в Россию?\n \
        Первым шагом является покупка автомобиля на аукционе в Корее. Затем автомобиль отправляют на склад, где его осматривают и подготавливают к доставке.\n \
        Далее автомобиль может быть отправлен морским или авиационным транспортом в порт назначения. При выборе морской доставки автомобиль загружают на корабль и перевозят через Тихий океан до России.\n \
        После прибытия автомобиля на порт выполняется процедура таможенного оформления, где автомобиль проходит проверку таможенниками. Если все документы на машину в порядке, таможенники утверждают ее ввоз в Россию.\n \
        Наконец, автомобиль отправляют на транспортировку к конечному пункту назначения, где покупатель получает свой новый автомобиль! 🚗💨'
        bot.send_message(call.message.chat.id, text_2)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)

    elif call_back == 'von_price':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        von_price = exchange()
        text_3 = f'Курс воны по соотношению с рублем равен: {von_price} вон.'
        bot.send_message(call.message.chat.id, text_3)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)

    elif call_back == 'car_price':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="KIA🚗", callback_data='KIA')
        line_2 = types.InlineKeyboardButton(text="Hyundai🚙", callback_data='Hyundai')
        text = "Выберите марку авто:"
        table.add(line_1, line_2)
        bot.send_message(call.message.chat.id, text=text, reply_markup=table)


    elif call_back == 'Hyundai':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Creta", callback_data='Creta')
        line_2 = types.InlineKeyboardButton(text="Solaris", callback_data='Solaris')
        line_3 = types.InlineKeyboardButton(text="Tucson", callback_data='Tucson')
        line_4 = types.InlineKeyboardButton(text="Santa Fe", callback_data='Santa Fe')
        text = "Выберите модель доступных авто:"
        table.add(line_1, line_2, line_3, line_4)
        bot.send_message(call.message.chat.id, text=text, reply_markup=table)

    elif call_back == 'KIA':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="K5", callback_data='K5')
        line_2 = types.InlineKeyboardButton(text="Sportage", callback_data='Sportage')
        line_3 = types.InlineKeyboardButton(text="Rio", callback_data='Rio')
        line_4 = types.InlineKeyboardButton(text="Ceed", callback_data='Ceed')
        line_5 = types.InlineKeyboardButton(text="Cerato", callback_data='Cerato')
        line_6 = types.InlineKeyboardButton(text="Karnival", callback_data='Karnival')
        text = "Выберите марку доступных авто:"
        table.add(line_1, line_2, line_3, line_4, line_5, line_6)
        bot.send_message(call.message.chat.id, text=text, reply_markup=table)

    elif call_back == 'K5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        with sqlite3.connect('all_cars.db') as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM CARS WHERE Name_auto == 'K5'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            text = f'🚙Марка авто:\n{result[0][0]}\n\n🛞Модель:\n{result[0][1]}\n\n🔒Год и поколение:\n{result[0][2]}' \
                   f'\n\n💰Цена под ключ до города Владивосток со всеми коммиссиями:\n{result[0][3]}' \
                   f'\n\n👨‍🔧Отзывы от владельцев авто:\n{result[0][4]}'
        bot.send_message(call.message.chat.id, text)
        picture_1 = open('photo/K5.jpg', 'rb')
        picture_2 = open('photo/K5-2.jpg', 'rb')
        picture_3 = open('photo/K5-3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=picture_1)
        bot.send_photo(call.message.chat.id, photo=picture_2)
        bot.send_photo(call.message.chat.id, photo=picture_3)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)

    elif call_back == 'Sportage':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        with sqlite3.connect('all_cars.db') as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM CARS WHERE Name_auto == 'Sportage'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            print(result)
            text = f'🚙Марка авто:\n{result[0][0]}\n\n🛞Модель:\n{result[0][1]}\n\n🔒Год и поколение:\n{result[0][2]}' \
                   f'\n\n💰Цена под ключ до города Владивосток со всеми коммиссиями:\n{result[0][3]}' \
                   f'\n\n👨‍🔧Отзывы от владельцев авто:\n{result[0][4]}'
        bot.send_message(call.message.chat.id, text)
        picture_1 = open('photo/Sportage-1.jpg', 'rb')
        picture_2 = open('photo/Sportage-2.jpg', 'rb')
        picture_3 = open('photo/Sportage-3.jpg', 'rb')
        picture_4 = open('photo/Sportage-4.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=picture_1)
        bot.send_photo(call.message.chat.id, photo=picture_2)
        bot.send_photo(call.message.chat.id, photo=picture_3)
        bot.send_photo(call.message.chat.id, photo=picture_4)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)

    elif call_back == 'Rio':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        with sqlite3.connect('all_cars.db') as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM CARS WHERE Name_auto == 'Rio'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            print(result)
            text = f'🚙Марка авто:\n{result[0][0]}\n\n🛞Модель:\n{result[0][1]}\n\n🔒Год и поколение:\n{result[0][2]}' \
                   f'\n\n💰Цена под ключ до города Владивосток со всеми коммиссиями:\n{result[0][3]}' \
                   f'\n\n👨‍🔧Отзывы от владельцев авто:\n{result[0][4]}'
        bot.send_message(call.message.chat.id, text)
        picture_1 = open('photo/Rio-1.jpg', 'rb')
        picture_2 = open('photo/Rio-2.jpg', 'rb')
        picture_3 = open('photo/Rio-3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=picture_1)
        bot.send_photo(call.message.chat.id, photo=picture_2)
        bot.send_photo(call.message.chat.id, photo=picture_3)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)


    elif call_back == 'Ceed':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        with sqlite3.connect('all_cars.db') as conn:
            cursor = conn.cursor()
            query = f"SELECT * FROM CARS WHERE Name_auto == 'Ceed'"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            print(result)
            text = f'🚙Марка авто:\n{result[0][0]}\n\n🛞Модель:\n{result[0][1]}\n\n🔒Год и поколение:\n{result[0][2]}' \
                   f'\n\n💰Цена под ключ до города Владивосток со всеми коммиссиями:\n{result[0][3]}' \
                   f'\n\n👨‍🔧Отзывы от владельцев авто:\n{result[0][4]}'
        bot.send_message(call.message.chat.id, text)
        picture_1 = open('photo/Ceed-1.jpg', 'rb')
        picture_2 = open('photo/Ceed-2.jpg', 'rb')
        picture_3 = open('photo/Ceed-3.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo=picture_1)
        bot.send_photo(call.message.chat.id, photo=picture_2)
        bot.send_photo(call.message.chat.id, photo=picture_3)
        table = types.InlineKeyboardMarkup(row_width=1)
        line_1 = types.InlineKeyboardButton(text="Связаться с администратором 🧑‍💻", callback_data='admin')
        line_2 = types.InlineKeyboardButton(text="Расчитать стоимость авто 💲", callback_data='car_price')
        line_3 = types.InlineKeyboardButton(text="Курс воны по отношению к рублю 💱", callback_data='von_price')
        line_4 = types.InlineKeyboardButton(text="Полная информация по доставке авто 🚗", callback_data='info')
        table.add(line_1, line_3, line_4, line_2)
        bot.send_message(call.message.chat.id, text=f'😃Чем я еще могу помочь вам {call.message.chat.first_name}?😊',
                         reply_markup=table)


if __name__ == "__main__":
    print(Fore.LIGHTYELLOW_EX + "Бот успешно запущен.")
    bot.polling(none_stop=True)
