import discord
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

df = pd.read_csv('in.csv')
dic = dict(zip(df.questions, df.answers))

@bot.event
async def on_message(message):
	answer = dic.get(message.content)
	if answer is not None:
	 	await message.channel.send(answer)


bot.run(DISCORD_TOKEN)
