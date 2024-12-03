from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot1.db import add_booking


router = Router()

class Bron(StatesGroup):
    asking_name = State()
    asking_date = State()
    asking_time = State()
    asking_quantity = State()
    asking_preferences = State()

@router.message(Command('book'))
async def start_booking(message: Message, state: FSMContext):
    await message.answer('Введите ваше имя:')
    await state.set_state(Bron.asking_name)

@router.message(Bron.asking_name)
async def bron_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Хорошо! Введите день бронирования')
    await state.set_state(Bron.asking_date)

@router.message(Bron.asking_date)
async def bron_date(message: Message, state: FSMContext):
    await state.update_data(date_bron=message.text)
    await message.answer('Понял! Введите время для бронирования')
    await state.set_state(Bron.asking_time)

@router.message(Bron.asking_time)
async def bron_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer('Понятно! Укажите кол-во человек')
    await state.set_state(Bron.asking_quantity)

@router.message(Bron.asking_quantity)
async def bron_quantity(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await message.answer('Принял! Будут ли предпочтения по сервису?')
    await state.set_state(Bron.asking_preferences)

@router.message(Bron.asking_preferences)
async def bron_preferences(message: Message, state: FSMContext):
    await state.update_data(preferences=message.text)
#    await send_invoice_deposit(message)
    data = await state.get_data()
    await state.clear()

    a = {
        'name': data.get('name'),
        'date_bron': data.get('date_bron'),
        'time': data.get('time'),
        'quantity': data.get('quantity'),
        'preferences': data.get('preferences'),
    }
    add_booking(a.get('name'),
                a.get('date_bron'),
                a.get('time'),
                a.get('quantity'),
                message.from_user.id)