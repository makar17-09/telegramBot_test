# Иморт необходимых библиотек
import asyncio
from aiogram import F
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from random import randint

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="????????????????????")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Этот бот может поднять тебе настроение 😁"
                         "Выбери: \n\t/new если хочешь узнать новости"
                         "\n\t/joke если хочешь получить 💥 шутку"
                         "\n\t/nice если хочешь получить комплимент"
                         "\n\t/emoji чтобы выбрать смайлик")


@dp.message(Command("new"))
async def cmd_test1(message: types.Message):
    await message.answer("В Санкт-Петербурге открыли музей, "
                        "посвященный культуре и истории проклятий")

# У этой команды специально не объявлен хэндлер
# Хэндлер будет объявлен после команды /joke
# Чтобы продолжение шутки было после фразы "Кто там?"
async def echo_joke(message: types.Message):
    await message.reply("Джордж Мартин заходит в бар, и все, "
                        "кого вы когда-либо любили, умирают.")


@dp.message(Command('joke'))
async def cmd_test2(message: types.Message):
    await message.reply("Тук тук!")
    # вот и не объявленный хэндлер
    dp.message.register(echo_joke, F.text)


# Здесь еще используется рандом
@dp.message(Command("nice"))
async def cmd_answer(message: types.Message):
    mimimi = ['Ты сладенький единорожек🦄','У тебя красивые ноздри👃',
              'Милое косоглазие👀','Какие розовые щечки🐷',]
    await message.answer(mimimi[randint(0,len(mimimi) - 1)])


# Комнада /emoji сперва выдет текст доступных эмоджи
# Потом уже можно нажать на нужный
@dp.message(Command("emoji"))
async def cmd_emoji(message: types.Message):
    await message.answer("Выбери смайл:\n\t/dice - игральная кость"
                         "\n\t/bowling - боулинг"
                         "\n\t/dart - дартс"
                         "\n\t/basketball - баскетбол")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@dp.message(Command("basketball"))
async def cmd_emoji(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


@dp.message(Command("dart"))
async def cmd_emoji(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.DART)


@dp.message(Command("bowling"))
async def cmd_emoji(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

