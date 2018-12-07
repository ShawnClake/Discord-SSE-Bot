from discord import PermissionOverwrite, Guild

class OnJoin:
    @staticmethod
    async def on_join(user):
        guild: Guild = user.guild

        overwrites = {
            guild.default_role: PermissionOverwrite(read_messages=False),
            user: PermissionOverwrite(read_messages=True, send_messages=True)
        }

        # Check to see if the channel category exists.
        categories = guild.categories

        self_management = [channel for channel in categories if channel.name == "Self-Management"]

        if self_management:
            channel = await guild.create_text_channel(str(user), overwrites=overwrites, category=self_management[0])
        else:
            self_management = await guild.create_category("Self-Management")
            channel = await guild.create_text_channel(str(user), overwrites=overwrites, category=self_management)

        await channel.send("Hello, " + user.mention + "! Welcome to our discord server! Give yourself roles by typing /role in any text channel.")
        await channel.send("/help")

    @staticmethod
    async def on_ready(bot):
        # Get all channels that are in the self-management category.
        channels = [channel for channel in bot.get_all_channels() if channel.category and channel.category.name == "Self-Management"]
        # Get all members in the discord who are not admins.
        members = [member for member in bot.get_all_members() if member.top_role.name != "UR SSE Bot"]

        # Loop through all guilds that the bot is registered to
        # This ensures if players joined the guild while the bot was offline it creates a channel for them.
        for guild in bot.guilds:

            # Loop all non-admins
            for member in members:
                # Check if the user has their own channel
                self_channel = [channel for channel in channels if channel.topic == str(member.id)]

                if not self_channel:
                    # Get the self-management category to add text channels to.
                    categories = guild.categories
                    self_management = [channel for channel in categories if channel.name == "Self-Management"]

                    # If it doesn't exist, delete the category.
                    if self_management:
                        self_management = self_management[0]
                    else:
                        self_management = await guild.create_category("Self-Management")

                    # Generate the permissions for the channel
                    overwrites = {
                        guild.default_role: PermissionOverwrite(read_messages=False),
                        member: PermissionOverwrite(read_messages=True, send_messages=True)
                    }

                    # Create the private channel for the user
                    channel = await guild.create_text_channel(str(member),
                                                    overwrites=overwrites,
                                                    category=self_management)

                    await channel.edit(topic=str(member.id))