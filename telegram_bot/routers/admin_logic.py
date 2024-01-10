from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from database  import db
from keyboard_forAdmin.admin_panel import get_yes_no_kb
from dto.model_transder import User
from crud.operations import get_user_by_id, update_user

router = Router()
@router.message(Command("change_role"))
async def cmd_start(message: Message):
    if message.from_user.id == 930423518:
        user_buttons = get_yes_no_kb()
        await message.answer(
            "Выберите пользователя для смены его роли!",
            reply_markup=user_buttons.as_markup()
        )
    else:
        await message.answer(f"🔥Ты не администратор!!🔥 {message.from_user.full_name}")


@router.callback_query()  
async def send_random_value(callback: types.CallbackQuery):    
        selected_server = callback.data
        if selected_server:
            name = get_user_by_id(db, selected_server)
            update_user(db, selected_server)
            await callback.message.answer(f"Права пользователя : {name.name} были повышены!") 