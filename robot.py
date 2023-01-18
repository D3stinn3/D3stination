import discord
import random
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!')

giveaway_msg = None
giveaway_item = None


@bot.command()
async def startgiveaway(ctx, item: str, duration: int):
    """Starts a new giveaway for an item, with a specified duration in minutes"""
    global giveaway_msg, giveaway_item
    if giveaway_msg is not None:
        await ctx.send("A giveaway is already in progress.")
        return

    giveaway_item = item
    giveaway_msg = await ctx.send(f"A new giveaway has started for {item}! It will end in {duration} minutes.")
    await giveaway_msg.add_reaction("🎉")
    await asyncio.sleep(duration * 60)

    if giveaway_msg is None:
        await ctx.send("No giveaway is in progress.")
        return

    await giveaway_msg.clear_reactions()
    winners = await get_winners(giveaway_msg)
    await giveaway_msg.edit(content=f"The giveaway for {giveaway_item} has ended. The winner(s) are {winners}.")

    giveaway_msg = None
    giveaway_item = None


@bot.command()
async def endgiveaway(ctx):
    """Ends the current giveaway"""
    global giveaway_msg, giveaway_item
    if giveaway_msg is None:
        await ctx.send("No giveaway is in progress.")
        return
    await giveaway_msg.clear_reactions()
    winners = await get_winners(giveaway_msg)
    await giveaway_msg.edit(content=f"The giveaway for {giveaway_item} has ended early. The winner(s) are {winners}.")
    giveaway_msg = None
    giveaway_item = None


async def get_winners(giveaway_message):
    """Selects random winners from the users who reacted to the giveaway message"""
    reactions = giveaway_message.reactions
    if len(reactions) == 0:
        return "No one entered the giveaway."
    winners = []
    for reaction in reactions:
        users = await reaction.users().flatten()
        winners.extend(random.sample(users, min(len(users), reaction.count)))
    return ", ".join([user.mention for user in winners])


bot.run('token')
