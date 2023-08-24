
from .app import dp
from .keyboards import inline_kb

@dp.message_handler(commands='start')
async def send_welcome(message):
    await message.reply("Hello", reply_markup=inline_kb)

@dp.callback_query_handler(text='issues')
async def issues_click(message): 
    await message.message.answer("@TELEGRAM")
    
@dp.callback_query_handler(text='resources')
async def issues_click(message): 
    await message.message.answer("ссылка на ресурсы компании: (уточнить ссылки).")
    
