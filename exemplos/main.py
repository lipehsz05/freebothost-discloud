import discord
from discord.ext import commands
import os
from datetime import datetime

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está online!')
    print(f'📊 Servindo {len(bot.guilds)} servidores')
    print(f'🤖 Hospedado na Discloud - Plano Gratuito')

@bot.command()
async def ping(ctx):
    """Testa a latência do bot"""
    await ctx.send('🏓 Pong!')

@bot.command()
async def info(ctx):
    """Mostra informações do bot"""
    embed = discord.Embed(
        title='🤖 Informações do Bot',
        description='Bot hospedado gratuitamente na Discloud!',
        color=0x00D9FF
    )
    
    embed.add_field(
        name='📊 Uptime',
        value=f'{bot.uptime} segundos',
        inline=True
    )
    
    embed.add_field(
        name='🏠 Servidores',
        value=f'{len(bot.guilds)}',
        inline=True
    )
    
    embed.add_field(
        name='👥 Usuários',
        value=f'{len(bot.users)}',
        inline=True
    )
    
    embed.set_footer(text='Hospedado na Discloud - 100MB RAM Gratuito')
    
    await ctx.send(embed=embed)

@bot.command()
async def help_custom(ctx):
    """Mostra lista de comandos"""
    embed = discord.Embed(
        title='📚 Comandos Disponíveis',
        description='Lista de comandos do bot:',
        color=0x00FF88
    )
    
    embed.add_field(
        name='!ping',
        value='Testa a latência do bot',
        inline=False
    )
    
    embed.add_field(
        name='!info',
        value='Mostra informações do bot',
        inline=False
    )
    
    embed.add_field(
        name='!help_custom',
        value='Mostra esta lista de comandos',
        inline=False
    )
    
    embed.set_footer(text='Bot hospedado gratuitamente na Discloud')
    
    await ctx.send(embed=embed)

# Tratamento de erros
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('❌ Comando não encontrado! Use `!help_custom` para ver os comandos disponíveis.')
    else:
        print(f'❌ Erro: {error}')

# Use variável de ambiente para o token
bot.run(os.getenv('TOKEN'))
