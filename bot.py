import discord
from discord.ext import commands
from config import TOKEN

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("Basic Boy is online")


@client.command()
async def hello(ctx):
    await ctx.send("Hi!")


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="Not provided"):
    await member.send(f"You have been kicked! from Bot testing \nReason: {reason}")
    await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason="Not provided"):
    await ctx.send(f"{member.name} has been banned! \nReason: {reason}")
    await member.ban(reason=reason)


@client.command(aliases=['ub'])
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc, = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f"{member_name} has been unbanned!")
            return
    await ctx.send(f"{member} was not found!")

client.run(TOKEN)
