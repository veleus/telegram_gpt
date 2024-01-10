from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from crud.operations import get_all_users
from database import db

def get_yes_no_kb(): 
    users_data = get_all_users(db) 
    builder = InlineKeyboardBuilder() 
    for user in users_data:
        name = str(user[2])
        callback_data = str(user[1])
        button_text = f"{name}"
        builder.add(
            types.InlineKeyboardButton(
                text=button_text, 
                callback_data=f'{callback_data}'
            )
        )
    return builder


