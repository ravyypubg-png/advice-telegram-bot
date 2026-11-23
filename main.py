import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token='you shouldnt care about it...')
dp = Dispatcher()
async def get_random_quote() -> str:
    url = "https://api.adviceslip.com/advice"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data["slip"]["advice"]
@dp.message(Command("quote"))
async def cmd_quote(message: Message):
    try:
        quote = await get_random_quote()
        await message.answer(f"💬 {quote}")
    except Exception as e:
        await message.answer("Не удалось получить цитату 😔")
        print(e)
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())