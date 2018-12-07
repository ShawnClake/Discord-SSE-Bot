from discord import PermissionOverwrite

class OnJoin:
    @staticmethod
    async def on_join(user):
        guild = user.guild

        overwrites = {
            guild.default_role: PermissionOverwrite(read_messages=False),
            user: PermissionOverwrite(read_messages=True, send_messages=True)
        }

        # Check to see if the channel category exists.


        channel = await guild.create_text_channel(str(user), overwrites=overwrites)
        await channel.send("Hello, " + user.mention + "! Welcome to our discord server! Give yourself roles by typing /role in any text channel.")
        await channel.send("/help")