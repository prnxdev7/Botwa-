import discord
import logging
import sys
import os
from discord.ext import commands

# Import from package
from musicbot.cogs import music, error, meta, tips
from musicbot import config

# Load config
cfg = config.load_config()

# Override token with ENV if available
TOKEN = os.getenv("DISCORD_TOKEN", cfg.get("token", ""))

# Set up logging
logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix=cfg["prefix"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    logging.info(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

# List of all cogs
COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize and add cog

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