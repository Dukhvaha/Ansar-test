from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Добро пожаловать в бота для бронирования столика!\n'
                         '/book - Забронировать столик\n'
                         '/my_bookings - Просмотреть ваше бронирование')
    await state.clear()
