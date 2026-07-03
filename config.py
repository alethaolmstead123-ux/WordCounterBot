import os
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN not set!")
    exit(1)
print("✅ BOT_TOKEN loaded!")
