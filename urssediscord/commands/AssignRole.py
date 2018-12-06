from discord.ext.commands.context import Context
from discord import Server, Member
from discord.utils import get
from discord.ext.commands import Bot

class AssignRole:

    @staticmethod
    async def role(ctx: Context):
        # Get the user who sent the command
        user: Member = ctx.message.author
        server: Server = ctx.message.server
        bot: Bot = ctx.bot

        # Parse the sent in command and split the command in whitespace.
        arguments = ctx.message.content.split(' ')[1:]

        # Get the UR SSE Bot role
        bot_role = get(server.roles, name="UR SSE Bot")

        # Allow users to assign themselves to any role under the bot.
        roles = [role for role in server.roles if role < bot_role and "@" not in role.name]

        # If no arguments are passed, return the help information.
        if not arguments:
            # Send information about all possible server roles.
            message = "You have not specified a role.\nThe possible roles are: "

            for role in roles:
                message += role.name.replace(' ', '-') + ", "

            # Trim the trailing ', '
            message = message[:-2]

            message += ". \nCommand use: /role [<role> <role> ...]"
            message += "\nTo remove a role, add an ! in front of the role name. ex. /role !4th-year"
            await ctx.bot.say(message)
            return

        # Strings that the bot will reply with
        added_roles = ""
        removed_roles = ""
        unassignable_roles = ""
        non_existing_roles = ""

        # Loop through passed arguments.
        for arg in arguments:
            remove = False

            # Check to see if the user is trying to remove a role.
            if arg != arg.replace('!', ''):
                arg = arg.replace('!', '')
                remove = True

            # Check if the role exists
            role = get(server.roles, name=arg.replace('-', ' '))

            # if the role exists, check if the user has permission to assign the role.
            if role:
                # Check if the role is in the potential role list.
                if role in roles:
                    if remove:
                        await bot.remove_roles(user, role)
                        removed_roles += str(arg) + ", "
                    else:
                        # The role matches a discord role, assign the user the role.
                        await bot.add_roles(user, role)
                        added_roles += str(arg) + ", "
                else:
                    # The role cannot be assigned.
                    unassignable_roles += str(arg) + ", "
            else:
                # Role does not exist.
                non_existing_roles  += str(arg) + ", "

        message = ""

        if added_roles != "":
            message += "You were granted the " + added_roles[:-2] + " role(s)!\n"

        if removed_roles != "":
            message += "You were removed from the " + removed_roles[:-2] + " role(s)!\n"

        if unassignable_roles != "":
            message += "You are too much of a noob for the " + unassignable_roles[:-2] + " role(s), scrub!\n"

        if non_existing_roles != "":
            message += "You thought " + non_existing_roles[:-2] + " role(s) existed? You were wrong! '/roles' for help\n"

        await ctx.bot.say(message)
