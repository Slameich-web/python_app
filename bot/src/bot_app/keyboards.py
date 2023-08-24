from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from .env import WEB_APP

inline_button_web = InlineKeyboardButton('WEB', web_app=WebAppInfo(url=WEB_APP))
inline_button_resources = InlineKeyboardButton('Ресурсы', callback_data='resources')
inline_button_issues = InlineKeyboardButton('По вопросам сотрудничества', callback_data='issues')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_web)
inline_kb.add(inline_button_resources)
inline_kb.add(inline_button_issues)