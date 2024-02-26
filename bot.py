import asyncio
from contextlib import suppress
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.enums.dice_emoji import DiceEmoji
import random
from aiogram.exceptions import TelegramBadRequest
import keyboards
import httpx
import aiohttp
from config import bot

letterseng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lettersrus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

wordseng = ["awkward", "bureaucracy", "cryptocurrency", "dumbwaiter", "exaggerate",
            "flibbertigibbet", "gobbledygook", "higgledy-piggledy", "ignominious", "juxtaposition",
            "kaleidoscope", "labyrinthine", "mnemonic", "onomatopoeia", "pneumonoultramicroscopicsilicovolcanoconiosis",
            "quizzaciously", "rhythm", "sycophant", "troubadour",
            "ubiquitous", "vexatious", "whippersnapper", "xenophobic", "yellowbellied",
            "zeppelin", "absquatulate", "bamboozle", "cacophony", "doppelganger",
            "flummox", "garrulous", "hullabaloo", "inculcate", "jejune",
            "kowtow", "lackadaisical", "mellifluous", "nomenclature", "obfuscate",
            "peregrinate", "quixotic", "rambunctious", "serendipity", "triskaidekaphobia",
            "ululate", "verisimilitude", "wamblecropt", "xylophone", "yammer",
            "zeitgeist"]

wordsrus = ["абракадабра", "балдахин", "взблеск", "глубокомысленный", "двухэтажный",
            "ежих", "жужжание", "заговорщик", "изюминка", "йогурт",
            "капуста", "ловкость", "многогранник", "невзрачный", "оглушительный",
            "поддерживающий", "рассеивание", "свирепствующий", "трехъярусный", "ухаживающий",
            "фантастический", "хохочущий", "цветущий", "шептание", "щебетание",
            "эксцентричный", "ювелирный", "яростный", "абсурдный", "благородный",
            "вихревой", "гипнотизировать", "джентльмен", "железнодорожный", "зажигательный",
            "изысканный", "йодированный", "колеблющийся", "лаконичный", "магнитофон",
            "недооцененный", "овощеводство", "парадоксальный", "ретро", "сумасшедший",
            "телевизионный", "универсальный", "фьють", "харизматичный", "ценитель",
            "шахматный", "щегольской", "эклектичный", "юродивый", "ягодица"]

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f'Hello, {message.from_user.first_name}', reply_markup=keyboards.main_kb)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message()
async def echo(message:Message):
    msg = message.text.lower()

    if msg == 'настроить игру':
         await message.answer(f'Выбирайте:', reply_markup=keyboards.languages_kb)       

    elif msg== 'наши ссылки':
        await message.answer(f'Держи:', reply_markup=keyboards.links_kb)

@dp.message()
async def info(message:Message):
    msg = message.text.lower()

    if msg== 'правила игры':
        await message.answer(f'''
Для начала, для чего был создан этот бот?
                                                          
- Для того, чтобы вы научились печатке в сплепую.
Данный бот поможет отслеживать свой прогресс в печатке.
                                                          
Правила игры:
                             
Нажав на начать игру, вы выбираете сначала язык, а потом уже просто буквы или целые слова. После начала игры начинается отсчет. Отсчет идет в секундах. 
С самого начала имеется список из букв или слов. Бот возвращает вам букву или слово, а вы просто возвращаете
это слово или букву. Количество секунд, за которое вы решили данную задачу, сохранится в ваш профиль.                                                       
Отсчет идет в секундах. 
''')
        
@dp.message(F.text == 'Русский')
async def game(message:Message):
    await message.answer('Отлично! Вы выбрали русский язык. Выберите слово либо буква?', reply_markup=keyboards.action_kb)
        
@dp.message()
async def languages(message:Message):
    msg = message.text.lower()

    if msg == 'русский':
        await message.answer('Отлично! Вы выбрали русский язык. Выберите слово либо буква?', reply_markup=keyboards.action_kb)

        if msg == 'слово':
            await message.answer('Отлично! Вы выбрали слово.')
    
    elif msg == 'english':
        await message.answer('Отлично! Вы выбрали русский язык. Выберите слово либо буква?', reply_markup=keyboards.action_kb)

@dp.message()
async def echo(message:Message):
    await message.answer(f'I do not know this command!')

if __name__ == '__main__':
    asyncio.run(main())