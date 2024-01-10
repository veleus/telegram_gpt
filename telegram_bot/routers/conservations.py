from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from database  import db
from keyboard_forAdmin.admin_panel import get_yes_no_kb
from dto.model_transder import User
from crud.operations import get_user_by_id_admin

import openai


openai.api_key = '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'


router = Router()
@router.message()
async def chat_with_bot(message: types.Message):
    get_id = message.from_user.id

    user = get_user_by_id_admin(db, get_id)
    if user.role == 'role_admin':
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Выберите модель (model) в соответствии с вашими потребностями
            messages=[
                {"role": "user", "content": f"{message} ?"},
            ],
            max_tokens=1000
        )

        # Выведите результат
        result = response['choices'][0]['message']['content'].strip()
        
        await message.answer(text=result)

    else:
        await message.answer(text='Ты не можешь пользоваться ботом!')
    

