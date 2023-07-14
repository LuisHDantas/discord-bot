import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import pandas as pd
import asyncio
import csv

 
 
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
#bot = discord.Client(intents=intents)

bot = commands.Bot(command_prefix=">>", intents=intents)

df = pd.read_csv('in.csv', sep='|')

dataBase = [(topics, question, answer) for topics, question, answer in zip(df.topics, df.questions, df.answers)]


topicsToString = [
    "Introdução",
    "Arquitetura RISC-V: Assembly",
    "Arquitetura RISC-V: Monociclo",
    "Arquitetura RISC-V: Pipeline",
    "Hierarquia de Memória",
    "Entrada e Saída",
    "Barramento"
]

topics = [
    "Introducao",
    "Assembly",
    "Monociclo",
    "Pipeline",
    "Hierarquia",
    "ES",
    "Barramento"
]

@bot.event
async def on_ready():
    print("Bot is online!")
    
# async def on_message(message):
	
# 	if message.content.startswith(">>"):
# 		#getting command from user
# 		command = message.content.lstrip(">>")
  
# 		if command == "perguntas":
# 			#prints the topics of study for the user to choose
# 			await Questions.TopicsMenu(message)
# 			return
   
# 		answer = dic.get(command)
# 		if answer is not None:
# 			await message.channel.send(answer)

# 		#if on the topics menu
# 		elif onTopicsMenu():
# 			Questions.TopicChoice(message, dic)
      
@bot.command(
    aliases = ['questions','exercicios'],
	help = "Example:\n >>perguntas",
	brief = "Study material",
	description = "Gives the user study material for the course",
	enabled = True,
	hidden = False
)
async def perguntas(message):
	"""Gives the user the option to choose the desired topic of the questions"""
	embed = discord.Embed(
		colour = discord.Colour.dark_teal(),
		description = """1. Introdução
2. Arquitetura RISC-V: Assembly
3. Arquitetura RISC-V: Monociclo
4. Arquitetura RISC-V: Pipeline
5. Hierarquia de Memória
6. Entrada e Saída
7. Barramento

Use >>cancelar para sair!""",
		title = f"Olá **{message.author.global_name}**! Qual tópico você quer estudar?"
	)
	embed.set_footer(text="Organização e Arquitetura de Computadores")
	await message.send(embed=embed)
	#await Questions.TopicsMenu(message)
	def check(m):
		if m.content == ">>cancelar":
			return True
		return m.content.isdigit() and int(m.content) in range(1, 8) and m.channel == message.channel

	try:
		msg = await bot.wait_for('message', check=check)
		if msg.content == ">>cancelar":
			await message.send("Comando cancelado.")
			return
	except asyncio.TimeoutError:
		await message.send("Tempo esgotado. Comando 'perguntas' cancelado.")
		return

	
 
	#Gets questions and answers
	counter = 0
	questions = []
	answers = []
	for topic, question, answer in dataBase:
		if topic == topics[int(msg.content)-1]:
			questions.append(question)
			answers.append(answer)
			counter += 1
 
 
 
 #Sends user the questions in DM

	if len(questions) != 0:
		await message.author.send(f"""Aqui estão **{counter}** questões sobre o tópico **{topicsToString[int(msg.content)-1]}** da disciplina de Organização e Arquitetura de Computadores!
# Questões\n\n""")
  
		for i, (question,answer) in enumerate(zip(questions,answers)):
			await message.author.send(f"""### __**Questão {i+1}**__\n
```{question}```
Resposta:
||```{answer}```||""")

		await message.author.send("""## \n\nTem dúvidas? Entre em contato com um monitor ou com a professora Sarita!\n
**Contatos:**
__E-mail:__ sarita@icmc.usp.br
__Discord:__ @Sarita - ICMC/USP (No Grupo da disciplina)""")

	else:
		await message.author.send("Não tenho questões desse tópico disponíveis.")

 
	
	return
      
bot.run(DISCORD_TOKEN)


