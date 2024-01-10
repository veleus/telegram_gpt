
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from database import engine, db
from model.database import User, Base
from crud.operations import add_user, get_user
from telegram_config import TELEGRAM_TOKEN, ADMIN_TOKEN
from routers import admin_logic, conservations
from crud.operations import get_user_by_id

Base.metadata.create_all(bind=engine)

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):

    await message.answer(f"Привет, {message.from_user.first_name}! Приветсвуем тебя в проекте 🤝🏻")

    
@dp.message(Command("register"))
async def cmd_start(message: types.Message):

    name = message.from_user.first_name
    user_id  = message.from_user.id

    if get_user(db, user_id):
        await message.answer(f"🔥Ты уже зарегестрирован!!🔥")
    else:
        add_user(db, user_id,name)
        await message.answer(f"🔥Ты успешно зарегестрировался!!🔥")


dp.include_routers(admin_logic.router)
dp.include_routers(conservations.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())