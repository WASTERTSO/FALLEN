# FallenRobot/modules/disable.py

from telegram.ext import CommandHandler
from telegram import Update
from FallenRobot import dispatcher, DEV_USERS

class DisableAbleCommandHandler(CommandHandler):
    def __init__(self, command, callback, **kwargs):
        super().__init__(command, callback, **kwargs)
        self.disableable = True

    def handle_update(self, update: Update, context):
        if self.disableable:
            return super().handle_update(update, context)
        else:
            return

def disable_command(update: Update, context):
    if (link unavailable) in DEV_USERS:
        command = context.args[0]
        dispatcher.disable_command(command)
        update.effective_message.reply_text(f"Command '{command}' disabled.")
    else:
        update.effective_message.reply_text("You don't have permission to disable commands.")

def enable_command(update: Update, context):
    if (link unavailable) in DEV_USERS:
        command = context.args[0]
        dispatcher.enable_command(command)
        update.effective_message.reply_text(f"Command '{command}' enabled.")
    else:
        update.effective_message.reply_text("You don't have permission to enable commands.")

dispatcher.add_handler(DisableAbleCommandHandler("disable", disable_command))
dispatcher.add_handler(DisableAbleCommandHandler("enable", enable_command))

__mod_name__ = "Disable"
__help__ = """
/disable <command> - Disable a command.
/enable <command> - Enable a command.
"""
