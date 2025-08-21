import discord
import logging
import sys
from discord.ext import commands
from cogs import music, error, meta, tips
import config

# Load config
cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["prefix"], intents=discord.Intents.all())

@bot.event
async def on_ready():
    logging.info(f"✅ Logged in as {bot.user} (ID: {bot.user.id})")

COGS = [music.Music, error.CommandErrorHandler, meta.Meta, tips.Tips]

def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize each cog

def run():
    add_cogs(bot)
    if cfg["token"] == "":
        raise ValueError("❌ No token found. Please set DISCORD_TOKEN in environment variables.")
        sys.exit(1)
    bot.run(cfg["token"])

if __name__ == "__main__":
    run()