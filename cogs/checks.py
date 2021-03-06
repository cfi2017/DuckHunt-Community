# -*- coding: utf-8 -*-
import discord
from discord.ext import commands


def get_level(user: discord.user):
    top_role = user.top_role.name.lower()

    if top_role.id == '306076806371344385': # Owner
        return 5
    elif top_role.id == '195261182729256961': # Admin
        return 4
    elif top_role.id == '285752516589649922': # Moderator
        return 3
    elif top_role.id == '304949336989630466': # Proficient
        return 2
    elif top_role.id == '306078530712633346': # NoBoat
        return 0
    else:
        return 1


def have_required_level(required: int = 0, warn: bool = True):
    """
    Check if a player have the required access to perform a command.

    Access integers translate to the following roles :

    0 : banned user
    1 : normal user
    2 : helper user
    3 : moderator user
    4 : admin user
    5 : owner user
    :param required: An integer, the minimal access required to access the command.
    :param warn: Boolean. If true, the bot will send a message explaining why the sender could not access the command
    """

    def check(ctx, warn):
        level = get_level(ctx.message.author)
        access = level >= required
        if not access and warn:
            ctx.bot.loop.create_task(ctx.bot.send_message(ctx.message.channel,
                                                          "{mention} : :x: You don't have access to this command. Your current level is **{level}**, and this command requires a level **{minlevel}** access. If you think that this is an error, please contact Eyesofcreeper.".format(level=level, minlevel=required, mention=ctx.message.author.mention)))

        return access

    owner = commands.check(lambda ctx: check(ctx, warn))
    return owner
