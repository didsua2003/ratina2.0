import discord
import os
import asyncio
import re

client = discord.Client()
token = "NzE1NTkxMDM0ODgwNTI0NDA4.Xs_cdw.71GciEUs6YCQdSU4xKy8i87BnFM"


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)  # 온라인
    # await client.change_presence(status=discord.Status.idle) #자리비움
    # await client.change_presence(status=discord.Status.dnd) #다른용무
    # await client.change_presence(status=discord.Status.offline) #오프라인
    await client.change_presence(activity=discord.Game(name="최적화"))  #
    # await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크')) #
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중")) #
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
    print("봇 이름:", client.user.name, "봇 아이디:", client.user.id, "봇 버전:", discord.__version__)


@client.event  # 대화 집어넣기
async def on_message(message):
    if message.author.bot:  # 대상이 봇일때 무시
        return None

    print(message.content)
    if message.content == "^안녕":
        await message.channel.send("반가워요!")


    if message.content.startswith("^정보"):
        embed = discord.Embed(title="안녕하세요!라티나에요!", description="버전:2.0", color=0x00ff00)
        embed.add_field(name="생일", value="20200529", inline=True)
        embed.add_field(name="제작자", value="김세훈#0751", inline=True)
        embed.set_footer(text="테스트 중이에요!")
    await message.channel.send(embed=embed)




access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
