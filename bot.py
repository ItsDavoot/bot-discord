import discord
from discord.ext import commands

# ایجاد بات و تنظیمات اولیه
intents = discord.Intents.default()
intents.message_content = True  # مجوز دریافت محتوای پیام‌ها

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot {bot.user} is ready!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # جلوگیری از جواب دادن به پیام‌های خود بات

    if "خوبی" in message.content.lower():
        await message.channel.send("برو امروز پریودم حال ندارم 😒")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("سلام! 👋")

TOKEN = "MTM1NDUxMjY2OTI5Nzg2ODkxMQ.G8i41U.TALv_ebdjo-hno81LAeN42AZgq2po0C-Tofhwc"
bot.run(TOKEN)