from aiogram import Bot, Dispatcher, executor, types, executor
from aiohttp.client import request
from bot_token import TOKEN
import gkeepapi
import time

# init bot
bot = Bot(token=TOKEN,  parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

# Log in Google Keep
keep = gkeepapi.Keep()
# username and password app
keep.login('email', 'password')

title_time = time.asctime()


''' Command Start '''
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Hello.')

    ''' Buttons '''
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Create note", "Get all notes"]
    keyboard.add(*buttons)
    await bot.send_chat_action(message.chat.id, 'typing')
    await message.answer('Choose commands: ', reply_markup=keyboard)


''' Create Notes '''
@dp.message_handler(lambda message: message.text == "Create note")
async def notes(message: types.Message):
    await bot.send_chat_action(message.chat.id, 'typing')

    buttons = [
        types.InlineKeyboardButton(text="pinned", callback_data="pinned_notes"),
        types.InlineKeyboardButton(text="color", callback_data="color_notes")
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)

    await message.answer("please input text: ", reply_markup=keyboard)


    ''' Inline button PINNED '''
    @dp.callback_query_handler(text="pinned_notes")
    async def pinned(call: types.CallbackQuery):
        await message.answer('the notes will be *pinned*')
        await call.answer()


    @dp.message_handler()
    async def input_text(message: types.Message):
        # input text notes
        input_notes = str(message.text)
        gnote = keep.createNote(str(title_time), input_notes)
        gnote.pinned = True

        # notes color
        gnote.color = gkeepapi.node.ColorValue.Blue
        # keep sync
        keep.sync()
        await message.answer("✅")



''' Get help '''
@dp.message_handler(commands="help")
async def cmd_start(message: types.Message):
    await message.answer("'/pin' — Use the phrase  in your notes to pin the note. By default, notes are not pinned\n\n`Example: lorem ipsum /pin`")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
