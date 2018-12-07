from discord import PermissionOverwrite, Colour, Permissions


async def on_ready(bot):
    # Loop all the guilds that the box exists in
    for guild in bot.guilds:
        await create_categories(guild)
        await create_roles(guild)
        await create_private_channels(bot, guild)


async def create_categories(guild):
    await _create_category("Self-Management", guild)


async def create_roles(guild):
    await _create_role(guild, "SSE Insider", Permissions(), Colour.from_rgb(83, 92, 238))


async def _create_category(name, guild):
    self_management = [channel for channel in guild.categories if channel.name == name]

    # If it doesn't exist, delete the category.
    if not self_management:
        await guild.create_category("Self-Management")


async def _create_role(guild, name, permissions, colour):
    role = [role for role in guild.roles if role.name == name]

    # Get the Bot's role.
    bot_role = [role for role in guild.roles if role.name == "UR SSE Bot"][0]

    # Create if the role doesn't exist.
    if not role:
        role = await guild.create_role(name=name, colour=colour, permissions=permissions)
        # The bot cannot create a role higher or equal to itself.
        await role.edit(position=(bot_role.position - 1))


async def create_private_channels(bot, guild):
    # Get all channels that are in the self-management category.
    channels = [channel for channel in bot.get_all_channels() if
                channel.category and channel.category.name == "Self-Management"]

    # Get all members in the discord who are not the bot.
    members = [member for member in bot.get_all_members() if member.top_role.name != "UR SSE Bot"]

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


