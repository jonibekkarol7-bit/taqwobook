import os

class Config:
    # ─── BOT TOKEN ──────────────────────────────────────────────────────────────
    # BotFather dan olingan token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # ─── KANALLAR ───────────────────────────────────────────────────────────────
    TELEGRAM_CHANNEL = "@taqwobook"        # Telegram kanal
    INSTAGRAM_USERNAME = "@taqwobook"     # Instagram sahifa

    # ─── ADMIN IDs ──────────────────────────────────────────────────────────────
    # @userinfobot ga yozing va o'z ID ingizni qo'ying
    ADMIN_IDS = [
        int(x) for x in os.environ.get("ADMIN_IDS", "").split(",")
        if x.strip().isdigit()
    ]

    # ─── DATABASE ───────────────────────────────────────────────────────────────
    DB_PATH = "taqwobook.db"
