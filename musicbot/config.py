import os

def load_config():
    return {
        "token": os.getenv("DISCORD_TOKEN", ""),   # Bot token
        "prefix": os.getenv("BOT_PREFIX", "!"),    # Command prefix
        "max_volume": int(os.getenv("MAX_VOLUME", "250")),
        "vote_skip": os.getenv("VOTE_SKIP", "true").lower() == "true",
        "vote_skip_ratio": float(os.getenv("VOTE_SKIP_RATIO", "0.5")),
        "github_url": os.getenv("GITHUB_URL", "https://github.com/joek13/py-music-bot")
    }