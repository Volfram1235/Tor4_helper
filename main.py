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

async def clear( ctx, amount = 100 ):
    await ctx.channel.purge( limit = amount + 1 )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )
    await member.kick( reason = reason )
    await ctx.send( f'{member.mention} успешно кикнут!' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
    await ctx.channel.purge( limit = 1 )
    await member.ban( reason = reason )
    await ctx.send( f'{member.mention} успешно забанен!' )

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def pardon( ctx, *, member ):
    await ctx.channel.purge( limit = 1 )

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send(f'{user.mention} успешно разбанен!')
        return

@client.command( pass_context = True )

async def help( ctx ):
    emb = discord.Embed( title = 'Список команд' )

    emb.add_field( name = '{}clear'.format(PREFIX), value = 'Отчистка чата\n' )
    emb.add_field(name='{}kick'.format(PREFIX), value='Кик с сервера\n')
    emb.add_field(name='{}ban'.format(PREFIX), value='Бан\n')
    emb.add_field(name='{}pardon'.format(PREFIX), value='Разбан')

    await ctx.send( embed = emb )


token = open( 'token', 'r' ).readline()
client.run( token )
