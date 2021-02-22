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

import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.general_channel = bot.general_channel
        self.nitro_booster_role = bot.nitro_booster_role

    # TODO: Fazer uma mensagem de bem-vindo agradável.
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.bot:
            return

        embed = discord.Embed(
            title='Um membro entrou no servidor!',
            description=f'{member.mention} entrou no servidor! ❤️\n\nNão se esqueça de ler as <#795029002225451048>!',
            color=self.bot.color
        )

        await self.general_channel.send(member.mention, embed=embed)

    # RELATED: https://github.com/discord/discord-api-docs/issues/1182
    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if before.roles == after.roles:
            return

        has_boosted_before = self.nitro_booster_role in before.roles
        has_boosted_after = self.nitro_booster_role in after.roles

        if not has_boosted_before and has_boosted_after:
            embed = discord.Embed(
                title=f'{after.name} impulsionou o servidor!',
                description=f'Uma chuva de aplausos! {after.mention} impulsionou o servidor! ❤️',
                color=self.nitro_booster_role.color
            )

            await self.general_channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))
