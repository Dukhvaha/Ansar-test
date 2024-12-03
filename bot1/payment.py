from aiogram import Router
from aiogram.types import Message, PreCheckoutQuery
from utils import PRICE
from config import PAYMENT_TOKEN
router = Router()


async def send_invoice_deposit(message: Message):

    await message.bot.send_invoice(
        chat_id=message.chat.id,
        title='Deposit for the table',
        description=DESCRIPTION_FOR_DEPOSIT,
        payload='deposit',
        provider_token=PAYMENT_TOKEN,
        currency='RUB',
        prices=PRICE,
    )


@router.pre_checkout_query()
async def checkout_handler(query: PreCheckoutQuery):
    await query.bot.send_message(query.from_user.id, 'Ожидайте, оплата проверяется..')
    await query.answer(ok=True)


@router.message(lambda message: message.successful_payment is not None)
async def successful_payment_handler(message: Message):
    await message.answer('Оплата прошла успешно!')


@router.message(lambda message: message.successful_payment is False)
async def dont_successful_payment_handler(message: Message):
    await message.answer('Оплата не прошла! Попробуйте пожалуйста снова.')
