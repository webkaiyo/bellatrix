'''
MIT License

Copyright (c) 2021 Caio Alexandre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import logging

import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        bot.loop.create_task(self.update_status())

    async def update_status(self):
        users = len(self.bot.users)

        name = f'{users} usuários'
        activity_type = discord.ActivityType.listening

        activity = discord.Activity(name=name, type=activity_type)
        status = discord.Status.dnd

        await self.bot.change_presence(activity=activity, status=status)

    @commands.Cog.listener()
    async def on_member_join(self, guild: discord.Guild):
        await self.update_status()

    @commands.Cog.listener()
    async def on_member_remove(self, guild: discord.Guild):
        await self.update_status()


def setup(bot: commands.Bot):
    bot.add_cog(Status(bot))