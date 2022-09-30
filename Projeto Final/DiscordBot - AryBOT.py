#Importando as bibliotecas necessárias para o projeto
import discord
import requests
import time
from discord.ext import commands
from dotenv import load_dotenv
import os

#Iniciando o dotenv, para proteger o meu iToken
load_dotenv()
TOKEN=os.getenv("TOKEN")

#Guardando a URL de onde receberei as informações.
site = "https://api-charadas.herokuapp.com/puzzle?lang=ptbr"

#Iniciando o Bot e definindo o prefixo de comando.
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#Definindo os eventos ao qual o bot irá responder.
@bot.event
async def on_ready():
    print(f'{bot.user.name} chegou para alegrar o seu dia!')

#Definindo os comandos ao qual o bot irá responder.
@bot.command()
async def piada(ctx):
    #Pegando a resposta da API
    resposta = requests.get(site)
    data = resposta.json()

    #Definindo as informações que irão ser coletadas da API
    setup = data.get("question")
    punch = data.get("answer")

    #Configurando o retorno do BOT
    await ctx.send(setup)
    time.sleep(5)
    await ctx.send(punch)

bot.run(TOKEN)