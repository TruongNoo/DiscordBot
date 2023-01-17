import discord
import json
import os 
import random
import datetime
import time
from discord.utils import get
from dotenv import load_dotenv
import pytz
from discord.ext import commands
from discord.ext.commands import *

intents = discord.Intents.all()
intents.members = True
intents.guilds = True

start_time = time.time()
hochiminh = pytz.timezone("Asia/Ho_Chi_Minh")
load_dotenv()

bot = Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

#Event#
@bot.event
async def on_ready():
    print("Bot đã chạy!")

#Command#
@bot.command()
async def hello(ctx):
    await ctx.send("Hello. I'm Nha Thong Thai.")

@bot.command(name='caculate', help='Tính toán các phép toán cơ bản của học sinh lớp 1 xD')
async def caculate(ctx, *args):
    date_time_now = datetime.datetime.now()
    date_time_now = date_time_now.astimezone(hochiminh)
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    string = ' '.join(args)

    if string.find('x') != -1 :
        substrings = string.split('x')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])

            results = results*int(tmp)

        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)
                

    elif  string.find('*') != -1 :
        substrings = string.split('*')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results*int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('/') != -1 :
        substrings = string.split('/')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('+') != -1 : 
        substrings = string.split('+')
        results = 0
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results+int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('-') != -1 :
        substrings = string.split('-')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

@bot.command(name='cal')
async def cal(ctx, *args):
    date_time_now = datetime.datetime.now()
    date_time_now = date_time_now.astimezone(hochiminh)
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    string = ' '.join(args)

    if string.find('x') != -1 :
        substrings = string.split('x')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])

            results = results*int(tmp)

        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)
                

    elif  string.find('*') != -1 :
        substrings = string.split('*')
        results = 1
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results*int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('/') != -1 :
        substrings = string.split('/')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('+') != -1 : 
        substrings = string.split('+')
        results = 0
        n = len(substrings)
        for x in range(n):
            tmp = str(substrings[x])
            results = results+int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    elif  string.find('-') != -1 :
        substrings = string.split('-')
        tmp = str(substrings[0])
        results = int(tmp)
        n = len(substrings)
        for x in range(n):
            if x+1 < n :
                tmp = str(substrings[x+1])
                results = results-int(tmp)
        embed = discord.Embed(description=f"Kết quả của mình là : {results}", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

@bot.command(name='ship', help='Xem tỉ lệ thành công của bạn A và bạn B')
async def ship(ctx, arg1, arg2):

    date_time_now = datetime.datetime.now()
    date_time_now = date_time_now.astimezone(hochiminh)
    date_time_now = str(date_time_now)
    date_time_now =  date_time_now[:19] + date_time_now[26:]

    if arg2 == None or arg1 == None :
        embed = discord.Embed(description=f">ship chỉ có thể ship được 2 bạn với nhau", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

    else:
        percent = random.randint(1,100)

        embed = discord.Embed(description=f"Tỉ lệ thành công trong tình yêu của {arg1} và {arg2} là : {percent}%", color=0x00ff00)
        embed.set_footer(text=f" Made by TKG - {date_time_now} - According to the timezone UTC+7 of Vietnam")

        await ctx.send(embed=embed)

bot.run('MTA2NDgyNjc3MzM4MjEyMzU3MQ.G665P0.FF2nVKRxJ_3SyjS-As00dQbM5aR8rNYi79ah2M')
