import discord
from discord.ext import commands
import random

PREFIX = '$'

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( 'help' )


@client.event

async def on_ready():
    print( 'Bot ready to work, logged as {0.user}'.format(client) )

@client.command( pass_context = True )

async def clear( ctx, amount = 1 ):
    await ctx.channel.purge( limit = amount + 1 )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
    emb = discord.Embed(title='Готово!', colour=discord.Color.gold())

    emb.add_field(name='{} успешно кикнут!'.format(member.display_name), value='Справедливо...')

    await ctx.channel.purge( limit = 1 )
    await member.kick( reason = reason )
    await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
    emb = discord.Embed(title='Готово!', colour=discord.Color.dark_red())

    emb.add_field(name='{} успешно забанен!'.format(member.display_name), value='Справедливо...')

    await ctx.channel.purge( limit = 1 )
    await member.ban( reason = reason )
    await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def pardon( ctx, *, member ):
    emb = discord.Embed(title='Готово!', colour=discord.Color.green())
    await ctx.channel.purge( limit = 1 )

    emb.add_field(name='Пользователь успешно разбанен!', value='Справедливо...')

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send( embed = emb )
        return

@client.command( pass_context = True )

async def help( ctx ):
    emb = discord.Embed( title = 'Список команд', colour = discord.Color.purple() )

    emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
    emb.add_field( name = '{}clear'.format(PREFIX), value = 'Отчистка чата\n' )
    emb.add_field( name='{}kick'.format(PREFIX), value='Кик с сервера\n')
    emb.add_field( name='{}ban'.format(PREFIX), value='Бан\n')
    emb.add_field( name='{}pardon'.format(PREFIX), value='Разбан')
    emb.add_field(name='{}mute'.format(PREFIX), value='Замютить')

    await ctx.send( embed = emb )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def mute( ctx, member: discord.Member ):
    emb = discord.Embed(title='Готово!', colour=discord.Color.dark_gray())
    mute_role = discord.utils.get( ctx.message.guild.roles, name = 'mute' )

    emb.add_field( name = '{} успешно замючен!'.format(member.display_name), value = 'Справедливо...' )

    await member.add_roles( mute_role )
    await ctx.send( embed = emb )

@client.event
async def on_command_error( ctx, error ):
    pass

token = open( 'token', 'r' ).readline()
client.run( token )
