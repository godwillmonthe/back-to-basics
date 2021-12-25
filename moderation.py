import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
