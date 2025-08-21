import discord
import logging
import sys
import os
from discord.ext import commands
from cogs import music, error, meta, tips
import config

# Load config
cfg = config.load_config()

# Override token with ENV if available
TOKEN = os.getenv("DISCORD_TOKEN", cfg.get("token", ""))

bot = commands.Bot(command_prefix=cfg["prefix"])


@bot.event
async def on_ready():
    logging.info(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")


COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if TOKEN == "":
        raise ValueError(
            "❌ No token found. Please set DISCORD_TOKEN in environment variables "
            "or add it inside config.toml"
        )
        sys.exit(1)
    bot.run(TOKEN)


if __name__ == "__main__":
    run()