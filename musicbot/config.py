import toml
import logging
import os

EXAMPLE_CONFIG = """\"token\"=\"\" # the bot's token
\"prefix\"=\"!\" # prefix used to denote commands

[music]
# Options for the music commands
"max_volume"=250 # Max audio volume. Set to -1 for unlimited.
"vote_skip"=true # whether vote-skipping is enabled
"vote_skip_ratio"=0.5 # the minimum ratio of votes needed to skip a song
[tips]
"github_url"="https://github.com/joek13/py-music-bot"
"""


def load_config(path="./config.toml"):
    """Loads the config from `path`"""
    if os.path.exists(path) and os.path.isfile(path):
        config = toml.load(path)
    else:
        with open(path, "w") as f:
            f.write(EXAMPLE_CONFIG)
            logging.warning(
                f"No config file found. Creating a default config file at {path}"
            )
        config = toml.load(path)

    # ✅ Override with environment variables if available
    if os.getenv("TOKEN"):
        config["token"] = os.getenv("TOKEN")
    if os.getenv("PREFIX"):
        config["prefix"] = os.getenv("PREFIX")

    return config