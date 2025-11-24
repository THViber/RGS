import discord, os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print(f'{client.user} has connnected to Discord!')

@bot.command()
async def ocr():
    print("You tried to run an OCR!")
client.run(TOKEN)