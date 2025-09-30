import os
import asyncio
from playwright.async_api import async_playwright
from telegram import Bot

async def main():
    bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    await bot.send_message(chat_id=chat_id, text="🚀 Test: le script démarre correctement.")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://www.worldguessr.com/leaderboard")
        html = await page.content()
        print(html[:500])
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
