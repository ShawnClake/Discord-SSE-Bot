from discord import PermissionOverwrite, Guild

async def on_join(user):
    guild: Guild = user.guild

    # Check if the user's channel already exists.
    self_channel = [channel for channel in guild.channels if channel.topic == str(user.id)]
    if self_channel:
        return

    # Check to see if the channel category exists.
    categories = guild.categories

    self_management = [channel for channel in categories if channel.name == "Self-Management"]


    overwrites = {
        guild.default_role: PermissionOverwrite(read_messages=False),
        user: PermissionOverwrite(read_messages=True, send_messages=True)
    }

    if self_management:
        channel = await guild.create_text_channel(str(user), overwrites=overwrites, category=self_management[0])
    else:
        self_management = await guild.create_category("Self-Management")
        channel = await guild.create_text_channel(str(user), overwrites=overwrites, category=self_management)
    await channel.edit(topic=str(user.id))

    await channel.send("Hello, " + user.mention + "! Welcome to our discord server! Give yourself roles by typing /role.")
    await channel.send("Get /help")