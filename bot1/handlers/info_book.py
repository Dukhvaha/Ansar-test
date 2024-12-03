from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot1.db import get_bookings_by_user

router = Router()


@router.message(Command('my_bookings'))
async def reservation_cmd(message: Message):
    # Получаем данные о бронированиях
    user_id = message.from_user.id
    bookings = get_bookings_by_user(user_id)

    # Форматируем данные для отправки
    if bookings.empty:
        await message.reply("Нет активных броней.")
        return

    # Заголовок таблицы
    response_message = "📅 Список активных броней\n\n"
    response_message += "👤 Имя человека | 🏷️ Дата | 🕒 Время | 👥 Количество людей | 📝 Пожелания | Идентификатор пользователя (ID)\n"
    response_message += "-------------------------------------\n"

    # Добавляем каждую бронь в сообщение
    for index, row in bookings.iterrows():
        response_message += f"{row['name']} | {row['date']} | {row['time']} | {row['quantity']} | {row['preferences']} | {row['user_id']}\n"

    # Отправляем сообщение пользователю
    await message.reply(response_message)

# @router.message(Command('my_bookings'))
# async def info_bookings(message: Message):
#     user_id = message.from_user.id
#     bookings = get_bookings_by_user(user_id)
#
#     # Проверяем, пуст ли DataFrame
#     if bookings.empty:
#         await message.answer('У вас пока нет бронирований')
#         return
#
#     # Формируем ответ
#     response = 'Ваши бронирования:\n\n'
#     for booking in bookings.iterrows():  # Перебираем строки DataFrame
#         response += (
#             f"ID: {booking['id']}\n"
#             f"Дата: {booking['date']}\n"
#             f"Время: {booking['time']}\n"
#             f"Гости: {booking['quantity']}\n"
#             f"Пожелания: {booking['preferences']}\n"
#             f"Статус оплаты: {booking['payment_status']}\n\n"
#         )
#
#     await message.answer(response)
